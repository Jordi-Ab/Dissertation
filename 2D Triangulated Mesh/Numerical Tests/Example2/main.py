import numpy as np
import numpy.linalg as la
from math import erf
from meshtools import *
import NeuralField as nf
import QuadratureInTriangles as Qtri
import matplotlib.pyplot as plt
from matplotlib.mlab import griddata
from scipy.integrate import ode

# Parameters
c_ct = 1
l_ct = 5
s_ct = 5

def b(x_vec):
    c1 = erf( np.sqrt(l_ct)*(1-x_vec[0]) )
    c2 = erf( np.sqrt(l_ct)*(1+x_vec[0]) )
    c3 = erf( np.sqrt(l_ct)*(1-x_vec[1]) )
    c4 = erf( np.sqrt(l_ct)*(1+x_vec[1]) )
    return ( np.pi/(4*l_ct) )*(c1+c2)*(c3+c4)

def I(t, x_vec):
    return c_ct + t -np.tanh(s_ct*t)*b(x_vec)

def kernel(x_vec, y_vec):
    return np.exp( -l_ct*( (x_vec[0] - y_vec[0])**2 ) - l_ct*( (x_vec[1] - y_vec[1])**2 ) )

def f_rate(x):
    return np.tanh(s_ct*x)

def true_sol(t, xs):
    tru = np.ones(len(xs))
    return t*tru

Np = 2 # Desired number of gauss points.

gwp = Qtri.getWeightsAndPoints(Np)

weights = gwp[:,2]
x_hat = gwp[:,1]
y_hat = gwp[:,0]

Ng = len(weights) # Actual Number of Gauss points.

errors = []
hs = []
# Do it for an increasing mesh size
for i in np.arange(2,6,0.5):

	length = 1/i

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

	h = (Ux - Lx)/(len(xs)-1)
	#hs.append(h)
	hs.append(length)

	# Assemble Synaptic Matrix
	n = xs.shape[0]
	W = np.zeros((n,n))
	for i in range(n):
	    for j in range(n):
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
	u0 = np.zeros(len(xs))

	method = ode(neural_field).set_integrator("dopri5")
	method.set_initial_value(u0)
	final_t = 1
	dt = 0.1
	while method.t < final_t:
		next_t = method.t+dt
		sol = method.integrate(next_t)

	err = la.norm( sol - true_sol(next_t, xs), np.inf )
	errors.append(err)

	print(""+str( int(NT) )+"&"+str(int(NT*Ng))+"&"+str(round(length,3))+"&"+str(err)+"\\\\")

data = np.array([hs, errors])
np.savetxt("Errors.csv", np.transpose(data))