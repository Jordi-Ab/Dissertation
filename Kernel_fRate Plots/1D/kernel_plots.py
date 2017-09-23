import ConnectivityKernel as ck
import matplotlib.pyplot as pt
import numpy as np

b = 1/2

x = np.linspace(-10, 10, 1000)
ker1 = ck.ConnectivityKernel1(b)
ker2 = ck.ConnectivityKernel2(b)

w1 = ker1.evaluateAt(x)
w2 = ker2.evaluateAt(x)

fig1 = pt.figure(figsize = (11,5))
ax1 = fig1.add_subplot(121)
ax1.plot(x, w1)
ax1.set_xlabel('x')
ax1.set_ylabel('W(x)')
ax1.set_title('(a) "Wizard Hat" shape function')

ax2 = fig1.add_subplot(122)
ax2.plot(x, w2)
ax2.plot(x, np.zeros(len(x)), 'k-')
#ax2.text(0.3,0.3, "escrom")
#ax2.text(4,-0.1, "escrom")
ax2.annotate('Activation', xy=(0.3, 0.3), xytext=(3, 0.5), 
	arrowprops=dict(arrowstyle="->",connectionstyle="arc3"))
ax2.annotate('Inhibition', xy=(3, -0.1), xytext=(5, -0.2), 
	arrowprops=dict(arrowstyle="->",connectionstyle="arc3"))
ax2.set_xlabel('x')
ax2.set_ylabel('W(x)')
ax2.set_title('(b) "Mexican Hat" shape function')

fig1.savefig("Kernels.png")

pt.show()