
# coding: utf-8

# # Gaussian Elimination with Partial Pivoting

# In[1]:

import numpy as np


# In[38]:

n = 3

np.random.seed(22)
A = np.round(5*np.random.randn(n, n))
A[0,0] = 0
A


# ----------------
# Now define a function `row_swap_mat(i, j)` that returns a permutation matrix that swaps row i and j:

# In[39]:

def row_swap_mat(i, j):
    P = np.eye(n)
    P[i] = 0
    P[j] = 0
    P[i, j] = 1
    P[j, i] = 1
    return P


# What do these matrices look like?

# In[40]:

row_swap_mat(0,1)


# Do they work?

# In[41]:

row_swap_mat(0,1).dot(A)


# --------------

# `U` is the copy of `A` that we'll modify:

# In[63]:

U = A.copy()


# Create P1 to swap up the right row: 

# In[64]:

P1 = row_swap_mat(0, 2)
U = P1.dot(U)
U


# In[65]:

M1 = np.eye(n)
M1[1,0] = -U[1,0]/U[0,0]
M1


# In[66]:

U = M1.dot(U)
U


# Create `P2` to swap up the right row:

# In[67]:

P2 = row_swap_mat(1,2)
U = P2.dot(U)
U


# In[68]:

M2 = np.eye(n)
M2[2,1] = -U[2,1]/U[1,1]
M2


# In[69]:

U = M2.dot(U)
U


# So we've built $M_2P_2M_1P_1A=U$.

# In[75]:

M2.dot(P2).dot(M1).dot(P1).dot(A)


# ------------------
# Can't simply sort the permutation matrices out of the way:

# In[77]:

M2.dot(P2).dot(M1).dot(P1)


# In[80]:

M2.dot(M1).dot(P2).dot(P1)


# -----------------
# But: We now know the right reordering!

# In[87]:

P = P2.dot(P1)
P


# In[90]:

PA = P.dot(A)
PA

