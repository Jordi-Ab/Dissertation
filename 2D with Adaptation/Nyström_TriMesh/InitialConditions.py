"""
Various choices of Initial Conditions for time stepping.
See: CONTINUATION OF LOCALISED COHERENT STRUCTURES IN NONLOCAL NEURAL FIELD EQUATIONS, JAMES RANKIN and DANIELE AVITABILE. Appendix A, page 19.
"""
import numpy as np

class InitialCondition1():

	def __init__(self, A, L):
		"""
		Constructor
		--------------------
		Receives:
			A -> Amplitud
			L -> Length or "kurtosis"
		"""
		self._A = A
		self._L = L
		self.num = 1

	def __call__(self, x,y):
		"""
		operator ()
		---------------------------------
		Evaluate the initial condition function at
		the given point with x,y coordinates
		"""
		e = np.exp(-(x**2 + y**2)/self._L)
		return self._A*e

class InitialCondition2():

	def __init__(self, A, L):
		"""
		Constructor
		--------------------
		Receives:
			A -> Amplitud
			L -> Length or "kurtosis"
		"""
		self._A = A
		self._L = L
		self.num = 2

	def __call__(self, x,y):
		"""
		operator ()
		---------------------------------
		Evaluate the initial condition function at
		the given point with x,y coordinates
		"""
		e = np.exp(-(x**2 + y**2)/self._L)
		cos1 = np.cos(x)
		cos2 = np.cos( 0.5*x + (np.sqrt(3)/2)*y )
		cos3 = np.cos( -0.5*x + (np.sqrt(3)/2)*y )
		return self._A*e*(cos1 + cos2 + cos3)

class InitialCondition3():

	def __init__(self, A, L):
		"""
		Constructor
		--------------------
		Receives:
			A -> Amplitud
			L -> Length or "kurtosis"
		"""
		self._A = A
		self._L = L
		self.num = 3

	def __call__(self, x,y):
		"""
		operator ()
		---------------------------------
		Evaluate the initial condition function at
		the given point with x,y coordinates
		"""
		e = np.exp(-(x**2 + y**2)/self._L)
		return self._A*e*( -np.cos(x) - np.sin(y) )

class InitialCondition4():

	def __init__(self, A, L):
		"""
		Constructor
		--------------------
		Receives:
			A -> Amplitud
			L -> Length or "kurtosis"
		"""
		self._A = A
		self._L = L
		self.num = 4
		
	def __call__(self, x,y):
		"""
		operator ()
		---------------------------------
		Evaluate the initial condition function at
		the given point with x,y coordinates
		"""
		nrm = np.sqrt(x*x + y*y)
		return self._A/( np.cosh(self._L*nrm)**2 )