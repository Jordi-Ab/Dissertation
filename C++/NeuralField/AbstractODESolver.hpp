#ifndef ABSTRACTODESOLVER_HPP
#define ABSTRACTODESOLVER_HPP

#include <stdexcept>
#include <string>
#include <fstream>
#include <iomanip>
#include "ODEInterface.hpp"
class AbstractODESolver{

public:

    // Destructor
    ~AbstractODESolver();

    // Sets the step size of the ODE problem to the given number.
    void setStepSize(double h);

    // Sets the initial time and final time of the ODE problem
    void setTimeInterval(double initial_t, double final_t);

    // Sets the initial state vector.
    void setInitialState(const Vector& initial_state);

    // Returns the current step size.
    double getStepSize();

    // Returns the initial time.
    double getInitialTime();

    // Returns the final time.
    double getFinalTime();

    // Returns a shallow copy of the initial state vector.
    Vector getInitialState();

    // Changes the Path of the Output folder where the solution file will be saved.
    void setOutputFolder(const std::string folder_path);

    // Falgs if a specific path should be used to save the outputs.
    void useCompletePath(const bool flag);

    // Opens the "output file" instance variable, with the given name.
    void openOutputFile(const std::string file_name);

    // Closes the "output file" instance variable.
    void closeOutputFile();

    /* Writes Data on the "output file" instance variable.
     * Row-wise, per time unit, and column wise for Vector components,
     * i.e.
     *   t   component1  component2  ...     component_n
     *   -----------------------------------------------
     *   0   us[0]       us[1]       ...     us[n]
     */
    void writeData(const double t, const Vector& us);

    /*
     * Used to write the errors on a file.
     * Writes Data on the "output file" instance variable,
     * row-wise, per time unit, and column wise for the error value.
     * i.e.
     *   t   error
     *   ---------
     *   0   e0
     */
    void writeData(const double h, double e);

    /*
     * Function: solve
     * ----------------
     * Solves the ODE Problem.
     * Outputs the solution at each time step on a file.
     */
    void solve(bool save, bool print);

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
     */
    //void solve(Matrix& result, bool save=true, bool print=true);


    //double computeError();

protected:

    // Pointer to the ODE Object in consideration.
    ODEInterface* _ODEObject;

    // Name of the file where the approximate solution at each time step
    // will be written.
    std::string _output_file_name;

    /*
     * Time step gap at which you want to save the data.
     * Ex:
     *
     * Gap of one will save the data at every time step.
     * Gap of two will save the data at every two time steps.
     * and so on.
    */
    int _save_gap;

    /*
     * Time step gap at which you want to print the data.
     * Ex:
     *
     * Gap of one will print the data at every time step.
     * Gap of two will print the data at every two time steps.
     * and so on
    */
    int _print_gap;

    // Prints a header before printing the result on the Console Window
    // Will be overwritten depending on the method used.
    virtual void printHeader() = 0;

    // Advance one step in time (changes depending on method used)
    virtual void advance(const double current_t,
                         const Vector& current_state,
                         Vector& result) = 0;

private:

    // Variables for initial and final time
    double _final_time;
    double _initial_time;

    // Variable for the Step Size
    double _h;

    // Variable for Initial State
    Vector* _initial_state;

    // An OutputStream variable to write the soultion on a file.
    std::ofstream _output_file;

    // Current working Directory for saving the output files:
    // Set to the home directory by default
    std::string CWD = "";

    // The above path works only in my computer,
    // so when running on another computer this should be set to false.
    bool _use_complete_output_file = false; // false by default

    /*
     * Prints the given Vector of state "us" at the given time,
     * on the Console Window.
     * Vector of states "us" will have as many components as equations
     * there are on the system.
     * The method will just print a maximum of 3 components to
     * avoid console window cluttering for large systems.
    */
    void printData(const double t, const Vector& us);

};

#endif // ABSTRACTODESOLVER_HPP
