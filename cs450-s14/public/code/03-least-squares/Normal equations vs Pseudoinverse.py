
# In[1]:

import numpy as np
import numpy.linalg as la


# In[2]:

A = np.random.randn(5, 3)
b = np.random.randn(5)


# Solve $Ax\cong b$ using the normal equations:

# In[4]:

x1 = ...
x1


# Out[4]:

#     array([ 0.23982628, -0.26470109, -0.18776136])

# <!--
# x1 = la.solve(np.dot(A.T, A), np.dot(A.T, b))
# -->
# (Edit this cell for solution.)

# Solve $Ax\cong b$ using the pseudoinverse:

# In[5]:

U, sigma, VT = la.svd(A)
print U
print sigma
print VT


# Out[5]:

#     [[-0.40467972 -0.33714129 -0.63422814  0.20634795  0.52701543]
#      [ 0.42804578  0.47808154  0.02477487 -0.195988    0.74107338]
#      [-0.06483149 -0.50603238  0.15333028 -0.83497764  0.13795024]
#      [ 0.80377855 -0.49127211 -0.27409423  0.1695712  -0.09332588]
#      [-0.0524219  -0.40044568  0.70604748  0.4393941   0.38121514]]
#     [ 2.93921603  2.18290554  1.39834826]
#     [[-0.75141123  0.65519253 -0.07812746]
#      [ 0.62293553  0.74344157  0.24340493]
#      [-0.21756029 -0.13422882  0.96677306]]
# 

# In[6]:

Sigma_inv = np.zeros_like(A.T)
Sigma_inv[:3,:3] = np.diag(1/sigma)
Sigma_inv


# Out[6]:

#     array([[ 0.34022678,  0.        ,  0.        ,  0.        ,  0.        ],
#            [ 0.        ,  0.45810503,  0.        ,  0.        ,  0.        ],
#            [ 0.        ,  0.        ,  0.71512943,  0.        ,  0.        ]])

# In[7]:

pinv = ...
x2 = np.dot(pinv, b)
x2


# Out[7]:

#     array([ 0.23982628, -0.26470109, -0.18776136])

# <!--
# pinv = np.dot(np.dot(VT.T, Sigma_inv), U.T)
# -->
# (Edit this cell for solution.)

# In[8]:

la.norm(x1-x2)


# Out[8]:

#     1.7554167342883506e-16
