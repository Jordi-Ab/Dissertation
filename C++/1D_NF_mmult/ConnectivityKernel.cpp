#include "ConnectivityKernel.hpp"

ConnectivityKernel::ConnectivityKernel(double b){
    _b = b;
}

double ConnectivityKernel::evaluateAt(double x){
    return exp( -_b*std::abs(x) )*( _b*sin(std::abs(x)) + cos(x) );
}
