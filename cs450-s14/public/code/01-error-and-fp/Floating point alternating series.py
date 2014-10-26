
# In[1]:

import numpy as np
import matplotlib.pyplot as pt


# In[2]:

a = 0.0
x = 1e1 # flip sign
true_f = np.exp(x)
e = []

for i in range(0, 10): # crank up
    d = np.prod(
            np.arange(1, i+1).astype(np.float))
    
    # series for exp
    a += x**i / d

    print a, np.exp(x), x**i / d
    
    e.append(abs(true_f-a)/true_f)


# Out[2]:

#     1.0 22026.4657948 1.0
#     11.0 22026.4657948 10.0
#     61.0 22026.4657948 50.0
#     227.666666667 22026.4657948 166.666666667
#     644.333333333 22026.4657948 416.666666667
#     1477.66666667 22026.4657948 833.333333333
#     2866.55555556 22026.4657948 1388.88888889
#     4850.68253968 22026.4657948 1984.12698413
#     7330.84126984 22026.4657948 2480.15873016
#     10086.5731922 22026.4657948 2755.7319224
# 

# In[3]:

pt.semilogy(e)


# Out[3]:

#     [<matplotlib.lines.Line2D at 0x2d08490>]

# image file:

# In[3]:



