Text file with information about the files on this folder

MAIN FILES:
* 2dNyst_main.ipynb -> IPython Notebook. Requires Jupyter notebook for viewing and running. For installation: http://jupyter.org/
* 2dNyst_main.py -> Python script runnable from terminal. Requires Python >= 3.5 For installation: https://www.python.org/

DEPENDENCIES: Main Files require the following

CLASSES:
* Connectivity Kernel.py -> to define a callable connectivity kernel function (may not be included and defined by the user inside the main script)
* Firing Rate.py -> to define a callable firing rate function (may not be included and defined by the user inside the main script)
* Initial Conditions.py -> to define a callable initial condition function (may not be included and defined by the user inside the main script)
* Neural Field.py -> to evaluate the right hand side of a discretized neural field integral model.

HELPERS:
* getWeightsPonts.py -> Weights and Points for Gaussian Quadrature 
on the interval [-1,1].

PACKAGES:
* numpy
* scipy
* matplotlib