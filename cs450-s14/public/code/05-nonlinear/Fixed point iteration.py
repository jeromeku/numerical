
# In[1]:

from __future__ import division

import numpy as np
import matplotlib.pyplot as pt


# In[2]:

x = np.linspace(0, 4.5, 200)

def f(x):
    return x**2 - x - 2

pt.plot(x, f(x))
pt.grid()


# Out[2]:

# image file:

# Actual roots: $2$ and $-1$

# In[3]:

def fp1(x): return x**2-2
def fp2(x): return np.sqrt(x+2)
def fp3(x): return 1+2/x
def fp4(x): return (x**2+2)/(2*x-1)

fixed_point_functions = [fp1, fp2, fp3, fp4]


# In[4]:

for fp in fixed_point_functions:
    plot(x, fp(x), label=fp.__name__)
pt.ylim([0, 3])
pt.legend(loc="best")


# Out[4]:

#     -c:3: RuntimeWarning: divide by zero encountered in true_divide
# 

#     <matplotlib.legend.Legend at 0x471db10>

# image file:

# Common feature?

# In[5]:

for fp in fixed_point_functions:
    ...


# Out[5]:

#     2
#     2.0
#     2.0
#     2.0
# 

# <!--
# for fp in fixed_point_functions:
#     print fp(2)
# All functions have 2 as a fixed point.
# -->
# (Edit this cell for solution.)

# In[6]:

z = 2.1; fp = fp1
#z = 1; fp = fp2
#z = 1; fp = fp3
#z = 1; fp = fp4

n_iterations = 4

pt.figure(figsize=(8,8))
pt.plot(x, fp(x))
pt.plot(x, x, "--")
pt.gca().set_aspect("equal")
pt.ylim([-0.5, 4])

for i in range(n_iterations):
    z_new = fp(z)
    
    pt.arrow(z, z, 0, z_new-z)
    pt.arrow(z, z_new, z_new-z, 0)
    
    z = z_new
    print z


# Out[6]:

#     2.41
#     3.8081
#     12.50162561
#     154.290642893
# 

# image file:

# In[ ]:



