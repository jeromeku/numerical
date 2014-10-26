
# coding: utf-8

# # Orthogonal Iteration

# In[62]:

import numpy as np
import numpy.linalg as la


# Let's make a matrix with given eigenvalues:

# In[3]:

n = 5

np.random.seed(70)
eigvecs = np.random.randn(n, n)
eigvals = np.sort(np.random.randn(n))

A = np.dot(la.solve(eigvecs, np.diag(eigvals)), eigvecs)
print(eigvals)


# Let's make an array of iteration vectors:

# In[4]:

X = np.random.randn(n, n)


# Next, implement orthogonal iteration:
#     
# * Orthogonalize.
# * Apply A
# * Repeat
# 
# Run this cell in-place (Ctrl-Enter) many times.

# In[64]:

Q, R = la.qr(X)
X = np.dot(A, Q)
print(Q)


# Now check that the (hopefully) converged $Q$ actually led to Schur form:

# In[67]:

la.norm(
    np.dot(np.dot(Q, R), Q.T)
    - A)


# Do the eigenvalues match?

# In[68]:

R


# What are possible flaws in this plan?
# 
# * Will this always converge?
# * What about complex eigenvalues?
