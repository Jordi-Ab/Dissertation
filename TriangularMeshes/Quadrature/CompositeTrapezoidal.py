import numpy as np

def computeIntegral(f, v1,v2,v3):
	"""
	Compute the integral of a function 
	on a triangular domain.

	f -> function to integrate
	v1,v2,v3 -> Vertices of the triangle.
	ex. v1 = (x1, y1) being a tuple.
	"""
	x1 = v1[0]; x2=v2[0]; x3 = v3[0];
	y1 = v1[1]; y2=v2[1]; y3 = v3[1];

	# Area of the triangle
	A=abs( x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2) )/2.0

	I = f(x1,y1) + f(x2, y2) + f(x3,y3)

	I = (1/3)*A*I

	return I
