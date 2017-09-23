from math import *
import numpy as np
from scipy.integrate import ode
from getWeightsPoints import getWeightsAndPoints
import NeuralField as nf

def b(x_vec):
    c1 = erf(1-x_vec[0])
    c2 = erf(1+x_vec[0])
    c3 = erf(1-x_vec[1])
    c4 = erf(1+x_vec[1])
    return (np.pi/4)*(c1+c2)*(c3+c4)

def IExt(t, x_vec):
    return -np.tanh( np.exp(-t) )*b(x_vec)

def kernel(x_vec, y_vec):
    return np.exp( -( x_vec[0] - y_vec[0] )**2 - ( x_vec[1] - y_vec[1] )**2 )

def f_rate(x):
    return np.tanh(x)

def true_sol(t, xs):
    tru = np.ones(len(xs))
    return np.exp(-t)*tru

Np = 4 # Desired number of gauss points.
wgts, pts = getWeightsAndPoints(Np)
Ng = len(wgts) # Actual Number of Gauss points.
  

errors = []
hs = []
for i in np.arange(2,7):

	# Spatial Grid
	Nx = i # Number of points in the x space grid
	Lx = -1; Ux = 1 # x-space grid limits  
	#xi = np.linspace(Lx, Ux-hx, Nx) # nx equally spaced points between -Lx and Lx-hx
	xi = np.linspace(Lx, Ux, Nx) # nx equally spaced points between -Lx and Lx-hx
	hx = xi[1] - xi[0]
	hs.append(hx)

	# Assemble a Grid of Points as required by the integral i.e. (x_{is}, x_{jt})
	grid = []
	for i in range(Nx-1):
	    x = xi[i]
	    for j in range(Nx-1):
	        y = xi[j]
	        for s in range(Ng):
	            int_x = x + (hx/2)*(1+pts[s])
	            for t in range(Ng):
	                int_y = y + (hx/2)*(1+pts[t])
	                new_pt = np.array([int_x, int_y])
	                grid.append(new_pt)

	N = len(grid)
	#h = (grid[-1][0] - grid[0][0])/(N-1)
	#hs.append(h)
	                
	# Assemble Synaptic Matrix
	wgts_h = (hx/2)*wgts
	W = np.zeros( (len(grid), len(grid)) )
	for i, x_pt in enumerate(grid):
	    for j, y_pt in enumerate(grid):
	        s_ix = int(np.floor(j/Ng)) % Ng
	        rho_s = wgts_h[s_ix]
	        t_ix = j % Ng
	        rho_t = wgts_h[t_ix]
	        W[i,j] = rho_s*rho_t*kernel(x_pt,y_pt)
	        
	# Initialize Neural Field
	NeuralField = nf.NeuralField(f_rate, IExt, W, grid)
	neural_field = lambda t,u: NeuralField.evaluateAt(t,u) # Callable function

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

	err = np.linalg.norm( sol - true_sol(next_t, grid), np.inf )
	print(""+str( int(Nx) )+"&"+str(int(N))+"&"+str(round(hx,3))+"&"+str(err)+"\\\\")
	errors.append(err)
    
data = np.array([hs, errors])
np.savetxt("Errors.csv", np.transpose(data))
    
    
    