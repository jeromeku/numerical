
# In[1]:

import numpy as np


# In[2]:

a = np.random.randn(3)
a


# Out[2]:

#     array([ 0.4951792 , -1.03530404,  1.70427995])

# Let's zero out $a_2$:

# In[3]:

G = np.zeros((3, 3))

c = a[0]/sqrt(a[0]**2 + a[1]**2)
s = a[1]/sqrt(a[0]**2 + a[1]**2)

G[:2,:2] = np.array([
        [c, s],
        [-s, c]
        ])
G


# Out[3]:

#     array([[ 0.43147946, -0.90212276,  0.        ],
#            [ 0.90212276,  0.43147946,  0.        ],
#            [ 0.        ,  0.        ,  0.        ]])

# Anything wrong with $G$?

# <!--
# G zeroes out the last component.
# -->
# (Edit this cell for solution.)

# In[4]:

np.dot(G, a)


# Out[4]:

#     array([ 1.14763099,  0.        ,  0.        ])

# Observations?
