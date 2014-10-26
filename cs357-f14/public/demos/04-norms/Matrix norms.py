
# coding: utf-8

# # Function/Matrix norms

# In[1]:

import numpy as np
import numpy.linalg as la


# Here's a matrix of which we're trying to compute the norm:

# In[2]:

n = 3

A = np.random.randn(n, n)


# Recall:
# 
# $$||A||=\max_{x\ne 0} \frac{\|Ax\|}{\|x\|},$$
# 
# where the vector norm must be specified, and the value of the matrix norm $\|A\|$ depends on the choice of vector norm.
# 
# For instance, for the $p$-norms, we often write:
# 
# $$||A||_2=\max_{x\ne 0} \frac{\|Ax\|_2}{\|x\|_2},$$
# 
# and similarly for different values of $p$.

# --------------------
# We can approximate this by just producing very many random vectors and evaluating the formula:

# In[4]:

xs = np.random.randn(1000, 3)


# In[8]:

Axs = np.einsum("ij,kj->ki", A, xs)


# In[9]:

p = 2
norm_xs = np.sum(np.abs(xs)**p, axis=1)**(1/p)
norm_xs.shape


# In[10]:

norm_Axs = np.sum(np.abs(Axs)**p, axis=1)**(1/p)
norm_Axs.shape


# In[11]:

np.max(norm_Axs/norm_xs)


# In[12]:

la.norm(A, p)

