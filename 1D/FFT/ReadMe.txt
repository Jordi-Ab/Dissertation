Text file with information about the files on this folder

MAIN FILES:
* 1dFFT_main.ipynb -> IPython Notebook. Requires Jupyter notebook for viewing and running. For installation: http://jupyter.org/
* 1dFFT_main.py -> Python script runnable from terminal. Requires Python >= 3.5. For installation: https://www.python.org/

DEPENDENCIES: Main Files require the following

CLASSES:
* ConnectivityKernel.py -> to define a callable connectivity kernel function (may not be included and defined by the user inside the main script)
* FiringRate.py -> to define a callable firing rate function (may not be included and defined by the user inside the main script)
* NeuralFieldFFT.py -> to evaluate the right hand side of a discretized neural field integral model.

PACKAGES:
* numpy
* scipy
* matplotlib