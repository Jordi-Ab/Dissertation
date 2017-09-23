#ifndef HELPERS_HPP
#define HELPERS_HPP

#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
#include "Vector.hpp"

class Helpers{
public:

    Helpers();

    void linspace(double first, double last, int n, double* mesh);

    void printVector(std::vector<double>& elems);

    void printV(double* v, int size);

    void saveGrid(std::string file_name,
                  double* mesh, int Nx);

    void loadMeshGrid(std::string file_name,
                      std::vector<Vector> &v);

    void loadConnectivityMatrix(std::string file_name,
                                std::vector< std::vector<int> > &v);
};

#endif // HELPERS_HPP
