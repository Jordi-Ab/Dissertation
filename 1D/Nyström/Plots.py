import matplotlib.pyplot as pt
from numpy import ones

def plotFinal(xs, u0, un, title='', threshold = 0):
	fig = pt.figure(figsize=(7,5))

	ax = fig.add_subplot(111)
	ax.plot(xs, u0, 'k--',label=r'Initial Condition')
	ax.plot(xs, un, 'b-', label=r'Synaptic Activity')
	ax.plot(xs, threshold*ones(len(xs)), 'r-', label=r'Threshold $\mu/\theta$')
	ax.set_xlabel('x')
	ax.set_ylabel(r'$u(x, 60)$')
	ax.set_title(title)
	ax.legend(fontsize = 'medium')

