import numpy as np
import matplotlib.pyplot as plt
from matplotlib.mlab import griddata

def grid(x, y, z, resX=100, resY=100):
    "Convert 3 column data to matplotlib grid"
    xi = np.linspace(min(x), max(x), resX)
    yi = np.linspace(min(y), max(y), resY)
    Z = griddata(x, y, z, xi, yi)
    X, Y = np.meshgrid(xi, yi)
    return X, Y, Z

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

data = np.loadtxt('OutputData/RK4_output.dat')
xs, ys = np.loadtxt('OutputData/interior_points_grid.dat', unpack = True)

ts = data[:,0] # 1st column of each row
us = data[:,1:] # All columns from 1st onwards

u0 = us[0]
un = us[100]

fig = plt.figure(figsize=(15,4))

# Plot initial time
ax1 = fig.add_subplot(121)
x0, y0, z0 = grid(xs, ys, u0)
cont1 = ax1.contour(x0, y0, z0, 20)
cont1 = ax1.tricontour(xs, ys, u0)
ax1.set_title("Synaptic Potential at Initial Time")
plt.colorbar(cont1)

#Plot final time
ax2 = fig.add_subplot(122)
xn, yn, zn = grid(xs, ys, un)
cont2 = ax2.contour(xn, yn, zn, 20)
#cont2 = ax2.tricontour(xs, ys, un)
ax2.set_title("Synaptic Potential at Final Time")
plt.colorbar(cont2)
plt.show()


