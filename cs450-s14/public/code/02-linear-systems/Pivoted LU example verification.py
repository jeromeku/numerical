
# In[1]:

from __future__ import division

import numpy as np


# In[2]:

A = np.array([
              [1,2,1],
              [0,1,3],
              [2,1,0]
              ])


# In[3]:

P1 = np.array([[0,0,1,],[0,1,0],[1,0,0]])
E2 = np.array([[1,0,0,],[0,1,0],[0.5,0,1]])
P3 = np.array([[1,0,0,],[0,0,1],[0,1,0]])
E4 = np.array([[1,0,0,],[0,1,0],[0,02/3,1]])

Afinal = np.array([
              [2,1,0],
              [0,1.5,1],
              [0,0,7/3],
              ])

reduce(np.dot, [P1, E2, P3, E4, Afinal]) - A


# Out[3]:

#     array([[ 0.,  0.,  0.],
#            [ 0.,  0.,  0.],
#            [ 0.,  0.,  0.]])

# In[4]:

reduce(np.dot, [P1, E2, P3, E4])


# Out[4]:

#     array([[ 0.5       ,  1.        ,  0.        ],
#            [ 0.        ,  0.66666667,  1.        ],
#            [ 1.        ,  0.        ,  0.        ]])

# In[ ]:



