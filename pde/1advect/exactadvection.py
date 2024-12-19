from xml import dom
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from functools import partial
from scipy import optimize

def smooth(x):
    return np.sin(2.0*np.pi*x)


x  = np.linspace(0,1,200)
u  = smooth(x)

fig = plt.figure()
ax = fig.add_subplot(111)
line1, = ax.plot(x, u)   
plt.grid(True); plt.draw(); plt.pause(1)

Tf = 0.3; # final time
deltat = 0.01
t = 0 

while t < Tf:
    t += deltat
    for i in range(0, len(x)):
        u[i]  = smooth(x[i]-t)
    line1.set_ydata(u)
    plt.draw(); plt.pause(0.1)
    
plt.show()
# u_t + c u_x = 0,  u(x,t ) = g(x-ct)
# u(x,0) = g(x)   