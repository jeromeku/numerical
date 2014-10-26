
# In[56]:

import numpy as np
import scipy as sp
import matplotlib.pyplot as pt

import scipy.optimize as opt


# In[57]:

def f(x):
    return x**3 - x +1

def df(x):
    return 3*x**2 - 1

xmesh = np.linspace(-2, 2, 100)
pt.ylim([-3, 10])
pt.plot(xmesh, f(xmesh))


# Out[57]:

#     [<matplotlib.lines.Line2D at 0x48d41d0>]

# image file:

# In[86]:

iterates = [2, 1.5]

x_exact =  opt.fsolve(f, -1)
print "Exact:", x_exact

e = list(np.abs(iterates-x_exact))
print "Errors:", e


# Out[86]:

#     Exact: [-1.32471796]
#     Errors: [3.3247179572447534, 2.8247179572447534]
# 

# In[87]:

# Evaluate this cell many times in-place (using Ctrl-Enter)

xlast, x = iterates[-2:] # grab last two iterates

slope = df(x)                             # Newton's method
#slope = ( (f(x)-f(xlast)) / (x-xlast) )   # Secant method

pt.plot(xmesh, f(xmesh))
pt.plot(xmesh, f(x) + slope*(xmesh-x))
pt.plot(x, f(x), "o")
pt.ylim([-3, 10])
pt.axhline(0, color="black")

# Compute approximate root
xnew = x - f(x) / slope
iterates.append(xnew)
print xnew

e.append(abs(xnew - x_exact))


# Out[87]:

#     1.0
# 

# image file:

# ### Evaluate convergence history

# In[85]:

for i, x in enumerate(iterates):
    if i == 0:
        continue
    print "%3d %10g %10g | %10g %10g %10g"%(
                        i, x, e[i], 
                        e[i]/e[i-1],
                        e[i]/e[i-1]**2,
                        e[i]/e[i-1]**1.62)


# Out[85]:

#       1        1.5    2.82472 |   0.849611   0.255544   0.403397
#       2          1    2.32472 |   0.822991   0.291353   0.432305
#       3        0.5    1.82472 |    0.78492   0.337641   0.465239
#       4          3    4.32472 |    2.37007    1.29887    1.63238
#       5    2.03846    3.36318 |   0.777664   0.179819   0.313688
#       6    1.39028      2.715 |   0.807272   0.240032    0.38057
#       7   0.911612    2.23633 |   0.823694   0.303386   0.443434
#       8   0.345028    1.66975 |   0.746646   0.333871   0.453317
#       9    1.42775    2.75247 |    1.64844   0.987237    1.19958
#      10   0.942418    2.26714 |   0.823674   0.299249    0.43967
#      11   0.404949    1.72967 |   0.762931   0.336517   0.459292
#      12     1.7069    3.03162 |    1.75272    1.01333    1.24789
#      13    1.15576    2.48047 |     0.8182   0.269889   0.411359
#      14   0.694192    2.01891 |   0.813921   0.328131   0.463416
#      15  -0.742494   0.582224 |   0.288385   0.142842   0.186552
#      16    -2.7813    1.45658 |    2.50175    4.29689    3.49855
#      17   -1.98273   0.658007 |   0.451749   0.310144   0.357792
#      18   -1.53693   0.212209 |   0.322503   0.490121   0.418053
#      19   -1.35726  0.0325445 |    0.15336   0.722684   0.400977
#      20   -1.32566 0.000945137 |  0.0290414   0.892358   0.242818
#      21   -1.32472 8.31371e-07 | 0.000879629    0.93069  0.0659923
#      22   -1.32472 6.37046e-13 | 7.6626e-07   0.921683 0.00450924
#      23   -1.32472 7.10543e-15 |  0.0111537 1.75085e+10     406288
#      24   -1.32472 7.10543e-15 |          1 1.40737e+14 5.91581e+08
#      25   -1.32472 7.10543e-15 |          1 1.40737e+14 5.91581e+08
#      26   -1.32472 7.10543e-15 |          1 1.40737e+14 5.91581e+08
#      27   -1.32472 7.10543e-15 |          1 1.40737e+14 5.91581e+08
# 

# In[ ]:



