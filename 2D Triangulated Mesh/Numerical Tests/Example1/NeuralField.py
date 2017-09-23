import numpy as np

class NeuralField:
	"""
	NeuralField Object
	--------------------
	Discretized Amari type Neural Field 
	Integral equation, using a synaptic matrix
	assembled by the Nystrom Method.

	Receives:
		firing_rate -> object (as in FiringRate.py)
		synaptic_kernel -> object (as in Connectivity Kernel.py)
		mesh -> Mesh of interior points of each element
		n_elems -> Number of elements in the mesh
	"""
	def __init__(self, synaptic_matrix, firing_rate, ext_input):
		self.W = synaptic_matrix
		self.f_rate = firing_rate
		self.I = ext_input

	def evaluateAt(self, t, u, xs):
		"""
		Function: evaluateAt
		--------------------
		Evaluate the discretized integral equation
		at the given time t and vector u.
		""" 
		f_u = self.f_rate(u)
		I = np.zeros(len(xs))
		for i, x in enumerate(xs): 
			I[i] = self.I(t, x)
		return I - u + (self.W).dot(f_u)
