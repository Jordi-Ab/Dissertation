
# coding: utf-8

from math import *
import numpy as np
from scipy.integrate import ode
import matplotlib.pyplot as pt
import warnings
import FiringRate as fr
import ConnectivityKernel as ck
import NeuralField as nf

warnings.simplefilter("ignore")


# Spatial Grid
nx = (2**10)-1 # Number of points in the space grid
Lx = 30 # Space grid limits
hx = 2*Lx/nx # Space width between points in the grid 
x = np.linspace(-Lx, Lx-hx, nx) # nx equally spaced points between -Lx and Lx-hx


# Initialize Connectivity Kernel Object
b = 0.4
kernel = ck.ConnectivityKernel2(b)


# Plot the Chosen Connectivity Kernel
plot_kernel = True
if(plot_kernel):
    fig1 = pt.figure()

    ax1 = fig1.add_subplot(111)
    ax1.plot(x, kernel(x))
    ax1.set_title('Connectivity Kernel')
    ax1.set_xlabel('x')
    ax1.set_ylabel('w(x)')

# Quadrature weights for Composite trapezoidal
rho = np.ones(x.size)
rho = rho*hx

# Assemble the Synaptic Matrix W
W = np.zeros((nx, nx))
for i in range(nx):
    for j in range(nx):
        W[i,j] = rho[j]*kernel(x[i]-x[j])


# Initialize Firing Rate and Nerual Field objects.
mu = 3.5
theta = 3.5
f = fr.FiringRate2(mu, theta)

neural_field = nf.NeuralField(f, W)


# ### Use Standard ODE Solvers

#Initial Conditions
A0 = 10; alpha = 0.1 # Parameters of Initial Conditions Function
initCond = lambda x_vec: A0/(np.cosh(alpha*x_vec)**2)
u0 = initCond(x)

# Time step using RungeKutta4
method = ode(neural_field).set_integrator("dopri5")
method.set_initial_value(u0)
final_t = 60
dt = 0.1
ts = [] 
us = []
while method.t < final_t:
    next_t = method.t+dt
    ts.append(next_t)
    next_u = method.integrate(next_t)
    us.append(next_u)
us = np.array(us)
ts = np.array(ts)

#Plot
import Plots as plts
plts.plotFinal(x, u0, us[-1],'',mu/theta)
pt.show()
#pt.savefig()

