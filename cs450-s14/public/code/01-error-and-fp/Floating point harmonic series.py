
# In[1]:

from __future__ import division


# In[2]:

n = int(0)

float_type = np.float32

my_sum = float_type(0)

while True:
    n += 1
    last_sum = my_sum
    my_sum += float_type(1 / n)
    
    if n % 200000 == 0:
        print "1/n = %g, sum0 = %g"%(1.0/n, my_sum)
        
    if last_sum == my_sum:
        print "Stopped changing at %d" % n
        break


# Out[2]:

#     1/n = 5e-06, sum0 = 12.7828
#     1/n = 2.5e-06, sum0 = 13.4814
#     1/n = 1.66667e-06, sum0 = 13.8814
#     1/n = 1.25e-06, sum0 = 14.1666
#     1/n = 1e-06, sum0 = 14.3574
#     1/n = 8.33333e-07, sum0 = 14.5481
#     1/n = 7.14286e-07, sum0 = 14.7388
#     1/n = 6.25e-07, sum0 = 14.9296
#     1/n = 5.55556e-07, sum0 = 15.1203
#     1/n = 5e-07, sum0 = 15.311
#     Stopped changing at 2097152
# 

# In[2]:



