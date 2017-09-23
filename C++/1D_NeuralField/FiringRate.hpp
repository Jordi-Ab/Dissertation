#ifndef FIRINGRATE_HPP
#define FIRINGRATE_HPP

#include <cmath>

class FiringRate{

public:
    FiringRate(double decay, double threshold);
    double evaluateAt(double u_i);

private:
    double _miu;
    double _theta;
};

#endif // FIRINGRATE_HPP
