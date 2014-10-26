
# In[1]:

from __future__ import division

import numpy as np
import numpy.linalg as la


# In[2]:

n = 3

e1 = np.array([1,0,0])
e2 = np.array([0,1,0])
e3 = np.array([0,0,1])

A = np.random.randn(3, 3)
A


# Out[2]:

#     array([[ 0.47748905, -0.39916192,  0.40139911],
#            [ 0.43535359,  0.24187108, -0.66839074],
#            [ 0.30276693, -1.2088603 , -0.87829135]])

# Householder reflector:
# $$I-2\frac{vv^T}{v^Tv}$$
# 
# Choose $v=a-\|a\|e_1$.

# In[6]:

a = A[:, 0]
v = a-la.norm(a)*e1

H1 = ...
A1 = np.dot(H1, A)
A1


# Out[6]:

#     array([[  7.13579951e-01,  -6.32443387e-01,  -5.11842021e-01],
#            [  5.55111512e-17,   6.72044039e-01,   1.01563347e+00],
#            [  8.32667268e-17,  -9.09696239e-01,   2.92864361e-01]])

# <!--
# H1 = np.eye(3) - 2*np.outer(v, v)/np.dot(v, v)
# -->
# (Edit this cell for solution.)

# NB: Never build full Householder matrices in actual code! (Why? How?)

# In[7]:

a = A1[:, 1].copy()
a[0] = 0
v = a-la.norm(a)*e2

H2 = ...
R = np.dot(H2, A1)
R


# Out[7]:

#     array([[  7.13579951e-01,  -6.32443387e-01,  -5.11842021e-01],
#            [ -3.39885479e-17,   1.13101301e+00,   3.67929286e-01],
#            [ -9.41255243e-17,  -1.11022302e-16,  -9.90913173e-01]])

# <!--
# H2 = np.eye(3) - 2*np.outer(v, v)/np.dot(v, v)
# -->
# (Edit this cell for solution.)

# In[8]:

Q = np.dot(H2, H1).T
la.norm(np.dot(Q, R) - A)


# Out[8]:

#     5.2735593669694936e-16
