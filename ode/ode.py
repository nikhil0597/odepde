"""
for odes
""" 
from xml import dom
import numpy as np
import matplotlib.pyplot as plt
import argparse

# Get arguments
parser = argparse.ArgumentParser()
parser.add_argument('-tmin', type=float, help='starting time', default=-1.0)
parser.add_argument('-tmax', type=float, help='final time', default=1.0)
parser.add_argument('-yinit', type=float, help='initial datum', default=2.0)
parser.add_argument('-nc', type=int, help='Number of cells', default=100)
parser.add_argument('-compute_error', choices=('no','yes'),
                    help='Compute error norm', default='no')
parser.add_argument('-time_scheme', default = 'euler',
                    help = 'Chosen by degree if unspecified',
                    choices = ('euler','rk2', 'rk4'))
parser.add_argument('-plot', choices=('no','yes'),
                    help='Plot the solution', default='yes')
args = parser.parse_args()

# constants
nc    = args.nc
time_scheme = args.time_scheme
yinit=  args.yinit
tmin, tmax = args.tmin, args.tmax
dt = (tmax - tmin)/ nc             # Step size based on number of cells

def f(t, y): # RHS of the ODE
    #return np.cos(t)  
    return (y**2) - (((t**4)-6*(t**3)+12*(t**2)-(14*t)+9)/((1+t)**2))

def uexact(t,yinit):
    #return np.sin(t)  #exact solution
    return (1-t)*(2-t)/(1+t)

#Error computation
def compute_error(u1,exact,f, tmin, tmax,yinit, time_scheme):
    glob_err = 0.0
    glob_err = np.abs(u1[-1]-exact(tmax,yinit))
    return glob_err

def euler_method(f, y0, tmin, tmax, nc):                 
    t_values = np.linspace(tmin, tmax, nc + 1)  # Time points (nc + 1 to include both ends)
    y_values = np.zeros(len(t_values))         # Solution array
    y_values[0] = y0                           # Initial condition
    for i in range(1, len(t_values)):
        t = t_values[i - 1]
        y = y_values[i - 1]
        y_values[i] = y + (dt * f(t, y))          # Euler formula
    return t_values, y_values


def rk2(f, y0, tmin, tmax, nc):
    """
    Second-order Runge-Kutta method for solving ODEs (Midpoint Method).
    """
    #dt = (tmax - tmin) / nc               # Step size
    t_values = np.linspace(tmin, tmax, nc + 1)  # Time points
    y_values = np.zeros(len(t_values))         # Solution array
    y_values[0] = y0                           # Initial condition
    
    for i in range(1, len(t_values)):
        t = t_values[i - 1]
        y = y_values[i - 1]
        
        # RK2 coefficients
        k1 = dt * f(t, y)                      # Slope at the beginning of the interval
        k2 = dt * f(t + dt / 2, y + k1 / 2)    # Slope at the midpoint
        
        # Update the solution
        y_values[i] = y + k2
    
    return t_values, y_values


def rk4(f, y0, tmin, tmax, nc):
    """
    Fourth-order Runge-Kutta method for solving ODEs.
    """
    t_values = np.linspace(tmin, tmax, nc + 1)  # Time points
    y_values = np.zeros(len(t_values))         # Solution array
    y_values[0] = y0                           # Initial condition

    for i in range(1, len(t_values)):
        t = t_values[i - 1]
        y = y_values[i - 1]

        # RK4 coefficients
        k1 = dt * f(t, y)
        k2 = dt * f(t + dt / 2, y + k1 / 2)
        k3 = dt * f(t + dt / 2, y + k2 / 2)
        k4 = dt * f(t + dt, y + k3)

        # Update the solution
        y_values[i] = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6

    return t_values, y_values

time_schemes = {'euler': euler_method, 'rk2' : rk2, 'rk4' : rk4 }
t_values, y_values = time_schemes[time_scheme](f, yinit, tmin, tmax, nc)

#to plot the exact solution
te = np.linspace(t_values[0], t_values[-1], 10000)
exact_values = uexact(te, yinit)

# Plot the solution
if args.plot == 'yes':
    plt.figure(figsize=(8, 5))
    plt.plot(t_values, y_values, label="Approximate solution", marker='o', linestyle='--')
    plt.plot(te, exact_values, label="Exact solution", linestyle='-', color='red')
    plt.xlabel('t')
    plt.ylabel('u')
    plt.title("Solution of ODE")
    plt.grid()
    plt.legend()
    plt.show()


# save the approximate solution to a file
fname = 'sol.txt'
np.savetxt(fname, np.column_stack([t_values, y_values]))
print('Saved file ', fname)
#-------------------
# save exact time solution to another file
fname = 'exact.txt'
np.savetxt(fname, np.column_stack([te, exact_values]))
print('Saved file ', fname)

if args.compute_error == 'yes':
    er1 = compute_error(y_values,uexact,f, tmin, tmax, yinit, time_scheme)
    print('No. of cells, Global error')
    print(nc, er1)




