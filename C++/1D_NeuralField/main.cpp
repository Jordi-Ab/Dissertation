#include <iostream>
#include <vector>
#include <cmath>
#include "ConnectivityKernel.hpp"
#include "FiringRate.hpp"
#include "helpers.hpp"
#include "NeuralField.hpp"
#include "RungeKutta4Solver.hpp"

const std::string WD = "/Users/user/Documents/Maestria/Dissertation/Code/Dissertation_git/C++/1D_NeuralField";
double initCondition(double A, double alpha, double x);

int main(){

    std::cout << "Running..." << std::endl;
    std::cout << "" << std::endl;

    Helpers hlp; // A set of useful functions

    // Spatial Grid
    int Nx = pow(2.0,10.0)-1; // Number of points in the space grid
    double Lx = 30; // Space grid limits
    double hx = 2*Lx/(double)Nx; // Space width between points in the grid

    // nx equally spaced points between -Lx and Lx
    double *xs = new double[Nx];
    hlp.linspace(-Lx, Lx, Nx, xs);

    // Save Mesh.
    std::string mesh_filename = WD+"/OutputData/mesh.dat";
    hlp.saveGrid(mesh_filename, xs, Nx);

    // Parameter values
    double miu = 50;
    double theta = 0.5;
    double b = 1;

    // Initialize Objects
    ConnectivityKernel ker(b);
    FiringRate f_rate(miu, theta);

    // Integral Weights
    //double *ws = new double[nx];
    //for(int i=0; i<nx; i++){
    //    ws[i] = hx;
    //}

    // Initialize Neural Field.
    NeuralField rhs(ker, f_rate, xs, Nx);

    /* TIME STEP USING ODE SOLVERS:*/

    // Initial Condition
    Vector init_cond(Nx);
    double A = 10;
    double alpha = 0.1;
    for(int i=0; i<Nx; i++){
        init_cond[i] = initCondition(A, alpha, xs[i]);
    }

    // Time steps
    double t0 = 0;
    double T = 100;
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

double initCondition(double A, double alpha, double x){
    return A/( pow(cosh(alpha*x),2.0) );
}
