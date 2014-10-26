
# coding: utf-8

# # Computing the Nullspace

# In[41]:

import numpy as np
import numpy.linalg as la


# In[46]:

n = 5
np.random.seed(25)
A = np.random.randn(n, n)

# Decrease the rank
A[4] = A[0] + 5 * A[2]
A[1] = 3 * A[0] -2 * A[3]


# In[47]:

from scipy.linalg import lu


# In[48]:

PT, L, U = lu(A.T)
P = PT.T


# In[49]:

la.norm(
    P.dot(A.T) - L.dot(U))


# In[50]:

np.set_printoptions(precision=3)
U


# Now define `NUT` as vectors spanning the nullspace of $N(U^T)$.

# In[55]:

NUT = np.eye(n)[:, 3:]


# Check that it's actually a nullspace:

# In[56]:

U.T.dot(NUT)


# Now define `NA` as some vectors spanning $N(A)$:

# In[58]:

NA = P.T.dot(la.solve(L.T, NUT))


# And check:

# In[59]:

A.dot(NA)

