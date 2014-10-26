
# In[20]:

from __future__ import division
import numpy as np
import numpy.linalg as la

import scipy.optimize as sopt

import matplotlib.pyplot as pt
from mpl_toolkits.mplot3d import axes3d


# In[2]:

# Oblong bowl

def f(x):
    return 0.5*x[0]**2 + 2.5*x[1]**2

def df(x):
    return np.array([x[0], 5*x[1]])

def ddf(x):
    return np.array([
                     [1,0],
                     [0,5]
                     ])


# In[21]:

# Rosenbrock's banana function

def f(X):
    x = X[0]
    y = X[1]
    val = 100.0 * (y - x**2)**2 + (1.0 - x)**2
    return val

def df(X):
    x = X[0]
    y = X[1]
    val1 = 400.0 * (y - x**2) * x - 2 * x
    val2 = 200.0 * (y - x**2)
    return np.array([val1, val2])

def ddf(X):
    x = X[0]
    y = X[1]
    val11 = 400.0 * (y - x**2) - 800.0 * x**2 - 2
    val12 = 400.0
    val21 = -400.0 * x
    val22 = 200.0
    return np.array([[val11, val12], [val21, val22]])


# In[22]:

# Plot the function in 3D

fig = pt.figure()
ax = fig.gca(projection="3d")

xmesh, ymesh = np.mgrid[-2:2:50j,-2:2:50j]
fmesh = f(np.array([xmesh, ymesh]))
ax.plot_surface(xmesh, ymesh, fmesh,
                alpha=0.3, cmap=pt.cm.coolwarm, rstride=3, cstride=3)


# Out[22]:

#     <mpl_toolkits.mplot3d.art3d.Poly3DCollection at 0x55d8c10>

# image file:

# In[23]:

# Plot as a contour plot

pt.axis("equal")
pt.contour(xmesh, ymesh, fmesh, 50)


# Out[23]:

#     <matplotlib.contour.QuadContourSet instance at 0x4ee6200>

# image file:

# ### Newton

# In[5]:

# Initialize the method

iterates = [np.array([2, 2./5])]


# In[6]:

# Evaluate this cell many times in-place

x = iterates[-1]
s = la.solve(ddf(x), -df(x))
next_iterate = x + s
print f(next_iterate)

iterates.append(next_iterate)

# plot function and iterates
pt.axis("equal")
pt.contour(xmesh, ymesh, fmesh, 50)
it_array = np.array(iterates)
pt.plot(it_array.T[0], it_array.T[1], "x-")


# Out[6]:

#     0.0
# 

#     [<matplotlib.lines.Line2D at 0x42e4650>]

# image file:

# ### Conjugate gradients

# In[174]:

# Initialize the method

x0 = np.array([2, 2./5])
#x0 = np.array([2, 1])

iterates = [x0]
gradients = [df(x0)]
directions = [-df(x0)]


# In[183]:

# Evaluate this cell many times in-place

x = iterates[-1]
s = directions[-1]

def f1d(alpha):
    return f(x + alpha*s)

alpha_opt = sopt.golden(f1d)
next_x = x + alpha_opt*s

g = df(next_x)
last_g = gradients[-1]
gradients.append(g)

beta = np.dot(g, g)/np.dot(last_g, last_g)
directions.append(-g + beta*directions[-1])

print f(next_x)

iterates.append(next_x)

# plot function and iterates
pt.axis("equal")
pt.contour(xmesh, ymesh, fmesh, 50)
it_array = np.array(iterates)
pt.plot(it_array.T[0], it_array.T[1], "x-")


# Out[183]:

#     0.605928022992
# 

#     [<matplotlib.lines.Line2D at 0x24c547d0>]

# image file:
