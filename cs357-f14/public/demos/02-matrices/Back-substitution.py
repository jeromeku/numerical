
# coding: utf-8

# # Back-substitution

# In[2]:

import numpy as np


# In[11]:

n = 5

A = np.random.randn(n, n) * np.tri(n).T
print(A)

x = np.random.randn(n)
print(x)

b = np.dot(A, x)


# In[16]:

xcomp = np.zeros(n)

for i in range(n-1, -1, -1):
    tmp = b[i]
    for j in range(n-1, i, -1):
        tmp -= xcomp[j]*A[i,j]
        
    xcomp[i] = tmp/A[i,i]


# Now compare the computed $x$ against the reference solution.

# In[19]:

print(x)
print(xcomp)


# Questions/comments:
# 
# * Can this fail?
# * What's the operation count?
