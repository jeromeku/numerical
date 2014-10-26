
# In[1]:

import numpy as np
import numpy.linalg as la


# In[2]:

n = 4 # crank up--8 is a good example

nums = np.arange(n).astype(np.float64)
nums


# Out[2]:

#     array([ 0.,  1.,  2.,  3.])

# In[3]:

B = 1 + nums[:, np.newaxis] + nums
B


# Out[3]:

#     array([[ 1.,  2.,  3.,  4.],
#            [ 2.,  3.,  4.,  5.],
#            [ 3.,  4.,  5.,  6.],
#            [ 4.,  5.,  6.,  7.]])

# In[4]:

A = 1/B

from scipy.linalg import hilbert
A2 = hilbert(n)

print "difference: %g" % la.norm(A-A2)
print "cond: %g" % np.linalg.cond(A)


# Out[4]:

#     difference: 0
#     cond: 15513.7
# 

#     /usr/lib/pymodules/python2.7/numpy/oldnumeric/__init__.py:11: ModuleDeprecationWarning: The oldnumeric module will be dropped in Numpy 1.9
#       warnings.warn(_msg, ModuleDeprecationWarning)
# 

# In[5]:

b = np.ones((n,))

b1 = b.copy()
b1[-1] = 2.0/3.0
x1 = la.solve(A, b1)
print "residual of x1: %g"%(la.norm(b - np.dot(A, x1)))

b2 = b.copy()
b2[-1] = 0.667
x2 = la.solve(A, b2)
print "residual of x2: %g"%(la.norm(b - np.dot(A, x2)))

print "rel err in RHS: %g"%(la.norm(b2-b1)/la.norm(b1))
print "rel err in solution: %g"%(la.norm(x2-x1)/la.norm(x1))


# Out[5]:

#     residual of x1: 0.333333
#     residual of x2: 0.333
#     rel err in RHS: 0.000179605
#     rel err in solution: 0.0011524
# 

# In[6]:

x = np.ones((n,))
b = np.dot(A, x)
x3 = la.solve(A,b)
print "residual of x3: %g"%(la.norm(b - np.dot(A, x3)))
print "rel err in solution: %g"%(la.norm(x3-x)/la.norm(x))


# Out[6]:

#     residual of x3: 1.11022e-16
#     rel err in solution: 3.86179e-13
# 

# In[ ]:



