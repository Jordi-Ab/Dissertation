"""
NeuralField Object
--------------------
Discretized Amari type Neural Field Integral equation that
uses a synaptic matrix assembled by the Nystrom Method.
"""

import numpy as np

class NeuralField:
    """
    Constructor
    ---------------------------------
    Receives:
        firing_rate -> callable object or callable function 
        synaptic_matrix -> Square matrix (Synaptic connectivity)
    """
    def __init__(self, firing_rate, synaptic_matrix):
        self.W = synaptic_matrix
        self.f_rate = firing_rate

    def __call__(self, t, u):
        """
        operator ()
        --------------------
        Evaluate the discretized integral equation
        at the given time t and vector u.
        * Can be used directly with time steppers.
        """
        f_u = self.f_rate(u)
        return -u + (self.W).dot(f_u)