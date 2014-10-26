
# In[1]:

from __future__ import division

import numpy as np
import numpy.linalg as la


# In[2]:

n = 6

if 1:
    np.random.seed(70)
    eigvecs = np.random.randn(n, n)
    eigvals = np.sort(np.random.randn(n))
    # Uncomment for near-duplicate largest-magnitude eigenvalue
    # eigvals[1] = eigvals[0] + 1e-3

    A = np.dot(la.solve(eigvecs, np.diag(eigvals)), eigvecs)
    print eigvals
    
else:
    # Complex eigenvalues
    np.random.seed(40)
    A = np.random.randn(n, n)
    print la.eig(A)[0]

x0 = np.random.randn(n)


# Out[2]:

#     [-2.667651   -0.95797093 -0.33019549 -0.29151942 -0.18635343 -0.14418093]
# 

# ### Power iteration

# In[3]:

x = x0


# In[48]:

# Run this cell in-place (Ctrl-Enter) many times.
x = np.dot(A, x)
x


# Out[48]:

#     array([ -4.28616666e+19,  -4.53997702e+19,   8.19441238e+19,
#             -3.31918771e+19,   7.97142990e+19,   8.57108316e+19])

# ### Normalized power iteration

# In[49]:

x = x0/la.norm(x0)


# In[115]:

# Run this cell in-place (Ctrl-Enter) many times.

# x is unit-length here

x = np.dot(A, x)
nrm = la.norm(x)
x = x/nrm

print nrm
print x


# Out[115]:

#     2.66765099561
#     [ 0.2688559   0.28477652 -0.51400617  0.20820077 -0.50001928 -0.53763338]
# 

# What if we want smallest, not largest?

# In[117]:

x = x0/la.norm(x0)


# In[191]:

# Run this cell in-place (Ctrl-Enter) many times.

x = ...
nrm = la.norm(x)
x = x/nrm

print 1/nrm
print x


# Out[191]:

#     0.144180924949
#     [-0.26610396 -0.17430691  0.45852284 -0.11352085  0.51716735  0.63891591]
# 

# <!--
# x = la.solve(A, x)
# -->
# (Edit this cell for solution.)

# $\uparrow$ Inverse iteration

# How do we use the Rayleigh quotient?

# In[197]:

x = x0/la.norm(x0)


# In[208]:

# Run this cell in-place (Ctrl-Enter) many times.

sigma = np.dot(x, np.dot(A, x))/np.dot(x, x)
x = ...
x = x/la.norm(x)

print sigma
print x


# Out[208]:

#     -0.957970929184
#     [ 0.0539665   0.58040235 -0.44257009  0.39097236 -0.39553142 -0.39376129]
# 

# <!--
# x = la.solve(A-sigma*np.eye(n), x)
# -->
# (Edit this cell for solution.)

# $\uparrow$ Rayleigh quotient iteration

# * What's a reasonable stopping criterion?
# * Computational downside of Rayleigh quotient iteration?
