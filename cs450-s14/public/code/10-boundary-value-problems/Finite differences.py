
# In[7]:

from __future__ import division

import numpy as np
import matplotlib.pyplot as pt

import scipy.sparse as sps


# We'll solve
# 
# $u''+1000(1+x^2)u=0$ on $(-1,1)$
# 
# with $u(-1)=3$ and $u(1)=-3$.

# In[160]:

n = 500
mesh = np.linspace(-1, 1, n)
h = mesh[1] - mesh[0]


# In[145]:

A = sps.diags(
    [1,-2,1],
    offsets=[-1,0,1], 
    shape=(n, n))

if n < 10:
    print A.todense()


# Need to restrict to middle rows!

# In[153]:

second_deriv = ...

if n < 10:
    print second_deriv.todense()


# <!--
# sps.diags(
#     [1,-2,1],
#     offsets=np.array([-1,0,1])+1,
#     shape=(n-2, n))/h**2
# -->
# (Edit this cell for solution)

# In[154]:

factor = sps.diags(
    [1000*(1 + mesh[1:]**2)],
    offsets=[1],
    shape=(n-2, n))

if n < 10:
    print mesh[1:-1]
    print
    print factor.todense()


# In[155]:

A_int = second_deriv+factor

if n < 10:
    print A_int.todense()


# In[156]:

A = sps.vstack([
    sps.coo_matrix(([1], ([0],[0])), shape=(1, n)),
    A_int,
    sps.coo_matrix(([1], ([0],[n-1])), shape=(1, n)),
    ])
A = sps.csr_matrix(A)

if n < 10:
    print A.todense()


# In[157]:

rhs = np.zeros(n)



# <!--
# rhs[0] = 3
# rhs[-1] = -3
# -->
# (Edit this cell for solution.)

# In[158]:

import scipy.sparse.linalg as sla

sol = sla.spsolve(A, rhs)


# In[159]:

pt.plot(mesh, sol)


# Out[159]:

#     [<matplotlib.lines.Line2D at 0x5d0e610>]

# image file:

# In[136]:



