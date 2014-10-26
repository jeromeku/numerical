
# coding: utf-8

# # Gaussian elimination with elimination matrices

# In[56]:

import numpy as np
import numpy.linalg as la


# In[57]:

n = 3

np.random.seed(15)
A = np.round(5*np.random.randn(n, n))

A


# `U` is the copy of `A` that we'll modify:

# In[58]:

U = A.copy()


# Now eliminate `U[1,0]`:

# In[59]:

M1 = np.eye(n)
M1[1,0] = -U[1,0]/U[0,0]
M1


# In[60]:

U = M1.dot(U)
U


# Now eliminate `U[2,0]`:

# In[61]:

M2 = np.eye(n)
M2[2,0] = -U[2,0]/U[0,0]


# In[62]:

U = np.dot(M2, U)
U


# Now eliminate `U[2,1]`:

# In[63]:

M3 = np.eye(n)
M3[2,1] = -U[2,1]/U[1,1]


# In[64]:

U = M3.dot(U)
U


# ------------------
# 
# Try inverting one of the `M`s:

# In[65]:

print(M2)
print(la.inv(M2))


# ----------------
# 
# So we've built `M3*M2*M1*A=U`. Test:

# In[66]:

U2 = M3.dot(M2.dot(M1.dot(A)))
U2


# In[67]:

U


# Now define `L`:

# In[68]:

L = la.inv(M1).dot(la.inv(M2).dot(la.inv(M3)))
L


# Observations? (Shape? Diagonal values?)

# In[69]:

np.dot(L, U) - A

