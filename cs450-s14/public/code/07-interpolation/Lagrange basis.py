
# In[1]:

from __future__ import division

import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as pt


# In[28]:

#nodes = [0, 0.3]
nodes = [0, 0.3, 0.8]
#nodes = [0, 0.3, 0.8, 2, 3]


# In[23]:

def lagrange_basis_func(j, x):
    ...            
    return result


# <!--
#     result = 1
#     for k, x_k in enumerate(nodes):
#         if k != j:
#             result = result * (x-x_k)/(nodes[j]-x_k)
# -->
# (Edit cell for solution)

# In[24]:

mesh = np.linspace(-0.5, 3.5, 100)


# In[26]:

pt.axhline(0, color="black")
pt.axhline(1, linestyle="--", color="black", alpha=0.3)
for node in nodes:
    pt.axvline(node, linestyle="--", color="black", alpha=0.3)

for i in range(len(nodes)):
    pt.plot(mesh, lagrange_basis_func(i, mesh))
    
pt.ylim([-2,2])


# Out[26]:

#     (-2, 2)

# image file:

# Questions:
# 
# * How many interpolating polynomials are there?
# * Is interpolation any good outside of the interval?

# In[36]:

nodes = [0, 0.5, 2, 2.5]
values = np.random.randn(4)

def f(x):
    # Make f interpolate 'values' at 'nodes'
    return (
        ...
        )


# <!--
# values[0] * lagrange_basis_func(0, x)
# + values[1] * lagrange_basis_func(1, x)
# + values[2] * lagrange_basis_func(2, x)
# + values[3] * lagrange_basis_func(3, x)
# -->
# 
# (Edit this cell for solution.)

# In[37]:

pt.plot(nodes, values, "o")
pt.plot(mesh, f(mesh))


# Out[37]:

#     [<matplotlib.lines.Line2D at 0x496bdd0>]

# image file:

# In[ ]:



