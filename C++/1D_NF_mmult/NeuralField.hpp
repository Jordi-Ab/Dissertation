#ifndef NEURALFIELD_HPP
#define NEURALFIELD_HPP

#include "Vector.hpp"
#include "Matrix.hpp"
#include "ODEInterface.hpp"
#include "FiringRate.hpp"

class NeuralField: public ODEInterface{
public:

    // Constructor
    NeuralField(Matrix& synaptic_kernel,
                FiringRate& firing_rate);

    // FUNCTIONS
    void evaluateAt(const double t,
                    const Vector& u,
                    Vector& new_u) const;
private:

    // VARIABLES
    Matrix* _W;
    FiringRate* _f_rate;

};

#endif // NEURALFIELD_HPP
