import numpy as np
import numpy.linalg as la
from math import erf
from meshtools import *
import NeuralField as nf
import QuadratureInTriangles as Qtri
import matplotlib.pyplot as plt
from matplotlib.mlab import griddata
from scipy.integrate import ode

def b(x_vec):
    c1 = erf(1-x_vec[0])
    c2 = erf(1+x_vec[0])
    c3 = erf(1-x_vec[1])
    c4 = erf(1+x_vec[1])
    return (np.pi/4)*(c1+c2)*(c3+c4)

def I(t, x_vec):
    return -np.tanh( np.exp(-t) )*b(x_vec)

def kernel(x_vec, y_vec):
    return np.exp( -( x_vec[0] - y_vec[0] )**2 - ( x_vec[1] - y_vec[1] )**2 )

def f_rate(x):
    return np.tanh(x)

def true_sol(t, xs):
    tru = np.ones(len(xs))
    return np.exp(-t)*tru

Np = 2 # Desired number of gauss points.

gwp = Qtri.getWeightsAndPoints(Np)

weights = gwp[:,2]
x_hat = gwp[:,1]
y_hat = gwp[:,0]

Ng = len(weights) # Actual Number of Gauss points.

errors = []
length_size = []
# Do it for an increasing mesh size
for i in np.arange(2,7,0.5):

	length = 1/i
	length_size.append(length)

	# Generate Mesh
	Lx=-1; Ux=1
	Ly=-1; Uy=1
	p,v=RectangleSegments([Ux,Uy],[Lx, Ly],edge_length=length)
	mesh_pts, elems = DoTriMesh(p,v,edge_length=length)
	NT = len(elems) # Number of triangles

	# Assemble Mesh of Interior Points
	xs = []
	As = []
	for l, elem in enumerate(elems):
	    v1,v2,v3 = mesh_pts[elem] # Get vertices of the element
	    A_l = Qtri.computeArea(v1,v2,v3)
	    As.append(A_l)
	    for j in range(len(weights)):
	        new_point = Qtri.mapX(v1, v2, v3, x_hat[j], y_hat[j])
	        xs.append(new_point)
	xs = np.array(xs)
	As = np.array(As)
	N = len(xs)

	# Assemble Synaptic Matrix
	W = np.zeros((N,N))
	for i in range(N):
	    for j in range(N):
	        l = int(np.floor(j/Ng)) # Element At
	        A = As[l]
	        r = j - l*Ng # Interior point of element at
	        rho = weights[r]
	        w = kernel(xs[i,:], xs[j,:])
	        W[i,j] = w*A*rho

    # Initialize Neural Field
	NeuralField = nf.NeuralField(W, f_rate, I)
	neural_field = lambda t,u: NeuralField.evaluateAt(t,u,xs) # Callable function

	# Initial Condition
	u0 = np.ones(N)

	# Time step with RK4
	method = ode(neural_field).set_integrator("dopri5")
	method.set_initial_value(u0)
	final_t = 1
	dt = 0.1
	while method.t < final_t:
	    next_t = method.t+dt
	    sol = method.integrate(next_t)

	err = np.linalg.norm( sol - true_sol(next_t, xs), np.inf )
	print(""+str( int(NT) )+"&"+str(int(NT*Ng))+"&"+str(round(length,3))+"&"+str(err)+"\\\\")
	errors.append(err)
    
data = np.array([length_size, errors])
np.savetxt("Errors.csv", np.transpose(data))



