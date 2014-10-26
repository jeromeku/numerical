
# coding: utf-8

# # Orthogonal Projection

# In[1]:

import numpy as np
import numpy.linalg as la


# In[2]:


# for in-line plots
get_ipython().magic(u'matplotlib inline')

# for plots in a window
# %matplotlib qt

import matplotlib.pyplot as pt
from mpl_toolkits.mplot3d import Axes3D


# Make two random 3D vectors:

# In[3]:

np.random.seed(13)
x = np.random.randn(3)
y = np.random.randn(3)


# Make them orthonormal:

# In[4]:

y = y - y.dot(x)/x.dot(x)*x
x = x/la.norm(x)
y = y/la.norm(y)


# Check:

# In[5]:

print(y.dot(x))
print(la.norm(x))
print(la.norm(y))


# Plot the two vectors:

# In[6]:

fig = pt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim3d([-3, 3])
ax.set_ylim3d([-3, 3])
ax.set_zlim3d([-3, 3])

xy = np.array([x, y]).T
ax.quiver(
   0, 0, 0,
   xy[0], xy[1], xy[2],)


# Make an array with the cornerpoints of a cube:

# In[7]:

points = np.array([
    [-1,-1,-1],
    [-1,-1,1],
    [-1,1,-1],
    [-1,1,1],

    [1,-1,-1],
    [1,-1,1],
    [1,1,-1],
    [1,1,1],
])


# Plot them:

# In[8]:

fig = pt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(points[:,0], points[:, 1], points[:, 2])


# Construct the projection matrix:

# In[9]:

Q = np.array([
   x,y,np.zeros(3)
]).T
print(Q)


# In[10]:

P = Q.dot(Q.T)
print(P)


# Check that $P^2=P$:

# In[11]:

la.norm(P.dot(P)-P)


# Project the points, assign to `proj_points`:

# In[12]:

proj_points = np.einsum("ij,nj->ni", P, points)


# In[13]:

fig = pt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(points[:,0], points[:, 1], points[:, 2])
ax.scatter(proj_points[:,0], proj_points[:, 1], proj_points[:, 2], color="red")

xy = np.array([x, y]).T
ax.quiver(
   0, 0, 0,
   xy[0], xy[1], xy[2],)

