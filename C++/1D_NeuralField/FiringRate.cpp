#include "FiringRate.hpp"

FiringRate::FiringRate(double decay, double threshold){
    _miu = decay;
    _theta = threshold;
}

/*
double FiringRate::evaluateAt(double u_i){
    return 1 / (1 + exp(- _miu * (u_i - _theta) ));
}*/

double FiringRate::evaluateAt(double x){
    return 1 / (1 + exp( -_miu*x + _theta )) - 1/(1 + exp(_theta));
}
