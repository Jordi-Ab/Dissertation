
"""
NeuralField Object
--------------------
Neural Field model with linear spike frequency adaptation,
as the one in the paper: "Spots: Breathing, Drifting and 
Scattering in a Neural Field Model" by Coombes, Schmidt
and Avitabile.

Uses FFTs to compute the right hand side
"""
from scipy.fftpack import fft2, ifft2, ifftshift
import numpy as np

class NeuralFieldFFT:
    """
    Constructor
    ---------------------------------
    Receives:
        firing_rate -> callable object or callable function 
        synaptic_matrix_fft -> fft of the Synaptic Connectivity Matrix
        Ux -> Upper limit of the x-axis
        nx -> Number of points used to discretize the x-axis
        alpha -> Adaptation constant
        g -> Strength of the negative feedback
    """
    def __init__(self, firing_rate, synaptic_matrix_fft, Ux, nx, alpha, g):
        self.f = firing_rate
        self.w_hat = synaptic_matrix_fft
        self.Ux = Ux
        self.nx = nx
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

        # Rename for convenience
        alpha = self.alpha; g = self.g;
        
        N = (self.nx)**2;
        u = v[:N]; a=v[N:] # split vector v

        S = self._convolution(u)
        v0 = alpha*( S - u - g*a ) # Compute synaptic activity u
        v1 = u - a # Compute adaptivity a
        
        result = np.concatenate([v0,v1]) # stack v0 on top of v1
        return result
    
    def _convolution(self, u):
        """
        Function: _convolution
        --------------------
        Compute the convolution integral using
        FFTs
        """
        # Rename for convenience
        f_rate = self.f; w_hat = self.w_hat;
        Ux = self.Ux; nx = self.nx;
        
        u = u.reshape((nx,nx)) # To Matrix

        # FFT of firing rate at u
        f_u = f_rate(u)
        f_hat = fft2(f_u) # 2D fft of matrix

        p_prod = np.real( ifft2(f_hat*w_hat) ) # Pointwise product of matrices
        shift = ((2*Ux/nx)**2)*ifftshift(p_prod) # Shift result
        
        return shift.flatten() # return shift as a vector
        
        
