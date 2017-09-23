import numpy as np

class NeuralField:
    """
    NeuralField Object
    --------------------
    Discretized Amari type Neural Field 
    Integral equation, using a synaptic matrix
    assembled by the Nystrom Method.

    Receives:
        firing_rate -> object (as in FiringRate.py)
        synaptic_matrix -> Square matrix
    """
    def __init__(self, firing_rate, ext_input, synaptic_matrix, points_grid ):
        self.W = synaptic_matrix
        self.f_rate = firing_rate
        self.IExt = ext_input
        self.grid = points_grid

    def evaluateAt(self, t, u):
        """
        Function: evaluateAt
        --------------------
        Evaluate the discretized integral equation
        at the given time t and vector u.
        """
        f_u = self.f_rate(u)
        I = np.zeros(len(self.grid))
        for i, x in enumerate(self.grid): 
            I[i] = self.IExt(t, x)
        return I - u + (self.W).dot(f_u)