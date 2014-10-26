
# In[30]:

from __future__ import division
import numpy as np
import scipy.linalg as la

import matplotlib.pyplot as pt


# Let's solve $u''=-30x^2$ with $u(0)=1$ and $u(1)=-1$.

# In[61]:

n = 50

mesh = np.linspace(0, 1, n)
h = mesh[1] - mesh[0]


# In[136]:

A = ...


# <!--
# (np.eye(n, k=1) + -2*np.eye(n) + np.eye(n, k=-1))/h**2
# A[0] = 0
# A[-1] = 0
# A[0,0] = 1
# A[-1,-1] = 1
# -->
# (edit cell for solution)

# In[145]:

b = -30*mesh**2
b[0] = 1
b[-1] = -1


# In[138]:

x_true = la.solve(A, b)
pt.plot(mesh, x_true)


# Out[138]:

#     [<matplotlib.lines.Line2D at 0xc1d4710>]

# image file:

# ### And now with Jacobi

# In[440]:

x = np.zeros(n)


# In[444]:

x_new = np.empty(n)

for i in xrange(n):
    x_new[i] = b[i]
    for j in xrange(i):
        x_new[i] -= ...
    for j in xrange(i+1, n):
        x_new[i] -= ...
        
    x_new[i] = ...

x = x_new
pt.plot(mesh, x)
pt.plot(mesh, x_true, label="true")
pt.legend()


# Out[444]:

#     <matplotlib.legend.Legend at 0x204e4a10>

# image file:

# <!--
#     for j in xrange(i):
#         x_new[i] -= A[i,j]*x[j]
#     for j in xrange(i+1, n):
#         x_new[i] -= A[i,j]*x[j]
#         
#     x_new[i] = x_new[i] / A[i,i]
# 
# -->
# 
# (Edit cell for solution)

# * Ideas to accelerate this?
# * Multigrid

# ### And now Gauss-Seidel

# In[148]:

x = np.zeros(n)


# In[425]:

x_new = np.empty(n)

for i in xrange(n):
    x_new[i] = b[i]
    for j in xrange(i):
        x_new[i] -= A[i,j]*x_new[j]
    for j in xrange(i+1, n):
        x_new[i] -= A[i,j]*x[j]
        
    x_new[i] = x_new[i] / A[i,i]

x = x_new
pt.plot(mesh, x)
pt.plot(mesh, x_true, label="true")
pt.legend()


# Out[425]:

#     <matplotlib.legend.Legend at 0x1f603ad0>

# image file:

# ### And now Successive Over-Relaxation ("SOR")

# In[426]:

x = np.zeros(n)


# In[439]:

x_new = np.empty(n)

for i in xrange(n):
    x_new[i] = b[i]
    for j in xrange(i):
        x_new[i] -= A[i,j]*x_new[j]
    for j in xrange(i+1, n):
        x_new[i] -= A[i,j]*x[j]
        
    x_new[i] = x_new[i] / A[i,i]

direction = x_new - x
omega = 1.5
x = x + omega*direction

pt.plot(mesh, x)
pt.plot(mesh, x_true, label="true")
pt.legend()
pt.ylim([-1.3, 1.3])


# Out[439]:

#     (-1.3, 1.3)

# image file:

# In[ ]:



