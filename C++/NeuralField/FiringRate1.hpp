#ifndef FIRINGRATE1_HPP
#define FIRINGRATE1_HPP

#include <iostream>
#include <cmath>
#include "Vector.hpp"

class FiringRate1{
public:
    FiringRate1(double decay, double threshold);

    double evaluateAt(double u_i);

private:
    double _miu;
    double _theta;

};

#endif // FIRINGRATE1_HPP
