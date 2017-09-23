import ConnectivityKernel as ck
import FiringRate as fr
import matplotlib.pyplot as pt
import numpy as np

b = 0.4

miu = 3
theta = 5.6

x = np.linspace(-10, 10, 1000)

f_rate = fr.FiringRate2(miu, theta)
ker = ck.ConnectivityKernel2(b)

f = f_rate.evaluateAt(x)
w = ker.evaluateAt(x)

fig1 = pt.figure(figsize = (11,5))
ax1 = fig1.add_subplot(121)
ax1.plot(x, f)
ax1.set_xlabel('x')
ax1.set_ylabel('f(x)')
ax1.set_title('Firing Rate')
ax1.set_ylim(-0.3, 1.3)
ax1.set_xlim(-2,4)

ax2 = fig1.add_subplot(122)
ax2.plot(x, w)
ax2.plot(x, np.zeros(len(x)), 'k-')
ax2.set_xlabel('x')
ax2.set_ylabel('W(x)')
ax2.set_title('Connectivity Kernel')

fig1.savefig("1D_fRate_ker_nystrom.png")

pt.show()