
# In[4]:

from __future__ import division

import numpy as np
import matplotlib.pyplot as pt


# In[5]:

def rk4_step(y, t, h, f):
    k1 = f(t, y)
    k2 = f(t+h/2, y + h/2*k1)
    k3 = f(t+h/2, y + h/2*k2)
    k4 = f(t+h, y + h*k3)
    return y + h/6*(k1 + 2*k2 + 2*k3 + k4)


# Consider the second-order harmonic oscillator
# 
# $$u''=-u$$
# 
# with initial conditions $u(0) = 1$ and $u'(0)=0$.

# In[6]:

def f(t, y):
    u, up = y
    return np.array([up, -u])


# In[19]:

times = [0]
y_values = [np.array([1,0])]

h = 0.5
t_end = 800

while times[-1] < t_end:
    y_values.append(rk4_step(y_values[-1], times[-1], h, f))
    times.append(times[-1]+h)


# In[23]:

y_values = np.array(y_values)

pt.figure(figsize=(15,5))
pt.plot(times, y_values[:, 0])


# Out[23]:

#     [<matplotlib.lines.Line2D at 0x4c7f210>]

# image file:

# In[ ]:



