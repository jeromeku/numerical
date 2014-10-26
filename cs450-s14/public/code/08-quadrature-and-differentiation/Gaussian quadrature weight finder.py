
# In[4]:

from __future__ import division

import numpy as np
import numpy.linalg as la
import scipy.special as sps
import matplotlib.pyplot as pt


# In[5]:

# Set parameters

n = 5
left_end_nodes = 0
right_end_nodes = 0


# In[6]:

# Ignore (don't even evaluate) this cell at the outset.

# If enabled, it computes weights for variants of Gauss 
# quadratures that include interval ends.

# Enable (only) this for Gauss-Radau:
if 1:
    left_end_nodes = 1
    
# Enable (only) this for Gauss-Lobatto:
if 0:
    left_end_nodes = 1
    right_end_nodes = 1


# In[7]:

deg_reduction = left_end_nodes+right_end_nodes

nodes = np.empty(n)
nodes[left_end_nodes:n-right_end_nodes] =     sps.legendre(n - deg_reduction).weights[:, 0] 

nodes[:left_end_nodes] = -1
nodes[n-right_end_nodes:] = 1

mesh = np.linspace(-1, 1, 300)

pt.plot(mesh, sps.eval_legendre(n - deg_reduction, mesh))
pt.plot(nodes, 0*nodes, "o")


# Out[7]:

#     [<matplotlib.lines.Line2D at 0x38fac50>]

# image file:

# In[8]:

# Use method of undetermined coefficients to find
# Newton-Cotes rule for Gauss nodes.

max_degree = len(nodes) - 1
powers = np.arange(max_degree+1)

Vt = nodes ** powers.reshape(-1, 1)

a, b = -1, 1
rhs = 1/(powers+1) * (b**(powers+1) - a**(powers+1))

weights = la.solve(Vt, rhs)


# In[9]:

for i in range(2*len(nodes) + 1):
    approx = np.dot(weights, nodes**i)
    true = 1/(i+1)*(1. - (-1)**(i+1))
    
    print "Error at degree %d: %g" % (i, approx-true)


# Out[9]:

#     Error at degree 0: 0
#     Error at degree 1: -1.11022e-16
#     Error at degree 2: -1.11022e-16
#     Error at degree 3: -2.498e-16
#     Error at degree 4: 0
#     Error at degree 5: -4.71845e-16
#     Error at degree 6: 2.22045e-16
#     Error at degree 7: -5.68989e-16
#     Error at degree 8: -0.01161
#     Error at degree 9: -6.66134e-16
#     Error at degree 10: -0.0257832
# 

# In[ ]:



