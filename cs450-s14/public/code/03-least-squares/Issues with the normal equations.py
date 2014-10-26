
# In[1]:

import numpy as np
import numpy.linalg as la


# In[2]:

eps = 1e-2  # set to 1e-5, 1e-10

A = np.array([
        [1, 1],
        [eps, 0],
        [0, eps],
        ])

np.set_printoptions(precision=20)
print A
print np.dot(A.T, A)


# Out[2]:

#     [[ 1.                      1.                    ]
#      [ 0.01000000000000000021  0.                    ]
#      [ 0.                      0.01000000000000000021]]
#     [[ 1.00009999999999998899  1.                    ]
#      [ 1.                      1.00009999999999998899]]
# 

# Problem 1 is ...?

# In[3]:

n = 5

A = np.random.randn(5, 5) * 10**-np.linspace(0, -5, n)
la.cond(A)


# Out[3]:

#     60358.505352514032

# In[4]:

la.cond(np.dot(A.T, A))


# Out[4]:

#     3643149168.4817424

# Problem 2 is ...?

# General bound: $\operatorname{cond}(AB)\le \dots$?
