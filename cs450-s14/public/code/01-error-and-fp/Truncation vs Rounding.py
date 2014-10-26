
# In[4]:

import numpy as np
import matplotlib.pyplot as pt


# **Task:** Approximate a function (here: by a line)

# In[5]:

def f(x):
    return - x**2 + 3*x

def df(x):
    return -2*x + 3

center = -1
dist = 3
grid = np.linspace(center-dist, center+dist, 100)

fx = f(grid)
pt.plot(grid, fx)
pt.plot(grid, f(center) + df(center) * (grid-center))

pt.xlim([grid[0], grid[-1]])
pt.ylim([np.min(fx), np.max(fx)])


# Out[5]:

#     (-28.0, 2.2497704315886136)

# image file:

# * What's the error we see?
# * What if we make `dist` smaller?
