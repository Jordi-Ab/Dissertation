#include "RungeKutta4Solver.hpp"

RK4Solver::RK4Solver(ODEInterface& an_ODESystem,
                     const Vector& initial_value,
                     const double initial_time,
                     const double final_time,
                     const double step_size,
                     const std::string output_file_name,
                     const int save_gap,
                     const int print_gap){


    // Private Instances of AbstractODE
    setStepSize(step_size);
    setInitialState(initial_value);
    setTimeInterval(initial_time, final_time);

    // Protected Instances of AbstractODE
    _ODEObject = &an_ODESystem;
    _output_file_name = output_file_name;

    if (save_gap <= 0) _save_gap = 1;
    else if (save_gap >= final_time/step_size) _save_gap = final_time;
    else _save_gap = save_gap;

    if (print_gap <= 0) _print_gap = 1;
    else if (print_gap >= final_time/step_size) _print_gap = final_time;
    else _print_gap = print_gap;

}

void RK4Solver::advance(const double current_t,
                        const Vector& current_state,
                        Vector& result){

    double h = getStepSize();
    double size = current_state.GetSize();

    Vector k1(size);
    Vector k2(size);
    Vector k3(size);
    Vector k4(size);

    _ODEObject->evaluateAt(current_t, current_state, k1);
    k1 = k1*h;
    _ODEObject->evaluateAt(current_t + h/2.0, current_state + k1*0.5, k2);
    k2 = k2*h;
    _ODEObject->evaluateAt(current_t + h/2.0, current_state + k2*0.5, k3);
    k3 = k3*h;
    _ODEObject->evaluateAt(current_t + h, current_state + k3, k4);
    k4 = k4*h;

    result = current_state + (k1 + k2*2 + k3*2 + k4)*(1/6.0);

}

void RK4Solver::printHeader(){
    std::cout << "" << std::endl;
    std::cout << "Approximating solution using Runge-Kutta4 Method." << std::endl;
    std::cout << "" << std::endl;
    std::cout << "  Initial Time: " << getInitialTime() << std::endl;
    std::cout << "  Final Time: " << getFinalTime() << std::endl;
    std::cout << "  Step Size: " << getStepSize() << std::endl;
    std::cout << "  Number of Steps: " << getFinalTime()/getStepSize() << std::endl;

    if (getInitialState().GetSize() > 3){
        std::cout << "* Note: Will just print the first 3 components of the ";
        std::cout << "solutions vector on screen." << std::endl;
    }
    std::cout << "" << std::endl;
}





