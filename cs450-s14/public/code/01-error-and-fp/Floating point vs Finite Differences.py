
# In[1]:

from __future__ import division
import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as pt


# In[2]:

c = 20*2*np.pi

def f(x):
    return np.sin(c*x)

def df(x):
    return c*np.cos(c*x)

n = 2000
x = np.linspace(0, 1, n, endpoint=False).astype(np.float32)

plot(x, f(x))


# Out[2]:

#     [<matplotlib.lines.Line2D at 0x475cb10>]

# image file:

# In[3]:

h_values = []
err_values = []

for n_exp in xrange(5, 24):
    n = 2**n_exp
    h = (1/n)

    x = np.linspace(0, 1, n, endpoint=False).astype(np.float32)

    fx = f(x)
    dfx = df(x)

    dfx_num = (np.roll(fx, -1) - np.roll(fx, 1)) / (2*h)

    err = np.max(np.abs((dfx - dfx_num))) / np.max(np.abs(fx))

    print h, err

    h_values.append(h)
    err_values.append(err)

pt.rc("font", size=16)
pt.title(r"Single precision FD error on $\sin(20\cdot 2\pi)$")
pt.xlabel(r"$h$")
pt.ylabel(r"Rel. Error")
pt.loglog(h_values, err_values)


# Out[3]:

#     0.03125 148.291
#     0.015625 66.5355
#     0.0078125 19.2357
#     0.00390625 4.98669
#     0.001953125 1.25798
#     0.0009765625 0.318611
#     0.00048828125 0.0862198
#     0.000244140625 0.0271683
#     0.0001220703125 0.0188675
#     6.103515625e-05 0.0407867
#     3.0517578125e-05 0.0859985
#     1.52587890625e-05 0.163803
#     7.62939453125e-06 0.336319
#     3.81469726562e-06 0.663834
#     1.90734863281e-06 1.66391
#     9.53674316406e-07 2.33687
#     4.76837158203e-07 5.66476
#     2.38418579102e-07 13.6656
#     1.19209289551e-07 29.6663
# 

#     [<matplotlib.lines.Line2D at 0x4844350>]

# image file:
