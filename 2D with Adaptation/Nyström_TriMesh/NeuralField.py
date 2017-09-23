"""
NeuralField Object
--------------------
Neural Field model with linear spike frequency adaptation
as the one in the paper: "Spots: Breathing, Drifting and 
Scattering in a Neural Field Model" by Coombes, Schmidt
and Avitabile
"""

import numpy as np

class NeuralField:
    """
    Constructor
    ---------------------------------
    Receives:
        firing_rate -> callable object or callable function 
        synaptic_matrix -> Square matrix (Synaptic connectivity)
        alpha -> Adaptation constant
        g -> Strength of the negative feedback
    """
    def __init__(self, firing_rate, synaptic_matrix, alpha, g):
    	self.f_rate = firing_rate
    	self.W = synaptic_matrix
    	self.alpha = alpha
    	self.g = g

    def __call__(self, t, v):
        """
        operator ()
        --------------------
        Evaluate the discretized integral equation
        at the given time t and vector u.
        * Can be used directly with time steppers.
        """
        alpha = self.alpha; g = self.g
        N = int( len(v)/2 )
        u = v[:N]; a=v[N:] # Break v in u and a
        
        f_u = self.f_rate(u) # Evaluate firing rate at u
        v0 = alpha*( (self.W).dot(f_u) - u - g*a ) # Equate synaptic activity
        v1 = u - a # Equate adapative field

        result = np.concatenate([v0,v1]) # stack v0 on top of v1
        
        return result
