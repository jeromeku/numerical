
# In[1]:

from __future__ import division

import numpy as np
import numpy.linalg as la

import matplotlib.pyplot as pt


# In[2]:

np.random.seed(40)

# Generate matrix with eigenvalues 1...25
n = 25
eigvals = np.linspace(1., n, n)
eigvecs = np.random.randn(n, n)
print eigvals

A = la.solve(eigvecs, np.dot(np.diag(eigvals), eigvecs))
print la.eig(A)[0]


# Out[2]:

#     [  1.   2.   3.   4.   5.   6.   7.   8.   9.  10.  11.  12.  13.  14.  15.
#       16.  17.  18.  19.  20.  21.  22.  23.  24.  25.]
#     [ 25.  24.  23.   1.   2.   3.  22.   4.  21.  20.   5.   6.   7.  19.  18.
#        8.   9.  17.  16.  10.  11.  12.  15.  14.  13.]
# 

# In[82]:

# Initialize Arnoldi iteration

# Set up Q and H
Q = np.zeros((n, n))
H = np.zeros((n, n))

k = 0

# Pick a starting vector, normalize it
x0 = np.random.randn(n)
x0 = x0/la.norm(x0)

# Poke it into the first column of Q
Q[:, k] = x0

del x0

# ritz_values = []


# In[107]:

# Carry out one iteration of Arnoldi iteration
# Run this cell in-place (Ctrl-Enter) until H is filled.

print k

u = np.dot(A, Q[:, k])

# Carry out Gram-Schmidt on u against Q
for j in range(k+1):
    qj = Q[:, j]
    H[j,k] = np.dot(qj, u)
    u = u - H[j,k]*qj

if k+1 < n:
    H[k+1, k] = la.norm(u)
    Q[:, k+1] = u/H[k+1, k]

k += 1

pt.spy(H)

# ritz_values.append(la.eig(H)[0])


# Out[107]:

#     24
# 

# image file:

# In[108]:

# Check that Q^T A Q = H

la.norm(
        np.dot(np.dot(Q.T, A), Q)
        - H) / la.norm(A)


# Out[108]:

#     6.9230906536862802e-06

# In[109]:

# Check that Q is orthogonal

la.norm(
        np.dot(Q.T, Q) - np.eye(n))


# Out[109]:

#     1.3525100273749116e-05

# #### Plot convergence of Ritz values

# In[110]:

# Enable the Ritz value collection above to make this work.

for i, rv in enumerate(ritz_values):
    plot([i] * len(rv), rv, "x")


# Out[110]:

#     /usr/lib/pymodules/python2.7/numpy/core/numeric.py:460: ComplexWarning: Casting complex values to real discards the imaginary part
#       return array(a, dtype, copy=False, order=order)
# 

# image file:

# In[ ]:



