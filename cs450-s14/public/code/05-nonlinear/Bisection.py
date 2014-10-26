
# In[13]:

from __future__ import division

# ^^^ Demo will not work without this.

import numpy as np
import matplotlib.pyplot as pt


# In[14]:

a = 2
b = 6

x = np.linspace(a, b)

def f(x):
    return 1e-2 * np.exp(x) - 2

pt.grid()
pt.plot(x, f(x))


# Out[14]:

#     [<matplotlib.lines.Line2D at 0x312ca90>]

# image file:

# In[49]:

# Run this cell in-place many times. (Ctrl-Enter)

m = a + (b-a)/2

if np.sign(f(a)) == np.sign(f(m)):
    ...
else:
    ...
    
print a, b


# Out[49]:

#     5.29831695557 5.29831886292
# 

# <!--
# if np.sign(f(a)) == np.sign(f(m)):
#     a = m
# else:
#     b = m
# -->
# (Edit this cell for solution.)
