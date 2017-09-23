import numpy as np
from scipy.fftpack import fft, ifft, ifftshift

class NeuralFieldFFT:
	"""
	NeuralField Object
	--------------------
	Discretized Amari type Neural Field 
	Integral equation, using Fast Fourier
	Tranforms for the Discretization.

	Receives:
		firing_rate -> object (as in FiringRate.py)
		synaptic_kernel_fft -> Fast Fourier Tranform of
			the Synaptic Connectivity function evaluated
			at the space grid.
		Lx -> Last point in the space grid [-Lx, Lx]
		nx -> Number of points in the space grid. 
		heterogeneous_vector -> (optional) heterogeneous function
				A(y) evaliuated at the space grid.
	"""
	def __init__(self, firing_rate, synaptic_kernel_fft, Lx, nx, heterogeneous_vector=None):
		self.f = firing_rate
		self.A = heterogeneous_vector
		self.w_hat = synaptic_kernel_fft
		self.Lx = Lx
		self.nx = nx

	def __call__(self, t, u):
		"""
		operator ()
		--------------------
		Evaluate the discretized integral equation
		at the given time t and vector u.
		"""

		# Rename to skip the .self
		f_rate = self.f; A = self.A; w_hat = self.w_hat;
		Lx = self.Lx; nx = self.nx;

		f = f_rate(u)
		if (A != None): f *= A
		f_hat = fft(f)

		# Right-hand side
		F = -u + (2*Lx/nx)*ifftshift( np.real(ifft(f_hat*w_hat)) )
		return F
		