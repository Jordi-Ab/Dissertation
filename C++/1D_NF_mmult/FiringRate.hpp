#ifndef FIRINGRATE_HPP
#define FIRINGRATE_HPP

#include <cmath>
#include "Vector.hpp"

class FiringRate{

public:
    FiringRate(double decay, double threshold);
    void evaluateAt(const Vector& u, Vector& result);

private:

    double _miu;
    double _theta;

    double f(double x);
};

#endif // FIRINGRATE_HPP
