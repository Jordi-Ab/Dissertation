from scipy.fftpack import fft2, ifft2, ifftshift
import numpy as np

class NeuralFieldFFT:
    """
    NeuralField Object
    --------------------
    Discretized Amari type Neural Field 
    Integral equation, using Fast Fourier
    Tranforms for the Discretization.

    Receives:
	    firing_rate -> callable function
	    synaptic_kernel_fft -> Fast Fourier Tranform of
	    	the Synaptic Connectivity function evaluated
	    	at the space grid. (matrix)
	    Ux -> Last point in the space grid [Lx, Ux]
	    nx -> Number of points in the space grid. 
    """
    def __init__(self, firing_rate, synaptic_kernel_fft, Ux, nx):
        self.f = firing_rate
        self.w_hat = synaptic_kernel_fft
        self.Ux = Ux
        self.nx = nx

    def __call__(self, t, u):
        """
        operator ()
        --------------------
        Evaluate the discretized integral equation
        at the given time t and vector u.
        """
        
        # Rename to skip the self.
        f_rate = self.f; w_hat = self.w_hat;
        Ux = self.Ux; nx = self.nx;

        _u = u.reshape((nx,nx)) # To Matrix

        # FFT of firing rate at u
        f_u = f_rate(_u)
        f_hat = fft2(f_u) # 2D fft of matrix

        p_prod = np.real( ifft2(f_hat*w_hat) ) # Pointwise product of matrices
        shift = ((2*Ux/nx)**2)*ifftshift(p_prod) # Shift result
        F = - _u + shift
        return F.flatten()
