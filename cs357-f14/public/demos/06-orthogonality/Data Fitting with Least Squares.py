
# coding: utf-8

# # Data Fitting with Least Squares

# In[2]:

import numpy as np
import numpy.linalg as npla
import scipy.linalg as spla
import matplotlib.pyplot as pt


# In[3]:

a = 4
b = 2

def f(x):
    return a + b*x

plot_grid = np.linspace(-3, 3, 100)

pt.plot(plot_grid, f(plot_grid))


# In[4]:

npts = 5

np.random.seed(22)
points = np.linspace(-2, 2, npts) + np.random.randn(npts)
values = f(points) + 0.3*np.random.randn(npts)*f(points)

pt.plot(plot_grid, f(plot_grid))
pt.plot(points, values, "o")


# What's the system of equations for $a$ and $b$?

# ---------------
# Now build the system matrix $A$:

# In[5]:

A = np.array([
    1+0*points,
    points,
    ]).T
A


# What's the right-hand side vector?

# -------------
# Now solve the least-squares system:

# In[6]:

Q, R = npla.qr(A, "complete")


# In[7]:

print(A.shape)
print(Q.shape)
print(R.shape)

m, n = A.shape


# Determine $x$. Use `spla.solve_triangular(A, b, lower=False)`.

# In[8]:

x = spla.solve_triangular(R[:n], Q.T.dot(values)[:n], lower=False)


# Recover the computed $a$, $b$:

# In[9]:

a_c, b_c = x


# In[10]:

def f_c(x):
    return a_c + b_c * x

pt.plot(plot_grid, f(plot_grid), label="true")
pt.plot(points, values, "o", label="data")
pt.plot(plot_grid, f_c(plot_grid), label="found")
pt.legend()


# * What should happen if we change the number of data points?
# * What happens if there are lots of outliers?
# * What should happen if we don't add noise?
# * What about a bigger model?
# * What about different functions in the model?
