
# In[ ]:

import numpy as np


# In[1]:

n = 10**4
x = np.abs(np.random.rand(n).astype(np.float32))

sum0 = np.sum(x)

b = x.astype(np.float64)
sum1 = np.sum(b)

# https://en.wikipedia.org/wiki/Kahan_summation_algorithm
sum2 = x[0]
c = np.single(0.0)
for i in range(1,n):
    y = x[i] - c           # assume c is zero.
    t = sum2 + y           # sum2 is big, y is small
    c = (t - sum2) - y     # c should still be zero--but isn't. Why?
    sum2 = t

# large to smallest
d = np.sort(x)
d = d[::-1]
sum3 = d.sum()

# smallest to largest
e = np.sort(x)
sum4 = e.sum()

print "single =         %.20g"%sum0
print "double =         %.20g"%sum1
print "Kahan =          %.20g"%sum2
print "large to small = %.20g"%sum3
print "small to large = %.20g"%sum4


# Out[1]:

#     single =         4993.818359375
#     double =         4993.8146699111312046
#     Kahan =          4993.814453125
#     large to small = 4993.80126953125
#     small to large = 4993.81787109375
# 

# Which of these is going to do well, which poorly?
