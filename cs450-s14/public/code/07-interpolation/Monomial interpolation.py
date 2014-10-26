
# In[24]:

from __future__ import division

import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as pt


# In[25]:

mesh = np.linspace(0, 1, 200)


# In[26]:

for i in range(10):
    pt.plot(mesh, mesh**i)


# Out[26]:

# image file:

# ### Vandermonde matrix

# In[35]:

n = 5    # also try: 10, 20

V = np.array([mesh**i for i in range(n)]).T        


# In[36]:

la.cond(V)


# Out[36]:

#     677.44361212

# In[ ]:



