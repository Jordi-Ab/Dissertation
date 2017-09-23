/******************************************************************
 * Interface class for ODE problems of the type:
 *
 *  du/dt = f(t,u)
 *
 * where
 *   t is a real number
 *   u is a vector of state variables
 *******************************************************************/

#ifndef ODEINTERFACE_HPP
#define ODEINTERFACE_HPP

#include "Vector.hpp"

class ODEInterface{

  public:

    // Compute right-hand side (pure virtual)
    virtual void evaluateAt( const double t,
                             const Vector& u,
                             Vector& f ) const = 0;

    // Compute analytical solution
    virtual void ComputeAnalyticSolution( const double t, Vector& u ) const;

};


#endif // ODEINTERFACE_HPP
