
# In[1]:

from __future__ import division
import numpy as np
import matplotlib.pyplot as pt


# In[3]:

n = 64
omega = exp(2*pi*1j*1./n)

opowers = omega**[1,2,3,4,5]

xlim([-1.2, 1.2]); xlabel("Real")
ylim([-1.2, 1.2]); ylabel("Imaginary")
grid()
gca().set_aspect("equal")
plot(opowers.real, opowers.imag, "o")


# Out[3]:

#     [<matplotlib.lines.Line2D at 0x3d13b50>]

# image file:

# In[4]:

opowers = omega**arange(n)
plot(opowers.imag)


# Out[4]:

#     [<matplotlib.lines.Line2D at 0x42e71d0>]

# image file:

# In[5]:

plot((opowers**2).imag)


# Out[5]:

#     [<matplotlib.lines.Line2D at 0x4478b50>]

# image file:

# In[6]:

plot((opowers**5).imag)


# Out[6]:

#     [<matplotlib.lines.Line2D at 0x477da90>]

# image file:

# In[7]:

dot(opowers, opowers**3)


# Out[7]:

#     (-1.5210055437364645e-14-3.8691272408186705e-14j)

# In[8]:

dot(opowers**17, opowers**3)


# Out[8]:

#     (-5.7620574978045624e-14-3.8857805861880479e-15j)

# In[9]:

dot(opowers**3, opowers**3)


# Out[9]:

#     (-2.042810365310288e-14-3.0975222387041867e-14j)

# In[10]:

dot((opowers**3).conj(), opowers**3)


# Out[10]:

#     (64.000000000000668+0j)

# In[11]:

vdot(opowers**3, opowers**3)


# Out[11]:

#     (64.000000000000668+0j)

# # Now in matrix form

# In[12]:

mat = np.vstack(
   [opowers**0, opowers**1, opowers**2,
   opowers**3, opowers**4, opowers**5]).T
mat.shape


# Out[12]:

#     (64, 6)

# In[13]:

plot(np.dot(mat, [0, 1, 0,0, 0.3, 0.7]))


# Out[13]:

#     /usr/lib/python2.7/dist-packages/numpy/core/numeric.py:460: ComplexWarning: Casting complex values to real discards the imaginary part
#       return array(a, dtype, copy=False, order=order)
# 

#     [<matplotlib.lines.Line2D at 0x4986090>]

# image file:

# In[14]:

mat = opowers[:, newaxis] ** arange(n)
mat.shape


# Out[14]:

#     (64, 64)

# In[15]:

weights = zeros(n)
weights[1] = 1
weights[4] = 0.3
weights[5] = 0.7
plot(dot(mat, weights))


# Out[15]:

#     [<matplotlib.lines.Line2D at 0x4bce2d0>]

# image file:

# # Inverse of `mat`?

# In[16]:

dot(mat[:,3].conj(), mat[3])


# Out[16]:

#     (64.000000000000455+9.7574726076743483e-14j)

# In[ ]:



