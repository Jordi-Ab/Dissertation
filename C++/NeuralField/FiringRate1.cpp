#include "FiringRate1.hpp"

FiringRate1::FiringRate1(double decay, double threshold){
    _miu = decay;
    _theta = threshold;
}

/*
double FiringRate1::evaluateAt(double u_i){
    return 1 / (1 + exp(- _miu * (u_i - _theta) ));
}*/

double FiringRate1::evaluateAt(double u_i){
    return 1 / (1 + exp( -_miu*u_i + _theta )) - 1/(1 + exp(_theta));
}
