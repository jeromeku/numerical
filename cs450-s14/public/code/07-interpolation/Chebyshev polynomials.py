
# In[1]:

from __future__ import division

import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as pt


# In[2]:

x = np.linspace(-1, 1, 100)

pt.xlim([-1.2, 1.2])
pt.ylim([-1.2, 1.2])

for k in range(2): # crank up
    pt.plot(x, np.cos(k*np.arccos(x)))


# Out[2]:

# image file:

# ## Does any of this matter?
# 
# What if we interpolate random data?

# In[15]:

n = 10 # crank up

i = np.arange(n, dtype=np.float64)

# Chebyshev nodes:
nodes = np.cos((2*(i+1)-1)/(2*n)*np.pi)

# Equispace nodes:
# nodes = np.linspace(-1, 1, n)


# In[16]:

pt.plot(nodes, 0*nodes, "o")


# Out[16]:

#     [<matplotlib.lines.Line2D at 0x589b090>]

# image file:

# In[17]:

V = np.cos(i*np.arccos(nodes.reshape(-1, 1)))
data = np.random.randn(n)
coeffs = la.solve(V, data)


# In[18]:

x = np.linspace(-1, 1, 1000)
Vfull = np.cos(i*np.arccos(x.reshape(-1, 1)))
pt.plot(x, np.dot(Vfull, coeffs))
pt.plot(nodes, data, "o")


# Out[18]:

#     [<matplotlib.lines.Line2D at 0x5563f10>]

# image file:

# In[75]:



