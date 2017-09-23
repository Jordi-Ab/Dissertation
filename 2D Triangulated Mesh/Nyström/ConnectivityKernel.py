"""
Various choices for Connectivity Kernels.
They are callable objects.
Example:
	kernel = ConnectivityKernel1(b=0.1)
	x=1; y=2
	result = kernel(x,y)
"""

import numpy as np

class AbstractConnectivityKernel:
	"""
	AbstractConnectivityKernel Object
	-------------------
	Encapsulates the Parameters of the
	Connectivity Kernel function for a Neural Field
	Integral equation of the Amari type.
	"""
	def __init__(self, b=1):
		# Parameter that controls the decay rate of
		# the exponential Connectivity Kernel.
		# b=1 by default (when no decay parameter).
		self.b = b

class ConnectivityKernel1(AbstractConnectivityKernel):
	"""
	ConnectivityKernel1 Object "Wizard Hat"
	-------------------
	Inherits data from AbstractConnectivityKernel 
	"""
	def __call__(self, x, y=0):
		"""
		operator ()
		----------------------------------------
		Evaluate the Connectivity Kernel Function 
		at the given x,y coordinates
		"""
		nrm = np.sqrt(x*x + y*y) # Euclidian norm

		return 0.5*np.exp(-self.b*nrm)

class ConnectivityKernel2(AbstractConnectivityKernel):
	"""
	ConnectivityKernel2 Object "Mexican Hat"
	-------------------
	Inherits data from AbstractConnectivityKernel 
	"""
	def __call__(self, x, y=0):
		"""
		operator ()
		----------------------------------------
		Evaluate the Connectivity Kernel Function 
		at the given x,y coordinates
		"""
		nrm = np.sqrt(x*x + y*y) # Euclidian norm
		return np.exp( -self.b*nrm )*( self.b*np.sin(nrm) + np.cos(nrm) )

