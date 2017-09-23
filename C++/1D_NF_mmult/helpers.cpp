#include "helpers.hpp"

Helpers::Helpers(){}

void Helpers::loadMeshGrid(std::string file_name,
                           std::vector<Vector> &v){

    std::ifstream read_file(file_name);
    if(!read_file.is_open()){
        std::cerr << "Couldn't open the file" << file_name << std::endl;
    }

    //Loop over lines in the file reading data.
    while(true){
        if(read_file.fail()) break;
        Vector point(2);
        read_file >> point[0] >> point[1];
        v.push_back(point);
    }
    v.pop_back();
}

void Helpers::loadConnectivityMatrix(std::string file_name,
                                     std::vector< std::vector<int> > &v){

    std::ifstream read_file(file_name);
    if(!read_file.is_open()){
        std::cerr << "Couldn't open the file" << file_name << std::endl;
    }

    //Loop over lines in the file reading data.
    while(true){
        if(read_file.fail()) break;
        std::vector<int> elem;
        int v1; int v2; int v3;
        read_file >> v1 >> v2 >> v3;
        elem.push_back(v1);
        elem.push_back(v2);
        elem.push_back(v3);
        v.push_back(elem);
    }
    //v.pop_back();
}


void Helpers::saveGrid(std::string file_name,
                       double* mesh, int Nx){
    // Format output
    std::ofstream output_file;
    output_file.setf(std::ios::scientific,std::ios::floatfield);
    output_file.precision(6);

    // Open file (and perform a check)
    output_file.open(file_name);
    if(!output_file.is_open()){
        std::cerr << "Couldn't open the file" << file_name << std::endl;
    }

    // Write data
    for (int i=0; i<Nx; i++){
        output_file << std::setw(15) << mesh[i];
        output_file << std::endl;
        // Next row.
    }

    output_file.close();
}

void Helpers::printVector(std::vector<double>& elems) {
    for (size_t i = 0; i < elems.size(); ++i){
        std::cout << elems[i] << ' ';
        std::cout << std:: endl;
    }
}

void Helpers::printV(double* v, int size) {

    std::cout << "[" << v[0];
    for (int i=1; i<size; i++){
        std::cout << ", "<<v[i];
    }
    std::cout << "]"<< std:: endl;
}

void Helpers::linspace(double first, double last, int n, double* mesh){
    double h = (last - first)/(n-1);
    mesh[0] = first;
    for(int i=1; i<n; i++){
        mesh[i] = mesh[i-1] + h;
    }
    mesh[n-1] = last;
}
