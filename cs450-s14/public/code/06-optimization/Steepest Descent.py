
# In[55]:

from __future__ import division
import numpy as np
import numpy.linalg as la

import scipy.optimize as sopt

import matplotlib.pyplot as pt
from mpl_toolkits.mplot3d import axes3d


# In[99]:

# Oblong bowl

def f(x):
    return 0.5*x[0]**2 + 2.5*x[1]**2

def df(x):
    return np.array([x[0], 5*x[1]])


# In[100]:

# Plot the function in 3D

fig = pt.figure()
ax = fig.gca(projection="3d")

xmesh, ymesh = np.mgrid[-2:2:50j,-2:2:50j]
fmesh = f(np.array([xmesh, ymesh]))
ax.plot_surface(xmesh, ymesh, fmesh)


# Out[100]:

#     <mpl_toolkits.mplot3d.art3d.Poly3DCollection at 0xd158750>

# image file:

# In[101]:

# Plot as a contour plot

pt.axis("equal")
pt.contour(xmesh, ymesh, fmesh)


# Out[101]:

#     <matplotlib.contour.QuadContourSet instance at 0xdcee128>

# image file:

# In[130]:

# Initialize the method

iterates = [np.array([2, 2./5])]


# In[129]:

x = iterates[-1]
s = -df(x)

def f1d(alpha):
    return f(x + alpha*s)

alpha_opt = sopt.golden(f1d)
next_iterate = x + alpha_opt * s
iterates.append(next_iterate)

# plot function and iterates
pt.axis("equal")
pt.contour(xmesh, ymesh, fmesh)
it_array = np.array(iterates)
pt.plot(it_array.T[0], it_array.T[1], "x-")


# Out[129]:

#     [<matplotlib.lines.Line2D at 0x1151f490>]

# image file:

# In[ ]:



