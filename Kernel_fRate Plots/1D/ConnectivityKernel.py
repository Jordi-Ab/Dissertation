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
	ConnectivityKernel1 Object
	-------------------
	Inherits data from AbstractConnectivityKernel 
	"""
	def evaluateAt(self, x):
		"""
		Evaluate the Connectivity Kernel Function 
		at the given space grid vector x.
		"""
		return 0.5*np.exp(-self.b*abs(x))

class ConnectivityKernel2(AbstractConnectivityKernel):
	"""
	ConnectivityKernel2 Object
	-------------------
	Inherits data from AbstractConnectivityKernel 
	"""
	def evaluateAt(self, x):
		"""
		Evaluate the Connectivity Kernel Function 
		at the given space grid vector x.
		"""
		return np.exp( -self.b*abs(x) )*( self.b*np.sin(abs(x)) + np.cos(x) )

class laingKernel(AbstractConnectivityKernel):
	"""
	laing Kernel
	-------------------
	As in Carlo R. Laing paper, 1D Model 
	"""
	def evaluateAt(self, x):
		"""
		Evaluate the Connectivity Kernel Function 
		at the given space grid vector x.
		"""
		return 10*np.exp( -4*(x**2) ) - 6*np.exp( -(x**2) )

