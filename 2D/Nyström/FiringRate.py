"""
Various choices for Firing Rate function.
They are callable objects.
Example:
	firing_rate = FiringRate1(mu=3.5, theta=5.6)
	random_dim = np.random.randint(1,50)
	u = np.zeros( random_dim )
	result = firing_rate(u)
"""

import numpy as np

class AbstractFiringRate:
	"""
	AbstractFiringRate Object
	-------------------
	Encapsulates the Parameters of the
	Firing Rate function for a Neural Field
	Integral equation of the Amari type.
	"""
	def __init__(self, slope, threshold):
		# slope of the sigmoid function
		self.mu = slope
		# Threshold Parameter.
		self.theta = threshold

class FiringRate1(AbstractFiringRate):
	"""
	FiringRate1 Object
	-------------------
	Inherits data from AbstractFiringRate 
	"""
	def __call__(self, u):
		"""
		operator ()
		--------------------------------------
		Evaluate the Firing Rate Function at the
		given vector u.
		"""
		m = self.mu; h = self.theta
		return 1 / (1 + np.exp(- m * (u - h) ))

class FiringRate2(AbstractFiringRate):
	"""
	FiringRate2 Object
	-------------------
	Inherits data from AbstractFiringRate 
	"""
	def __call__(self, u):
		"""
		operator ()
		--------------------------------------
		Evaluate the Firing Rate Function at the
		given vector u.
		"""
		m = self.mu; h = self.theta
		return 1/( 1 + np.exp(- m*u + h) ) - 1/( 1 + np.exp(h) )