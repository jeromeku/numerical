
# In[17]:

from __future__ import division

import numpy
from math import sin, cos


# In[18]:

f = sin
df = cos


# In[19]:

x = 2.3

for k in range(3, 10):
    h = 2**(-k)

    fd1 = (f(x+2*h) - f(x))/(2*h)
    fd2 = (f(x+h) - f(x))/h
    
    richardson = (-1)*fd1 + 2*fd2
    
    true = df(x)
    
    print "Err FD1: %g\tErr FD2: %g\tErr Rich: %g" % (
            abs(true-fd1),
            abs(true-fd2),    
            abs(true-richardson))


# Out[19]:

#     Err FD1: 0.08581	Err FD2: 0.0448122	Err Rich: 0.00381441
#     Err FD1: 0.0448122	Err FD2: 0.022862	Err Rich: 0.000911846
#     Err FD1: 0.022862	Err FD2: 0.0115423	Err Rich: 0.000222501
#     Err FD1: 0.0115423	Err FD2: 0.00579859	Err Rich: 5.49282e-05
#     Err FD1: 0.00579859	Err FD2: 0.00290612	Err Rich: 1.3644e-05
#     Err FD1: 0.00290612	Err FD2: 0.00145476	Err Rich: 3.39995e-06
#     Err FD1: 0.00145476	Err FD2: 0.000727804	Err Rich: 8.48602e-07
# 
