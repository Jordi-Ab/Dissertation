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
                       std::vector<Vector> points_grid){
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
    int size = points_grid.size();
    for (int i=0; i<size; i++){
        Vector point = points_grid[i];
        // Save x component in column1
        output_file << std::setw(15) << point[0];
        // Save y component in column2
        output_file << std::setw(15) << point[1] << std::endl;
        // Next row.
    }

}

void Helpers::printVector(std::vector<double>& elems) {
    for (size_t i = 0; i < elems.size(); ++i){
        std::cout << elems[i] << ' ';
        std::cout << std:: endl;
    }
}

void Helpers::getGaussWeightsAndPoints(int n_points, std::vector<double> &ws,
                         std::vector<double> &xs, std::vector<double> &ys){
    if (n_points==1){
        ys.push_back(1/3.0); xs.push_back(1/3.0); ws.push_back(1);
    }else if (n_points==2){
        ys.push_back(1/6.0); xs.push_back(1/6.0); ws.push_back(1/3.0);
        ys.push_back(1/6.0); xs.push_back(2/3.0); ws.push_back(1/3.0);
        ys.push_back(2/3.0); xs.push_back(1/6.0); ws.push_back(1/3.0);
    }else if (n_points==3){
        ys.push_back(1/3.0); xs.push_back(1/3.0); ws.push_back(-27/48.0);
        ys.push_back(3/5.0); xs.push_back(1/5.0); ws.push_back(25/48.0);
        ys.push_back(1/5.0); xs.push_back(1/5.0); ws.push_back(25/48.0);
        ys.push_back(1/5.0); xs.push_back(3/5.0); ws.push_back(25/48.0);
    }else if (n_points==4){
        ys.push_back(0.44594849091597); xs.push_back(0.44594849091597); ws.push_back(0.22338158967801);
        ys.push_back(0.44594849091597); xs.push_back(0.10810301816807); ws.push_back(0.22338158967801);
        ys.push_back(0.10810301816807); xs.push_back(0.44594849091597); ws.push_back(0.22338158967801);
        ys.push_back(0.09157621350977); xs.push_back(0.09157621350977); ws.push_back(0.10995174365532);
        ys.push_back(0.09157621350977); xs.push_back(0.81684757298046); ws.push_back(0.10995174365532);
        ys.push_back(0.81684757298046); xs.push_back(0.09157621350977); ws.push_back(0.10995174365532);
    }else if (n_points==5){
        ys.push_back(0.33333333333333); xs.push_back(0.33333333333333); ws.push_back(0.22500000000000);
        ys.push_back(0.47014206410511); xs.push_back(0.47014206410511); ws.push_back(0.13239415278851);
        ys.push_back(0.47014206410511); xs.push_back(0.05971587178977); ws.push_back(0.13239415278851);
        ys.push_back(0.05971587178977); xs.push_back(0.47014206410511); ws.push_back(0.13239415278851);
        ys.push_back(0.10128650732346); xs.push_back(0.10128650732346); ws.push_back(0.12593918054483);
        ys.push_back(0.10128650732346); xs.push_back(0.79742698535309); ws.push_back(0.12593918054483);
        ys.push_back(0.79742698535309); xs.push_back(0.10128650732346); ws.push_back(0.12593918054483);
    }else if (n_points==6){
        ys.push_back(0.24928674517091); xs.push_back(0.24928674517091); ws.push_back(0.11678627572638);
        ys.push_back(0.24928674517091); xs.push_back(0.50142650965818); ws.push_back(0.11678627572638);
        ys.push_back(0.50142650965818); xs.push_back(0.24928674517091); ws.push_back(0.11678627572638);
        ys.push_back(0.06308901449150); xs.push_back(0.06308901449150); ws.push_back(0.05084490637021);
        ys.push_back(0.06308901449150); xs.push_back(0.87382197101700); ws.push_back(0.05084490637021);
        ys.push_back(0.87382197101700); xs.push_back(0.06308901449150); ws.push_back(0.05084490637021);
        ys.push_back(0.31035245103378); xs.push_back(0.63650249912140); ws.push_back(0.08285107561837);
        ys.push_back(0.63650249912140); xs.push_back(0.05314504984482); ws.push_back(0.08285107561837);
        ys.push_back(0.05314504984482); xs.push_back(0.31035245103378); ws.push_back(0.08285107561837);
        ys.push_back(0.63650249912140); xs.push_back(0.31035245103378); ws.push_back(0.08285107561837);
        ys.push_back(0.31035245103378); xs.push_back(0.05314504984482); ws.push_back(0.08285107561837);
        ys.push_back(0.05314504984482); xs.push_back(0.63650249912140); ws.push_back(0.08285107561837);
    }else if (n_points==7){
        ys.push_back(0.33333333333333); xs.push_back(0.33333333333333); ws.push_back(-0.14957004446768);
        ys.push_back(0.26034596607904); xs.push_back(0.26034596607904); ws.push_back(0.17561525743321);
        ys.push_back(0.26034596607904); xs.push_back(0.47930806784192); ws.push_back(0.17561525743321);
        ys.push_back(0.47930806784192); xs.push_back(0.26034596607904); ws.push_back(0.17561525743321);
        ys.push_back(0.06513010290222); xs.push_back(0.06513010290222); ws.push_back(0.05334723560884);
        ys.push_back(0.06513010290222); xs.push_back(0.86973979419557); ws.push_back(0.05334723560884);
        ys.push_back(0.86973979419557); xs.push_back(0.06513010290222); ws.push_back(0.05334723560884);
        ys.push_back(0.31286549600487); xs.push_back(0.63844418856981); ws.push_back(0.07711376089026);
        ys.push_back(0.63844418856981); xs.push_back(0.04869031542532); ws.push_back(0.07711376089026);
        ys.push_back(0.04869031542532); xs.push_back(0.31286549600487); ws.push_back(0.07711376089026);
        ys.push_back(0.63844418856981); xs.push_back(0.31286549600487); ws.push_back(0.07711376089026);
        ys.push_back(0.31286549600487); xs.push_back(0.04869031542532); ws.push_back(0.07711376089026);
        ys.push_back(0.04869031542532); xs.push_back(0.63844418856981); ws.push_back(0.07711376089026);
    }else if (n_points==8){
        ys.push_back(0.33333333333333); xs.push_back(0.33333333333333); ws.push_back(0.14431560767779);
        ys.push_back(0.45929258829272); xs.push_back(0.45929258829272); ws.push_back(0.09509163426728);
        ys.push_back(0.45929258829272); xs.push_back(0.08141482341455); ws.push_back(0.09509163426728);
        ys.push_back(0.08141482341455); xs.push_back(0.45929258829272); ws.push_back(0.09509163426728);
        ys.push_back(0.17056930775176); xs.push_back(0.17056930775176); ws.push_back(0.10321737053472);
        ys.push_back(0.17056930775176); xs.push_back(0.65886138449648); ws.push_back(0.10321737053472);
        ys.push_back(0.65886138449648); xs.push_back(0.17056930775176); ws.push_back(0.10321737053472);
        ys.push_back(0.05054722831703); xs.push_back(0.05054722831703); ws.push_back(0.03245849762320);
        ys.push_back(0.05054722831703); xs.push_back(0.89890554336594); ws.push_back(0.03245849762320);
        ys.push_back(0.89890554336594); xs.push_back(0.05054722831703); ws.push_back(0.03245849762320);
        ys.push_back(0.26311282963464); xs.push_back(0.72849239295540); ws.push_back(0.02723031417443);
        ys.push_back(0.72849239295540); xs.push_back(0.00839477740996); ws.push_back(0.02723031417443);
        ys.push_back(0.00839477740996); xs.push_back(0.26311282963464); ws.push_back(0.02723031417443);
        ys.push_back(0.72849239295540); xs.push_back(0.26311282963464); ws.push_back(0.02723031417443);
        ys.push_back(0.26311282963464); xs.push_back(0.00839477740996); ws.push_back(0.02723031417443);
        ys.push_back(0.00839477740996); xs.push_back(0.72849239295540); ws.push_back(0.02723031417443);
    }else{
        std::cout << "No weights for that value of n" << std::endl;
    }
}
