
# coding: utf-8

# # Vector Norms

# $p$-norms can be computed in two different ways in numpy:

# In[18]:

import numpy as np
import numpy.linalg as la


# In[19]:

x = np.array([1.,2,3])


# In[20]:

np.sum(x**2)**(1/2)


# In[21]:

la.norm(x, 2)


# Both of the values above represent the 2-norm: $\|x\|_2$.

# --------------
# Different values of $p$ work similarly:

# In[22]:

np.sum(np.abs(x)**5)**(1/5)


# In[23]:

la.norm(x, 5)


# ---------------------
# 
# The $\infty$ norm represents a special case, because it's actually (in some sense) the *limit* of $p$-norms as $p\to\infty$.
# 
# Recall that: $\|x\|_\infty = \max(|x_1|, |x_2|, |x_3|)$.
# 
# Where does that come from? Let's try with $p=100$:

# In[24]:

x**100


# In[25]:

np.sum(x**100)


# Compare to last value in vector: the addition has essentially taken the maximum:

# In[26]:

np.sum(x**100)**(1/100)


# Numpy can compute that, too:

# In[27]:

la.norm(x, np.inf)

