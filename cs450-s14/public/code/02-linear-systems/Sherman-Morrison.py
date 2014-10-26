
# In[1]:

from __future__ import division

import numpy as np
import scipy.linalg as la


# Out[1]:

#     /usr/lib/pymodules/python2.7/numpy/oldnumeric/__init__.py:11: ModuleDeprecationWarning: The oldnumeric module will be dropped in Numpy 1.9
#       warnings.warn(_msg, ModuleDeprecationWarning)
# 

# In[2]:

n = 5
A = np.random.randn(n, n)
u = np.random.randn(n)
v = np.random.randn(n)

b = np.random.randn(n)

Ahat = A + np.outer(u, v)


# In[3]:

LU, piv = la.lu_factor(A)
print LU
print piv


# Out[3]:

#     [[-1.34619591 -2.40396885  1.34168773 -1.26156511 -0.57082875]
#      [-0.65336062 -4.03983814  1.8543316   0.62740517  0.04102615]
#      [-0.12411925  0.35016924 -3.01157725  1.71780721 -0.10249761]
#      [-0.23344541 -0.05001819  0.08638383 -1.58556641  0.49576436]
#      [-0.01497017  0.02626202 -0.16798668 -0.09674568  2.0533571 ]]
#     [1 4 2 4 4]
# 

# In[4]:

def solveA(b):
    return la.lu_solve((LU, piv), b)

la.norm(np.dot(A, solveA(b)) - b)


# Out[4]:

#     4.002966042486721e-16

# $$(A+uv^T)^{-1} = A^{-1} - {A^{-1}uv^T A^{-1} \over 1 + v^T A^{-1}u}$$

# In[9]:

xhat = la.solve(Ahat, b)

xhat2 = ...

print la.norm(xhat - xhat2)


# Out[9]:

#     1.57009245868e-16
# 

# <!--
# xhat2 = solveA(b) - solveA(u)*np.dot(v, solveA(b))/(1+np.dot(v, solveA(u)))
# -->
# (Edit this cell to see solution.)

# What's the cost of the Sherman-Morrison procedure?
