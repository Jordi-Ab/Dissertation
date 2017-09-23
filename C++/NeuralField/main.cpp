#include <iostream>
#include <vector>
#include "Vector.hpp"
#include "ConnectivityKernel1.hpp"
#include "FiringRate1.hpp"
#include "helpers.hpp"
#include "NeuralField.hpp"
#include "RungeKutta4Solver.hpp"

const std::string WD = "/Users/user/Documents/Maestria/Dissertation/Code/Dissertation_git/C++/NeuralField";
void loadMeshGrid(std::vector<Vector> &v);
void loadConnectivityMatrix(std::vector< std::vector<int> > &v);

// Nodal Basis function for mapping to a canonical reference triangle.
double N1(double x_hat, double y_hat){return 1-x_hat-y_hat;}
double N2(double x_hat, double y_hat){return x_hat;}
double N3(double x_hat, double y_hat){return y_hat;}

Vector rho_l(Vector &v1, Vector &v2, Vector &v3,
             double x_hat, double y_hat);

void getWeightsAndPoints(int n_points,
                         std::vector<double>& ws,
                         std::vector<double>& xs,
                         std::vector<double>& ys);

/*
 * For a description of the Initial Conditions:
 * See:
 *  "CONTINUATION OF LOCALISED COHERENT STRUCTURES
 *  IN NONLOCAL NEURAL FIELD EQUATIONS"
 * By:
 *  JAMES RANKIN, DANIELE AVITABILE
 * Appendix A, page 19
*/
void initCondition1(std::vector<Vector>& points,
                   Vector& result);
void initCondition2(std::vector<Vector>& points,
                   Vector& result);
void initCondition3(std::vector<Vector>& points,
                   Vector& result);

int main(){

    std::cout << "Running..." << std::endl;
    std::cout << "" << std::endl;

    Helpers hlp; // A set of useful functions

    // Load Triangulated Mesh.
    std::vector<Vector> vertices;
    std::vector< std::vector<int> > elems;
    std::string elems_filename = WD+"/elements.dat";
    std::string verts_filename = WD+"/mesh_points.dat";

    hlp.loadMeshGrid(verts_filename, vertices);
    hlp.loadConnectivityMatrix(elems_filename, elems);
    int NT = elems.size();

    // Parameter values
    double miu = 3.4;
    double theta = 5.6;
    double b = 0.4;

    //Initialize objects
    ConnectivityKernel1 ker(b);
    FiringRate1 f_rate(miu, theta);

    // Gauss Weights and Points inside a reference triangle.
    std::vector<double> weights;
    std::vector<double> x_hat;
    std::vector<double> y_hat;

    int Np = 3; // Desired number of GaussPoints
    hlp.getGaussWeightsAndPoints(Np, weights, x_hat, y_hat);
    int Ng = weights.size(); // Effective number of Gauss Points.

    // Assemble grid of interior points.
    std::cout << "Assembling interior points mesh..." << std::endl;
    std::vector<Vector> points_grid;
    for (int i=0; i<NT; i++){
        // Get vertices of the element
        std::vector<int> elem = elems[i];
        Vector v1 = vertices[elem[0]];
        Vector v2 = vertices[elem[1]];
        Vector v3 = vertices[elem[2]];

        for (int j=0; j<Ng ; j++){
            // Map interior points of reference triangle to interior points of element.
            Vector new_point = rho_l(v1,v2,v3, x_hat[j], y_hat[j]);
            points_grid.push_back(new_point);
        }
    }

    // Save points Grid.
    std::string points_filename = WD+"/OutputData/interior_points_grid.dat";
    hlp.saveGrid(points_filename, points_grid);

    // Initialize Neural Field.
    NeuralField rhs(ker, f_rate, points_grid, weights, vertices, elems);

    /* TIME STEP USING ODE SOLVERS:*/

    // Initial Condition
    Vector init_cond( points_grid.size() );
    initCondition1(points_grid, init_cond);

    // Time steps
    double t0 = 0;
    double T = 15;
    double dt = 0.1;

    // Storing the Output
    std::string path_data_folder = WD+"/OutputData";
    std::string output_file_name = "RK4_output.dat";
    bool use_complete_path = true;

    // Initialize Runge-Kutta4 solver
    RK4Solver RK4(rhs,init_cond,t0,T,dt,output_file_name,1,1);

    RK4.setOutputFolder(path_data_folder);
    RK4.useCompletePath(use_complete_path);

    // Solve. save=true, print=false.
    std::cout << "Solving..." << std::endl;
    RK4.solve(true, false);

    std::cout << "Finish" << std::endl;
    return 0;
}

Vector rho_l(Vector &v1, Vector &v2, Vector &v3, double x_hat, double y_hat){
    /*
        v1, v2, v3 are Vectors containing x and y
        i.e. v1 = [x1, y1],
        and represent the vertices of a triangular element.
        x_hat is the x value of a point inside the refernce triangle
        y_hat is the y value of a point inside the reference triangle
    */
    Vector result(2);
    // Map gauss points inside the triangle using the Nodal Basis Functions
    double x = v1[0]*N1(x_hat, y_hat) + v2[0]*N2(x_hat, y_hat) + v3[0]*N3(x_hat, y_hat);
    double y = v1[1]*N1(x_hat, y_hat) + v2[1]*N2(x_hat, y_hat) + v3[1]*N3(x_hat, y_hat);
    result[0] = x; result[1] = y;
    return result;
}

void initCondition1(std::vector<Vector>& points,
                   Vector& result){
    int n = points.size();
    for(int i=0; i<n; i++){
        double x = points[i][0];
        double y = points[i][1];

        result[i] = 6.0*exp( -( x*x + y*y )/5.77 );
    }
}

void initCondition2(std::vector<Vector>& points,
                   Vector& result){
    int n = points.size();
    for(int i=0; i<n; i++){
        double x = points[i][0];
        double y = points[i][1];
        double e = exp( -( x*x + y*y )/100.0 );
        double cos1 = cos(x);
        double cos2 = cos( 0.5*x + ( sqrt(3)/2.0 )*y );
        double cos3 = cos( -0.5*x + ( sqrt(3)/2.0 )*y );

        result[i] = 2*e*(cos1 + cos2 + cos3);
    }
}

void initCondition3(std::vector<Vector>& points,
                   Vector& result){
    int n = points.size();
    for(int i=0; i<n; i++){
        double x = points[i][0];
        double y = points[i][1];
        double e = exp( -( x*x + y*y )/100.0 );

        result[i] = 2*e*( -cos(x) -sin(y) );
    }
}



