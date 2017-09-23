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

    void getGaussWeightsAndPoints(int n_points,
                                  std::vector<double> &ws,
                                  std::vector<double> &xs,
                                  std::vector<double> &ys);

    void printVector(std::vector<double>& elems);

    void saveGrid(std::string file_name,
                  std::vector<Vector> points_grid);

    void loadMeshGrid(std::string file_name,
                      std::vector<Vector> &v);

    void loadConnectivityMatrix(std::string file_name,
                                std::vector< std::vector<int> > &v);
};

#endif // HELPERS_HPP
