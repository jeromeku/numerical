
# coding: utf-8

# # Orthogonalizing three vectors

# In[1]:

import numpy as np
import numpy.linalg as la


# In[3]:

np.random.seed(13)
xorig = np.random.randn(200)
yorig = np.random.randn(200)
zorig = np.random.randn(200)


# Orthonormalize $x$ and $y$ as we know:

# In[4]:

x = xorig/la.norm(xorig)


# In[6]:

y = yorig
y = y - x.dot(y)*x
y = y / la.norm(y)


# Check:

# In[7]:

print(la.norm(x))
print(la.norm(y))
print(x.dot(y))


# Now what to with $z$?

# In[8]:

z = zorig
z = z - np.dot(z, x)*x - np.dot(z,y)*y
z = z / la.norm(z)


# Check:

# In[9]:

print(la.norm(z))
print(x.dot(z))
print(y.dot(z))

