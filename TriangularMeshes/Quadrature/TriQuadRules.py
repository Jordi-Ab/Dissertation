import numpy as np
from GaussWeightsPoints import getWeightsAndPoints

# Nodal Basis Functions for Mapping to a canonical reference triangle. 
N1 = lambda x_hat, y_hat: 1 - x_hat - y_hat
N2 = lambda x_hat, y_hat: x_hat
N3 = lambda x_hat, y_hat: y_hat

def gaussInt(f, N_point, v1,v2,v3):
	""" 
	Evaluates \iint_K f(x,y) dxdy
	using a Gaussian Quadrature of order N,
	where K is a triangle with vertices at
	(x1, y1), (x2, y2), (x3,y3)
	"""
	x1 = v1[0]; x2=v2[0]; x3 = v3[0];
	y1 = v1[1]; y2=v2[1]; y3 = v3[1];
	xw = getWeightsAndPoints(N_point) # Get quadrature points and weights.
	if N_point==1: xw = xw.T

	#Calculate the area of the Triangle.
	A=abs( x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2) )/2.0
	
	# number of Gauss points 
	np = xw[:,0].size;

	weights = xw[:,2]
	x_hat = xw[:,1]
	y_hat = xw[:,0]

	result = 0
	for i in range(np):
		x = x1*N1(x_hat[i], y_hat[i]) + x2*N2(x_hat[i], y_hat[i]) + x3*N3(x_hat[i], y_hat[i])
		y = y1*N1(x_hat[i], y_hat[i]) + y2*N2(x_hat[i], y_hat[i]) + y3*N3(x_hat[i], y_hat[i])
		result += f(x,y)*weights[i]

	result *= A

	return result

def trapezoidInt(f, v1,v2,v3):
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






