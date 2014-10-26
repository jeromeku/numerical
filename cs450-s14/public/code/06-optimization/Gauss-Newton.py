
# Suppose $f(t,x) = x_0 e^{x_1 t}$
# 
# with data
# 
#     t: 0     1    2     3
#     y: 2.0   0.7  0.3   0.1
# 
# Use Gauss Newton to fit the data.

# In[4]:

import numpy as np
import scipy as sp
import matplotlib.pyplot as pt
import scipy.linalg as la


# Out[4]:

#     /usr/lib/python2.7/dist-packages/numpy/oldnumeric/__init__.py:11: ModuleDeprecationWarning: The oldnumeric module will be dropped in Numpy 1.9
#       warnings.warn(_msg, ModuleDeprecationWarning)
# 

# In[5]:

def residual(x):
    return y - x[0] * np.exp(x[1] * t)

def jacobian(x):
    return np.array([
        ...,
        ...
        ]).T


# <!--
# def jacobian(x):
#     return np.array([
#         -np.exp(x[1] * t),
#         -x[0] * t * np.exp(x[1] * t)
#         ]).T
# -->
# (Edit this cell for solution)

# In[6]:

# data
t = np.array([0.0, 1.0, 2.0, 3.0])
y = np.array([2.0, 0.7, 0.3, 0.1])


# In[16]:

# initial guess
x = np.array([1, 0])
#x = np.array([0.4, 2])

def plot_iterate(x):
    pt.plot(t, y, 'ro', markersize=20, clip_on=False)
    T = np.linspace(t.min(), t.max(), 100)
    Y = x[0] * np.exp(x[1] * T)
    pt.plot(T, Y, 'b-')

plot_iterate(x)


# Out[16]:

# image file:

# In[25]:

# evaluate this cell in-place many times (Ctrl-Enter)

J = jacobian(x)
r = residual(x)
s = la.lstsq(...)[0]
x = x + s
print la.norm(r)

plot_iterate(x)


# Out[25]:

#     0.0446775329872
# 

# image file:

# <!--
# s = la.lstsq(J, -r)[0]
# -->
# (Edit this cell for solution.)
