
# In[1]:

import numpy as np
import numpy.linalg as la


# In[2]:

alpha = 3
beta = 2
gamma = 2

def f(x):
    return alpha*x**2 + beta*x + gamma

plot_grid = np.linspace(-3, 3, 100)

plot(plot_grid, f(plot_grid))


# Out[2]:

#     [<matplotlib.lines.Line2D at 0x4231890>]

# image file:

# In[3]:

npts = 5

np.random.seed(22)
points = np.linspace(-2, 2, npts) + np.random.randn(npts)
values = f(points) + 0.3*np.random.randn(npts)*f(points)

plot(plot_grid, f(plot_grid))
plot(points, values, "o")


# Out[3]:

#     [<matplotlib.lines.Line2D at 0x409be50>]

# image file:

# In[4]:

A = np.array([
    np.ones(npts),
    points,
    points**2
    ]).T
print A


# Out[4]:

#     [[ 1.         -2.09194992  4.37625447]
#      [ 1.         -2.46335065  6.06809644]
#      [ 1.          1.08179168  1.17027324]
#      [ 1.          0.76067483  0.5786262 ]
#      [ 1.          1.50887086  2.27669128]]
# 

# In[6]:

x = ...
x


# Out[6]:

#     array([ 0.13178048,  1.84869187,  3.45132033])

# <!--
# x = la.solve(np.dot(A.T, A), np.dot(A.T, values))
# -->
# (Edit this cell for solution.)

# In[7]:

... = x

def f_c(x):
    return alpha_c*x**2 + beta_c*x + gamma_c

plot(plot_grid, f(plot_grid), label="true")
plot(points, values, "o", label="data")
plot(plot_grid, f_c(plot_grid), label="found")
legend()


# Out[7]:

#     <matplotlib.legend.Legend at 0x4773dd0>

# image file:

# <!--
# gamma_c, beta_c, alpha_c = x
# -->
# (Edit this cell for solution.)
