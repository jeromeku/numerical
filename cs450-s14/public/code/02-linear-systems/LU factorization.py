
# In[1]:

from __future__ import division

import numpy as np
import numpy.linalg as la


# In[2]:

A = np.array([
        [3, 4, 5],
        [2, 3, 1],
        [9, 2, 7]
        ], dtype=np.float64)


# In[3]:

A = np.array([
        [1e-20, 1],
        [1, 1],
        ])


# In[4]:

n = A.shape[0]

elim_matrices = []

W = A

for i in xrange(n-1):
    M = np.eye(n)
    M[i+1:, i] = -W[i+1:, i]/W[i,i]
    
    elim_matrices.append(M)
    
    W = np.dot(M, W)
    print "--------------------------------------"
    print "column %d" % i
    print "--------------------------------------"
    print "elimination mat:"
    print M
    print "left over:"
    print W


# Out[4]:

#     --------------------------------------
#     column 0
#     --------------------------------------
#     elimination mat:
#     [[  1.00000000e+00   0.00000000e+00]
#      [ -1.00000000e+20   1.00000000e+00]]
#     left over:
#     [[  1.00000000e-20   1.00000000e+00]
#      [  0.00000000e+00  -1.00000000e+20]]
# 

# In[5]:

L = reduce(np.dot, [la.inv(M) for M in elim_matrices])
U = W

print "L"
print L
print "U"
print U


# Out[5]:

#     L
#     [[  1.00000000e+00  -0.00000000e+00]
#      [  1.00000000e+20   1.00000000e+00]]
#     U
#     [[  1.00000000e-20   1.00000000e+00]
#      [  0.00000000e+00  -1.00000000e+20]]
# 

# In[6]:

A_rebuilt = np.dot(L, U)
A_rebuilt


# Out[6]:

#     array([[  1.00000000e-20,   1.00000000e+00],
#            [  1.00000000e+00,   0.00000000e+00]])

# In[7]:

la.norm(A_rebuilt - A)


# Out[7]:

#     1.0

# Why is this a terrible algorithm? What is its cost?
