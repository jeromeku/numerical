
# coding: utf-8

# # Computing the Rank

# In[16]:

import numpy as np


# In[17]:

n = 5
A = np.random.randn(n, n)


# Now decrease the rank of `A`:

# In[18]:

A[4] = A[0] + 5 * A[2]
A[1] = 3 * A[0] -2 * A[2]


# What should the rank be now?

# -------------------
# Let's run Gaussian Elimination:

# In[19]:

np.set_printoptions(precision=4)

for i in range(n):
    # find biggest entry
    j = max(
        (j for j in range(i, n)),
        key=lambda j: abs(A[j, i]))
    
    # swap rows i and piv_row
    row_i = A[i].copy()
    row_j = A[j]
    A[i] = row_j
    A[j] = row_i
    
    # eliminate down
    for j in range(i+1, n):
        A[j] -= A[i] * A[j,i]/A[i,i]
        
    print(A)
    print()


# Now what is the rank of that matrix?
