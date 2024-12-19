import numpy as np

xmin, xmax = -1.0, 1.0
ymin, ymax = -1.0, 1.0


def initial_condition(x,y):
    return np.sin(2*np.pi*x) * np.sin(2*np.pi*y)
