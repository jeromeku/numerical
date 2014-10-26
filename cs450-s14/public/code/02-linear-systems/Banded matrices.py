
# In[1]:

import numpy as np
import scipy.linalg as la


# Out[1]:

#     /usr/lib/pymodules/python2.7/numpy/oldnumeric/__init__.py:11: ModuleDeprecationWarning: The oldnumeric module will be dropped in Numpy 1.9
#       warnings.warn(_msg, ModuleDeprecationWarning)
# 

# In[2]:

n = 6

np.random.seed(0)
A = (
     +         np.diag(np.random.randn(n))
     + np.roll(np.diag(np.random.randn(n)), 1)
     + np.roll(np.diag(np.random.randn(n)), -1)
     )

np.set_printoptions(precision=2)
A


# Out[2]:

#     array([[ 3.22,  0.95,  0.  ,  0.  ,  0.  ,  0.  ],
#            [ 0.12,  0.4 , -0.15,  0.  ,  0.  ,  0.  ],
#            [ 0.  ,  0.44,  0.98, -0.1 ,  0.  ,  0.  ],
#            [ 0.  ,  0.  ,  0.33,  2.24,  0.41,  0.  ],
#            [ 0.  ,  0.  ,  0.  ,  1.49,  1.87,  0.14],
#            [ 0.  ,  0.  ,  0.  ,  0.  , -0.21, -0.22]])

# In[3]:

P, L, U = la.lu(A)


# In[4]:

L


# Out[4]:

#     array([[ 1.  ,  0.  ,  0.  ,  0.  ,  0.  ,  0.  ],
#            [ 0.  ,  1.  ,  0.  ,  0.  ,  0.  ,  0.  ],
#            [ 0.04,  0.82,  1.  ,  0.  ,  0.  ,  0.  ],
#            [ 0.  ,  0.  , -0.35,  1.  ,  0.  ,  0.  ],
#            [ 0.  ,  0.  , -0.  ,  0.66,  1.  ,  0.  ],
#            [ 0.  ,  0.  , -0.  ,  0.  , -0.13,  1.  ]])

# In[5]:

U


# Out[5]:

#     array([[ 3.22,  0.95,  0.  ,  0.  ,  0.  ,  0.  ],
#            [ 0.  ,  0.44,  0.98, -0.1 ,  0.  ,  0.  ],
#            [ 0.  ,  0.  , -0.95,  0.08,  0.  ,  0.  ],
#            [ 0.  ,  0.  ,  0.  ,  2.27,  0.41,  0.  ],
#            [ 0.  ,  0.  ,  0.  ,  0.  ,  1.6 ,  0.14],
#            [ 0.  ,  0.  ,  0.  ,  0.  ,  0.  , -0.2 ]])

# * Observe bandwidth growth.
# * Asymptotic cost of operating on banded matrices? (Mat-vec? Factorization?)
