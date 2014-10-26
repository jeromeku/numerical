
# coding: utf-8

# In[1]:

import numpy as np
import numpy.linalg as la


# In[3]:

X = np.random.randn(3,3)


# In[10]:

U, singvals, VT = la.svd(X)
V = VT.T
Sigma = np.diag(singvals)


# In[11]:

print(U)
print(Sigma)
print(V)


# In[12]:

X - U.dot(Sigma).dot(V.T)


# In[13]:

U2 = U.copy()
U2[:, 0] *= -1
V2 = V.copy()
V2[:, 0] *= -1


# In[14]:

X - U2.dot(Sigma).dot(V2.T)


# In[11]:




# In[11]:




# In[11]:




# In[ ]:



