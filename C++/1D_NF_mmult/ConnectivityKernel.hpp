#ifndef CONNECTIVITYKERNEL_HPP
#define CONNECTIVITYKERNEL_HPP

#include <iostream>
#include <cmath>

class ConnectivityKernel{
public:
    ConnectivityKernel(double b=1);
    double evaluateAt(double x);
private:
    double _b;
};

#endif // CONNECTIVITYKERNEL_HPP
