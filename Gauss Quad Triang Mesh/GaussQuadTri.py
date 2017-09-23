import numpy as np
from GaussWeightsPoints import getWeightsAndPoints
from meshtools import *
import matplotlib.pyplot as pt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as pt

# Nodal Basis Functions for Mapping to a canonical reference triangle. 
N1 = lambda x_hat, y_hat: 1 - x_hat - y_hat
N2 = lambda x_hat, y_hat: x_hat
N3 = lambda x_hat, y_hat: y_hat

# Function that maps any point in the element K using its vertices and
# the coordinates of that point inside a reference triangle
def mapX(v1, v2, v3, x_hat, y_hat):
    """
    v1, v2, v3 are lists containing x and y
    i.e. v1 = [x1, y1],
    and represent the vertices of a triangular element.
    x_hat is the x value of a point inside the refernce triangle
    y_hat is the y value of a point inside the reference triangle
    """
    # Map gauss points inside the triangle using the Nodal Basis Functions
    x = v1[0]*N1(x_hat, y_hat) + v2[0]*N2(x_hat, y_hat) + v3[0]*N3(x_hat, y_hat)
    y = v1[1]*N1(x_hat, y_hat) + v2[1]*N2(x_hat, y_hat) + v3[1]*N3(x_hat, y_hat)
    return np.array([x, y])

def computeArea(v1, v2, v3):
	x1, y1 = v1; x2, y2 = v2; x3, y3 = v3;
	A = abs( x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2) )/2.0
	return A

def gaussIntTriangle(f, N_point, v1, v2, v3):
	""" 
	Evaluates \int \int_K f(x,y) dxdy
	using a Gaussian Quadrature of order N,
	where K is a triangle with vertices at
	v1,v2,v3. 
	Each vertex v is a 2D array containing
	its x and y coordinates. i.e.
	v = [x, y]
	"""
	xw = getWeightsAndPoints(N_point) # Get quadrature points and weights.

	#Calculate the area of the Triangle.
	A = computeArea(v1,v2,v3)

	# Weights and points on the reference triangle
	x_hat = xw[:,0]
	y_hat = xw[:,1]
	weights = xw[:,2]

	# number of Gauss points
	np = len(weights)

	result = 0
	for i in range(np):
		# Map interior points to the element.
		x, y = mapX(v1,v2,v3, x_hat[i], y_hat[i])
		result += f(x,y)*weights[i]

	result *= A

	return result

def main():

	# Create Triangulate mesh
	edge_length = 0.3
	p, v = RectangleSegments([2,2],[-2,-2], edge_length=edge_length)
	mesh_pts, elems = DoTriMesh(p, v, edge_length)

	#Plot triangulated mesh for visualization
	pt.triplot(mesh_pts[:, 0], mesh_pts[:, 1], elems)
	pt.xlabel('x'); pt.ylabel('y')
	pt.title(r"$\Omega$")
	pt.savefig("tri_mesh.png")

	# Function to integrate over 
	def f(x, y):
	    return x**2 + y**2

    # Plot Function on the T mesh:
	x = mesh_pts[:,0]
	y = mesh_pts[:,1]
	z = f(x,y)

	fig = pt.figure(figsize=plt.figaspect(0.5))
	ax = fig.add_subplot(1, 1, 1, projection='3d')
	ax.plot_trisurf(x, y, z, triangles=elems, cmap=pt.cm.Spectral)
	ax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel(r'$f (x,y)$');
	pt.savefig("f_tri_mesh.png")

	N = 2 # Point rule of the Quadrature
	S = 0
	# Iterate through each element
	for i, elem in enumerate(elems):
	    # Get vertices of the element
	    v1,v2,v3 = mesh_pts[elem]
	    # Compute the integral of each element.
	    S += gaussIntTriangle(f, N, v1, v2, v3)

	print("Result: " +str(S))
	print("Error: " + str(S - 128/3))

if __name__ == "__main__": main()






