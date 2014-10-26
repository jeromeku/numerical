
# coding: utf-8

# # Pseudoinverse and Least Squares

# In[1]:

import numpy as np
import numpy.linalg as la

np.set_printoptions(precision=4, linewidth=100)


# In[2]:

A = np.random.randn(5, 3)


# Now compute the SVD of $A$. Note that `numpy.linalg.svd` returns $V^T$:

# In[3]:

U, singval, VT = la.svd(A)
V = VT.T


# Let's first understand the shapes of these arrays:

# In[4]:

print(U.shape)
print(singval.shape)
print(V.shape) 


# Check the orthogonality of $U$ and $V$:

# In[5]:

U.T.dot(U)


# In[6]:

V.T.dot(V)


# Now build the matrix $\Sigma$:

# In[7]:

Sigma = np.zeros(A.shape)
Sigma[:3, :3] = np.diag(singval)
Sigma


# Now piece $A$ back together from the factorization:

# In[8]:

U.dot(Sigma).dot(V.T) - A


# ----------------
# Next, compute the pseudoinverse:

# In[9]:

SigmaInv = np.zeros((3,5))
SigmaInv[:3, :3] = np.diag(1/singval)
SigmaInv


# In[10]:

A_pinv = V.dot(SigmaInv).dot(U.T)


# -------------
# Now use the pseudoinverse to "solve" $Ax=b$ for our tall-and-skinny $A$:

# In[11]:

b = np.random.randn(5)


# In[12]:

A_pinv.dot(b)


# ---------------
# Compare with the solution from QR-based Least Squares:

# In[13]:

Q, R = la.qr(A, "complete")
la.solve(R[:3], Q.T.dot(b)[:3])

