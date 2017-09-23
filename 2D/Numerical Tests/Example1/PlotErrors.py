import matplotlib.pyplot as plt
import numpy as np

hs, errors = np.loadtxt("Errors.csv", unpack=True)

#p2 = np.poly1d(np.polyfit(ts,errors,2))

plt.loglog(hs, errors, 'bo', label = 'errors')
#plt.loglog(ts, p2(ts), 'r-', label = r'$O(h_t^2)$')
plt.loglog(hs, (hs**4)/10e2, 'r-', label = r'$O(h^4)$')
plt.legend(loc = 'upper left')
plt.xlabel('h')
plt.ylabel('error')
plt.savefig('Test1_Errors_q=2.png')

plt.show()