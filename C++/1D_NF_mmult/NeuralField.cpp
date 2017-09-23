#include "NeuralField.hpp"

NeuralField::NeuralField(Matrix& synaptic_kernel,
                         FiringRate& firing_rate){
    _W = &synaptic_kernel;
    _f_rate = &firing_rate;
}

void NeuralField::evaluateAt(const double t,
                             const Vector& u,
                             Vector& new_u) const{

    // Evaluate firing rate function at vector u.
    Vector f_u(u.GetSize());
    _f_rate->evaluateAt(u, f_u);
    Vector S =  (*_W) * f_u;
    new_u = -u + S;
}

