
# coding: utf-8

# # "Complete" QR vs Reduced QR

# In[37]:

import numpy as np
import numpy.linalg as la


# In[38]:

A = np.random.randn(20, 5)


# In[39]:

Q, R = la.qr(A)


# In[40]:

print(Q.shape)
print(R.shape)


# In[41]:

la.norm(Q.dot(R) - A)


# Now try adding `"complete"` as an argument to `qr()`.

# ---------------
# Let's make our own 'complete' QR.

# In[42]:

m, n = A.shape

Qnew = np.zeros((m,m))
Qnew[:m,:n] = Q


# In[43]:

for i in range(n, m):
    q = np.random.randn(m)
    for j in range(i):
        prev_q = Qnew[:, j]
        q = q - prev_q.dot(q)*prev_q
    q = q/la.norm(q)
    Qnew[:, i] = q


# In[44]:

Rnew = np.zeros((m,n))
Rnew[:n,:n] = R


# In[45]:

la.norm(
    Qnew.T.dot(Qnew) - np.eye(m))


# In[46]:

la.norm(
    Qnew.dot(Rnew) - A)

