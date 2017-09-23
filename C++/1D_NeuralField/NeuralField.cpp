#include "NeuralField.hpp"

NeuralField::NeuralField(ConnectivityKernel& synaptic_kernel,
                         FiringRate& firing_rate,
                         double* mesh,
                         int Nx){
    _ker = &synaptic_kernel;
    _f_rate = &firing_rate;
    _mesh = mesh;
    _size = Nx;
    _hx = (mesh[Nx-1] - mesh[0])/(Nx-1);
}

void NeuralField::evaluateAt(const double t,
                             const Vector& u,
                             Vector& new_u) const{

    for(int i=0; i<_size; i++){
        double x_i = _mesh[i];
        double S = computeIntegral(u, x_i);
        new_u[i] = -u.Read(i) + S + t*0;
    }
}

double NeuralField::computeIntegral(const Vector& u,
                                    double& x_i) const{
    double S=0;
    for (int j=0; j<_size; j++){
        double x_j = _mesh[j];
        double rho = _hx;
        double w = rho*_ker->evaluateAt(x_i - x_j);
        double f_u = _f_rate->evaluateAt(u.Read(j));
        S += w*f_u;
    }
    return S;
}

