#include "AbstractODESolver.hpp"

AbstractODESolver::~AbstractODESolver() {
    delete _initial_state;
    if (_output_file.is_open()) _output_file.close();
}

void AbstractODESolver::setOutputFolder(const std::string folder_path){
    CWD = folder_path;
}

void AbstractODESolver::useCompletePath(const bool flag){
    _use_complete_output_file = flag;
}

void AbstractODESolver::setStepSize(double h){
    if(h < 0 || h >=1){
        throw std::runtime_error("Invalid value for step size h. Must be between 0 and 1.");
    }
    _h = h;
}

void AbstractODESolver::setTimeInterval(double initial_t, double final_t){
    if(final_t <= initial_t){
        throw std::runtime_error("Invalid time interval.");
    }
    _final_time = final_t;
    _initial_time = initial_t;
}

void AbstractODESolver::setInitialState(const Vector &initial_state){
    _initial_state = new Vector(initial_state);
}

Vector AbstractODESolver::getInitialState(){
    Vector to_give(*_initial_state);
    return to_give; // return a copy, instead of the instance vector.
}

double AbstractODESolver::getStepSize(){
    return _h;
}

double AbstractODESolver::getInitialTime(){
    return _initial_time;
}

double AbstractODESolver::getFinalTime(){
    return _final_time;
}

void AbstractODESolver::solve(bool save, bool print){

    if (print) printHeader(); // Each stepper overwrites its own header.

    double h = getStepSize();

    if (save) openOutputFile(_output_file_name);

    int iteration = 1;

    Vector current_state = *_initial_state;
    Vector next_state(current_state);
    double current_t = getInitialTime();

    while(current_t < getFinalTime()){


        if( save && (iteration % _save_gap) == 0){
            writeData(current_t, current_state);
        }

        if( print && (iteration % _print_gap) == 0){
            printData(current_t, current_state);
        }
        std::cout << "  Solving for time step:" << current_t << std::endl;

        double next_t = current_t + h;

        // Each stepper overwites its own advance method.
        advance(current_t, current_state, next_state);

        current_t = next_t; // Take one step in time.
        current_state = next_state; // Take one step in the state.

        iteration++;

    }

    if (save) closeOutputFile();
}

/*
 * Function: solve
 * ----------------
 * Solves the ODE Problem.
 * Saves the solution at each time step on
 * the given "result" Matrix.
 * If save is true, it also Outputs the solution
 * at each time step on a file. In the same way,
 * if print is true, it prints the output at each
 * time step in the console window.

void AbstractODESolver::solve(Matrix& result, bool save, bool print){

    if (print) printHeader(); // Each stepper overwrites its own header.

    double h = getStepSize();

    if (save) openOutputFile(_output_file_name);

    int iteration = 1;

    Vector current_state = *_initial_state;
    Vector next_state(current_state);
    double current_t = getInitialTime();

    while(current_t <= getFinalTime()){

        // For each component in current_state,
        // save the component in the result Matrix.
        for (int i=0; i<current_state.GetSize(); i++){
            result(iteration,i+1) = current_state[i];
        }

        if( save && (iteration % _save_gap) == 0){
            writeData(current_t, current_state);
        }

        if( print && (iteration % _print_gap) == 0){
            printData(current_t, current_state);
        }

        double next_t = current_t + h;

        // Each stepper implements its own advance method.
        advance(current_t, current_state, next_state);

        current_t = next_t; // Take one step in time.
        current_state = next_state; // Take one step in the state.

        iteration++;

    }

    if (save) closeOutputFile();
}*/

/*double AbstractODESolver::computeError(){

    double h = getStepSize();

    Vector current_state = *_initial_state;
    Vector next_state(current_state);
    double current_t = getInitialTime();

    double n_components = current_state.GetSize();
    Vector true_sol(n_components);
    double max_norm = 0;

    while(current_t < getFinalTime()){

        double next_t = current_t + h;

        // Evaluate true solution function at the
        // next time step and store the result in true_sol vector.
        _ODEObject->ComputeAnalyticSolution(next_t, true_sol);

        // Each stepper overwites its own advance method.
        advance(current_t, current_state, next_state);

        Vector difference = next_state - true_sol;

        // Euclidian Norm
        double norm = difference.CalculateNorm(2);

        if (norm > max_norm) max_norm = norm;

        current_t = next_t; // Take one step in time.
        current_state = next_state; // Take one step in the state.

    }
    return max_norm;
}*/

void AbstractODESolver::openOutputFile(const std::string file_name){

    _output_file.setf(std::ios::scientific,std::ios::floatfield);
    _output_file.precision(7);

    std::string file_path;
    if(_use_complete_output_file){
        file_path = CWD + "/" + file_name;
    }else{
        file_path = file_name;
    }

    _output_file.open(file_path);

    if(!_output_file.is_open()){
        throw std::runtime_error("Error when opening the file to write the solution.");
    }
}

void AbstractODESolver::writeData(const double t, const Vector& us){
    _output_file << std::setw(15) << t;
    for (int i=0; i<us.GetSize(); i++){
        _output_file << std::setw(15) << us.Read(i);
    }
    _output_file << "\n"; // End of Line.
}

void AbstractODESolver::writeData(const double h, double e){
    _output_file << std::setw(15) << h;
    _output_file << std::setw(15) << e << std::endl;
}

void AbstractODESolver::printData(const double t, const Vector& us){
    std::cout << "For time= " << t;
    int components_to_print = std::min(3, us.GetSize());
    for(int i=0; i<components_to_print; i++){
        std::cout << ", u[" << i << "]= " << us.Read(i);
    }
    std::cout << "\n"; // End of Line.
}

void AbstractODESolver::closeOutputFile(){
    _output_file.close();
}





