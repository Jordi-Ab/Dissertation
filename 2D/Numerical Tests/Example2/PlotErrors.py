import matplotlib.pyplot as plt
import numpy as np

hs, errors = np.loadtxt("Errors.csv", unpack=True)

diff = hs[-1] - errors[-1]
print(diff)

plt.loglog(hs, errors, 'bo', label = 'errors')
plt.loglog(hs, (hs**8)/20e3, 'r-', label = r'$O(h^8)$')

plt.legend(loc = 'upper left')
plt.xlabel('h')
plt.ylabel('error')
plt.savefig('2dRectTest2_q=4_case3.png')

plt.show()