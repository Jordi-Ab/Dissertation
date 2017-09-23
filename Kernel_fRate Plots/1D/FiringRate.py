import numpy as np

class AbstractFiringRate:
	"""
	AbstractFiringRate Object
	-------------------
	Encapsulates the Parameters of the
	Firing Rate function for a Neural Field
	Integral equation of the Amari type.
	"""
	def __init__(self, decay, threshold):
		# Decay rate parameter.
		self.miu = decay
		# Threshold Parameter.
		self.theta = threshold

class FiringRate1(AbstractFiringRate):
	"""
	FiringRate1 Object
	-------------------
	Inherits data from AbstractFiringRate 
	"""
	def evaluateAt(self, u):
		"""
		Evaluate the Firing Rate Function at the
		given vector u.
		"""
		m = self.miu; h = self.theta
		return 1 / (1 + np.exp(- m * (u - h) ))

class FiringRate2(AbstractFiringRate):
	"""
	FiringRate2 Object
	-------------------
	Inherits data from AbstractFiringRate 
	"""
	def evaluateAt(self, u):
		"""
		Evaluate the Firing Rate Function at the
		given vector u.
		"""
		m = self.miu; h = self.theta
		return 1/( 1 + np.exp(- m*u + h) ) - 1/( 1 + np.exp(h) )

class laingFiringRate(AbstractFiringRate):
	"""
	laingFiringRate Object
	-------------------
	Firing Rate function as in Carlo R.Laing paper
	1D Model
	"""
	def evaluateAt(self, u):
		"""
		Evaluate the Firing Rate Function at the
		given vector u.
		"""
		m = self.miu; h = self.theta
		return 1/( 1 + np.exp(- m*u + h) ) - 1/( 1 + np.exp(h) )