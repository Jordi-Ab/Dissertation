#ifndef NEURALFIELD_HPP
#define NEURALFIELD_HPP

#include <vector>
#include "Vector.hpp"
#include "ODEInterface.hpp"
#include "ConnectivityKernel1.hpp"
#include "FiringRate1.hpp"


class NeuralField: public ODEInterface{
public:

    // CONSTRUCTOR
    NeuralField(ConnectivityKernel1& synaptic_kernel,
                FiringRate1& firing_rate,
                std::vector<Vector>& points_mesh,
                std::vector<double>& integral_weights,
                std::vector<Vector>& vertices,
                std::vector< std::vector<int> >& elems);

    // FUNCTIONS
    void evaluateAt(const double t,
                    const Vector& u,
                    Vector& new_u) const;

private:

    // INSTANCE VARIABLES
    ConnectivityKernel1* _ker;
    FiringRate1* _f_rate;
    std::vector<Vector>* _interior_points;
    std::vector<double>* _weights;
    std::vector<Vector>* _vertices;
    std::vector< std::vector<int> >* _elems;

    // FUNCTIONS
    double computeIntegral(const Vector& u,
                           const Vector& x_i) const;
    double computeArea(int elem_index) const;

};

#endif // NEURALFIELD_HPP
