#ifndef RUNGEKUTTA4SOLVER_HPP
#define RUNGEKUTTA4SOLVER_HPP

#include "AbstractODESolver.hpp"
#include <string>
#include <iostream>
class RK4Solver : public AbstractODESolver{

public:

    // Constructor
    RK4Solver(ODEInterface& an_ODESystem,
              const Vector& initial_value,
              const double initial_time,
              const double final_time,
              const double step_size,
              const std::string output_file_name,
              const int save_gap,
              const int print_gap);

    /*Its own print header method*/
    void printHeader();

    /*
     * Function: advance
     * ---------------------------
     * Overwrites the virtual "advance" function of AbstractODESolver.
     * Implements Runge-Kutta4 Formula to advance one step in time.
     * The result of the step taken will get stored in the given
     * "result vector"
    */
    void advance(const double current_t,
                 const Vector& current_state,
                 Vector& result);


private:

    RK4Solver();

};

#endif // RUNGEKUTTA4SOLVER_HPP
