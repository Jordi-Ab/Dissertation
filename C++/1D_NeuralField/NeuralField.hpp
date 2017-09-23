#ifndef NEURALFIELD_HPP
#define NEURALFIELD_HPP

#include "Vector.hpp"
#include "ODEInterface.hpp"
#include "ConnectivityKernel.hpp"
#include "FiringRate.hpp"

class NeuralField: public ODEInterface{
public:

    // Constructor
    NeuralField(ConnectivityKernel& synaptic_kernel,
                FiringRate& firing_rate,
                double* mesh,
                int Nx);

    // FUNCTIONS
    void evaluateAt(const double t,
                    const Vector& u,
                    Vector& new_u) const;
private:

    // VARIABLES
    ConnectivityKernel* _ker;
    FiringRate* _f_rate;
    double* _mesh;
    int _size;
    double _hx;

    // FUNCTIONS
    double computeIntegral(const Vector& u,
                           double& x_i) const;

};

#endif // NEURALFIELD_HPP
