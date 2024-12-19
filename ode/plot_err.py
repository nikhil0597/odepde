#from mpl import *
import numpy as np
import matplotlib.pyplot as plt


#Loading the error files
euler = np.loadtxt("euler.txt")
rk2   = np.loadtxt("rk2.txt")
rk4   = np.loadtxt("rk4.txt")


#-------------------------------------

fig = plt.figure()
plt.loglog(euler[:,0],euler[:,1],'r--',fillstyle='none',label='Euler')
plt.loglog(rk2[:,0],rk2[:,1],'o-', fillstyle='none',label='RK-2', color='b')
plt.loglog(rk4[:,0],rk4[:,1],'.-',fillstyle='full',label='RK-4',c='g')
plt.xlabel('N')
plt.ylabel('Error')
plt.legend();                
plt.grid(True, linestyle = '--')
plt.savefig('error.pdf')