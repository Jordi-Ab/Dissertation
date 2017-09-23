#include "FiringRate.hpp"

FiringRate::FiringRate(double decay, double threshold){
    _miu = decay;
    _theta = threshold;
}


double FiringRate::f(double x){
    //return 1 / (1 + exp(- _miu * (u_i - _theta) ));
    return 1 / (1 + exp( -_miu*x + _theta )) - 1/(1 + exp(_theta));
}

void FiringRate::evaluateAt(const Vector& u, Vector& result){
    for (int i=0; i<result.GetSize(); i++){
        result[i] = f( u.Read(i) );
    }
}
