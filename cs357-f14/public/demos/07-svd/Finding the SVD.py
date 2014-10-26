
# coding: utf-8

# # Finding the SVD

# In[10]:

import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as pt


# In[11]:

np.random.seed(27)
X = np.random.randn(2,2)


# In[7]:

phi = np.linspace(0, 2*np.pi, 100)
norm1_vecs = np.array([
    np.cos(phi),
    np.sin(phi)
])


# In[8]:

X_norm1_vecs = X.dot(norm1_vecs)

pt.grid()
pt.plot(X_norm1_vecs[0], X_norm1_vecs[1])
pt.gca().set_aspect("equal")


# Approximately, what is $\|X\|_2$?

# In[15]:

np.sqrt(1.3**2 + 0.6**2)


# In[16]:

la.norm(X, 2)


# --------------
# Let's find the vector $v_1$ that achieves that.
# 
# First, find the norms of all the $Xn$, where $n$ are the norm-1 vectors we generated above:

# In[18]:

norm_X_norm1_vecs = np.sqrt(np.sum(X_norm1_vecs**2, axis=0))


# Next, find the approximate 2-norm of X from this as `approx_norm`:

# In[19]:

approx_norm = np.max(norm_X_norm1_vecs)
approx_norm


# And find the vector $v_1$ that achieves `approx_norm`:

# In[22]:

np.where(norm_X_norm1_vecs == approx_norm)


# In[25]:

v1 = norm1_vecs[:, 48]


# In[28]:

la.norm(v1, 2)


# In[27]:


X_v1 = X.dot(v1)

pt.grid()
pt.plot(X_norm1_vecs[0], X_norm1_vecs[1])
pt.arrow(0, 0, X_v1[0], X_v1[1])
pt.gca().set_aspect("equal")


# ------------------
# Now $v_2$ has to be orthogonal--that doesn't leave much choice in 2D:

# In[32]:

v2 = np.array([v1[1], -v1[0]])


# In[33]:

print(la.norm(v2, 2))
print(v1.dot(v2))


# ------------
# Now define the matrices $V$ and $\Sigma$:

# In[36]:

V = np.array([v1, v2]).T
print(V)

Sigma = np.diag([
    la.norm(X.dot(v1)),
    la.norm(X.dot(v2))
])
print(Sigma)


# In[45]:

U = X.dot(V).dot(la.inv(Sigma))


# Now watch this:

# In[48]:

U.dot(U.T)


# Notice anything? (It's not very accurate, but still visible.)

# --------------
# What we have discovered is called the *singular value decomposition ("SVD")*.

# In[47]:

la.svd(X)


# In[53]:

print(U)
print(Sigma)
print(V)

