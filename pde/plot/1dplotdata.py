import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.size'] = 16
plt.rcParams['font.family'] = 'serif'
plt.rcParams['figure.autolayout'] = True
plt.rcParams['lines.linewidth'] = 2
plt.rcParams['lines.markersize'] = 10
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['axes.labelsize'] = 16
plt.autoscale(enable=True, axis='x', tight=True)
#plt.rcParams['text.usetex'] = True    # This will use Latex fonts (slow)
plt.axis('tight')
plt.autoscale(enable=True, axis='x', tight=True)

uw = np.loadtxt("uw.txt")
ex = np.loadtxt("exact.txt")
plt.figure()
plt.plot(uw[:,0],uw[:,1],'-',label='UW', c = 'k', marker ='o',markersize = 5)
plt.plot(ex[:,0],ex[:,1],'-',label='Exact', c = 'b')
plt.xlim(0,1)
plt.xlabel('x')
plt.ylabel('u')
plt.legend(fontsize=12);
plt.grid(True, linestyle = '--', linewidth = 0.5)

plt.savefig('solution.pdf')
