#include "NeuralField.hpp"

NeuralField::NeuralField(ConnectivityKernel1& synaptic_kernel,
                         FiringRate1& firing_rate,
                         std::vector<Vector>& interior_points,
                         std::vector<double>& integral_weights,
                         std::vector<Vector>& vertices,
                         std::vector< std::vector<int> >& elems){
    _ker = &synaptic_kernel;
    _f_rate = &firing_rate;
    _interior_points = &interior_points;
    _weights = &integral_weights;
    _vertices = &vertices;
    _elems = &elems;

}

void NeuralField::evaluateAt(const double t,
                             const Vector& u,
                             Vector& new_u) const{
    int grid_size = _interior_points->size();
    for (int i=0; i<grid_size; i++){
        Vector x_i = _interior_points->at(i);
        double S = computeIntegral(u, x_i);
        double F_i = -u.Read(i) + S + t*0;
        new_u[i] = F_i;
    }
}

double NeuralField::computeIntegral(const Vector& u,
                                    const Vector& x_i) const{
    double result = 0;
    int NT = _elems->size();
    for (int l=0; l<NT; l++){
        double s=0;
        double Area = computeArea(l);
        int Ng = _weights->size();
        for(int j=0; j< Ng; j++){
            int ix = l*Ng + j;
            Vector x_j = _interior_points->at(ix);
            Vector diff = x_i - x_j;
            s += _ker->evaluateAt(diff)*_f_rate->evaluateAt(u.Read(ix))*_weights->at(j);
        }
        result += Area*s;
    }
    return result;
}

double NeuralField::computeArea(int elem_index) const{

    // Get vertices of the element
    std::vector<int> elem = _elems->at(elem_index);
    Vector v1 = _vertices->at( elem.at(0) );
    Vector v2 = _vertices->at( elem.at(1) );
    Vector v3 = _vertices->at( elem.at(2) );

    double x1 = v1[0]; double y1 = v1[1];
    double x2 = v2[0]; double y2 = v2[1];
    double x3 = v3[0]; double y3 = v3[1];

    return std::abs( x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2) )/2.0;
}
