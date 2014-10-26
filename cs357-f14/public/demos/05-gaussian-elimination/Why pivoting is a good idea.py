
# coding: utf-8

# # Why pivoting is a good idea

# In[15]:

import numpy as np
import numpy.linalg as la


# In[43]:


A = np.array([
    [1e-20, 1],
    [1, 1],
])


# Now find an elimination matrix and go to town:

# In[44]:

U = A.copy()


# In[45]:

M = np.eye(2)
M[1,0] = -A[1,0]/A[0,0]


# In[46]:

U = M.dot(U)
U


# In[47]:

M


# Now define `L`:

# In[48]:

L = la.inv(M)


# In[49]:

L.dot(U) - A


# * Problem?
# * Is the lower right hand entry of `U` correct?
# * Now try with pivoting.
