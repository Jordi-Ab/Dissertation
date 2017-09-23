#ifndef CONNECTIVITYKERNEL1_HPP
#define CONNECTIVITYKERNEL1_HPP

#include <iostream>
#include <cmath>
#include "Vector.hpp"


class ConnectivityKernel1{
public:
    ConnectivityKernel1(double b=1);
    double evaluateAt(Vector& x);
private:
    double _b;
};

#endif // CONNECTIVITYKERNEL1_HPP
