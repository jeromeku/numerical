
# coding: utf-8

# Let's import the `numpy` module.

# In[1]:

import numpy as np


# In[3]:

n = 10  # CHANGE ME
a1 = list(range(n))
a2 = np.arange(n)

if n <= 10:
    print(a1)
    print(a2)


# In[4]:

get_ipython().magic(u'timeit [i**2 for i in a1]')


# In[5]:

get_ipython().magic(u'timeit a2**2')


# Numpy Arrays: much less flexible, but:
# 
# * much faster
# * less memory

# ---
# 
# Ways to create a numpy array:
# 
# * Casting from a list

# In[6]:

np.array([1,2,3])


# * `linspace`

# In[7]:

np.linspace(-1, 1, 10)


# * `zeros`

# In[8]:

np.zeros((10,10), np.float64)


# ---
# 
# Operations on arrays propagate to all elements:

# In[9]:


a = np.array([1.2, 3, 4])
b = np.array([0.5, 0, 1])


# Addition, multiplication, power, .. are all elementwise:

# In[10]:

a+b


# In[11]:

a*b


# In[12]:

a**b


# Matrix multiplication is `np.dot(A, B)` for two 2D arrays.

# ---
# 
# Numpy arrays have two (most) important attributes:

# In[13]:

a = np.random.rand(5, 4, 3)
a.shape


# In[14]:

a.dtype


# Other `dtype`s include `np.complex64`, `np.int32`, ...
