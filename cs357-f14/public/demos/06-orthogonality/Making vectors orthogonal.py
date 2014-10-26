
# coding: utf-8

# # Making vectors orthogonal

# In[4]:

import numpy as np
import matplotlib.pyplot as pt


# In[25]:

np.random.seed(13)
x = np.random.randn(2)
y = np.random.randn(2)


# In[22]:

pt.arrow(0, 0, x[0], x[1], color="blue")
pt.arrow(0, 0, y[0], y[1], color="red")
pt.xlim([-1, 1])
pt.ylim([-1, 1])
pt.gca().set_aspect("equal")
pt.grid()


# Are those orgonal? How would we find out?

# In[26]:

x.dot(y)


# Now use the formula to make `ynew` which *is* orthogonal to `x`:

# In[27]:

ynew = y - y.dot(x)/x.dot(x)*x


# In[28]:

pt.arrow(0, 0, x[0], x[1], color="blue")
pt.arrow(0, 0, ynew[0], ynew[1], color="red")
pt.xlim([-1, 1])
pt.ylim([-1, 1])
pt.gca().set_aspect("equal")
pt.grid()


# In[ ]:



