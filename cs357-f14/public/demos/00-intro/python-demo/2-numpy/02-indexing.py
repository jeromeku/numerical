
# coding: utf-8

# In[1]:

import numpy as np


# In[2]:

a = np.random.rand(3,4,5)
a.shape


# What's the result of this?

# In[3]:

a[0].shape


# And this?

# In[4]:

a[...,2].shape


# In[5]:

a[1,0,3]


# Like all other things in Python, numpy indexes from 0.

# In[6]:

a[3,2,2].shape


# In[7]:

a[:,2].shape


# ---
# 
# Indexing into numpy arrays usually results in a so-called *view*.

# In[8]:

a = np.zeros((4,4))
a


# Let's call `b` the top-left $2\times 2$ submatrix.

# In[9]:

b = a[:2,:2]
b


# What happens if we change `b`?

# In[10]:

b[1,0] = 5
b


# In[12]:

print(a)


# To decouple `b` from `a`, use `.copy()`.

# In[13]:

b = b.copy()
b[1,1] = 7
print(a) 


# ----
# 
# You can also index with other arrays:

# In[14]:

a = np.random.rand(4,4)
a


# In[15]:

i = np.array([0,2])
a[i]


# ---
# 
# And with conditionals:

# In[16]:

a>0.5


# In[17]:

a[a>0.5]

