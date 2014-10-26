
# coding: utf-8

# In[1]:

import numpy as np


# In[3]:

a = np.arange(9).reshape(3, 3)
print(a.shape)
print(a)
b = np.arange(4, 4+9).reshape(3, 3)
print(b.shape)
print(b)


# In[4]:

a+b


# So this is easy and one-to-one.
# 

# ---
# 
# What if the shapes do not match?

# In[5]:

a = np.arange(9).reshape(3, 3)
print(a.shape)
print(a)
b = np.arange(3)
print(b.shape)
print(b)


# What will this do?

# In[6]:

a+b


# It has *broadcast* along the last axis!

# ---
# 
# Can we broadcast along the *first* axis?

# In[8]:

a+b[:, np.newaxis]


# What's the shape of the `newaxis` thing?

# In[9]:

b[:, np.newaxis].shape


# Rules:
# 
# * Shapes are matched axis-by-axis from last to first.
# * A length-1 axis can be *broadcast* if necessary.
