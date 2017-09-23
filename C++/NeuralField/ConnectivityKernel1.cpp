#include "ConnectivityKernel1.hpp"

ConnectivityKernel1::ConnectivityKernel1(double b){
    _b = b;
}

double ConnectivityKernel1::evaluateAt(Vector& x){
    double x_val = x.Norm(2);
    return exp( -_b*x_val )*( _b*sin(x_val) + cos(x_val) );
}
