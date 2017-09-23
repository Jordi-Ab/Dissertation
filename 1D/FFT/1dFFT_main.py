
# coding: utf-8

from math import *
import numpy as np
from scipy.integrate import ode
from scipy.fftpack import fft
import FiringRate as fr
import ConnectivityKernel as ck
import NeuralFieldFFT as nf
import matplotlib.pyplot as pt
import warnings
warnings.simplefilter("ignore")

# Spatial Grid
nx = (2**10)-1 # Number of points in the space grid
Lx = 30 # Space grid limits
hx = 2*Lx/nx # Space width between points in the grid 
x = np.linspace(-Lx, Lx-hx, nx) # nx equally spaced points between -Lx and Lx-hx

# Initialize Connectivity Kernel
b=1
kernel = ck.ConnectivityKernel1(b)


# Plot the Chosen Connectivity Kernel:
plot_kernel = True
if(plot_kernel):
    fig = pt.figure()
    ax1 = fig.add_subplot(111)
    ax1.plot(x, kernel(x))
    ax1.set_title('Connectivity Kernel')
    ax1.set_xlabel('x')
    ax1.set_ylabel('w(x)')

# Heterogenous Vector
_a = .30
_epsilon = 1
A_vec = (1 + _a*np.cos(x/_epsilon))

# FFT of Synaptic Kernel
W = kernel(x)
W_hat = np.real(fft(W))

# Initialize Firing Rate
mu = 50
theta = 0.5
f_rate = fr.FiringRate1(mu, theta)

# Initialize Neural Field
neural_field = nf.NeuralFieldFFT(f_rate, W_hat, Lx, nx, A_vec)

# Use Standard ODE Solvers

#Initial Conditions
A0 = 10; alpha = 0.1 # Parameters of Initial Conditions Function
initCond = lambda x_vec: A0/(np.cosh(alpha*x_vec)**2)
u0 = initCond(x)

# Time step using RungeKutta45
method = ode(neural_field).set_integrator("dopri5")
method.set_initial_value(u0)
final_t = 100
dt = 0.1
sol = []
while method.t < final_t:
    next_u = method.integrate(method.t+dt)
    sol.append(next_u)

#Plot
fig = pt.figure(figsize=(15,4))

ax1 = fig.add_subplot(121)
ax1.plot(x, u0)
ax1.set_title('Synaptic Activity at Initial Time.')
ax1.set_xlabel('x')
ax1.set_ylabel('u(x)')

ax1 = fig.add_subplot(122)
ax1.plot(x, sol[-1])
ax1.set_title('Synaptic Activity at Final Time.')
ax1.set_xlabel('x')
ax1.set_ylabel('u(x)')

pt.show()



