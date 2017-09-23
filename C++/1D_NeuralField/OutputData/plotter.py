import numpy as np
import matplotlib.pyplot as pt

x = np.loadtxt('mesh.dat')
data = np.loadtxt('RK4_output.dat')

ts = data[:,0] # 1st column of each row
sol = data[:,1:] # All columns from 1st onwards

fig = pt.figure(figsize=(15,4))

ax1 = fig.add_subplot(121)
ax1.plot(x, sol[0])
ax1.set_title('Synaptic Potential at Initial Time.')
ax1.set_xlabel('x')
ax1.set_ylabel('u(x)')

ax2 = fig.add_subplot(122)
ax2.plot(x, sol[-1])
ax2.set_title('Synaptic Potential at Final Time.')
ax2.set_ylim(0,1.5)
ax2.set_xlabel('x')
ax2.set_ylabel('u(x)')

pt.show()