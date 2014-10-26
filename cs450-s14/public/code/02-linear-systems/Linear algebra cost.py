
# In[1]:

from __future__ import division

import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as pt

from time import time


# In[2]:

# vector-vector
nlist1 = np.linspace(1e3,1e5,1e3).astype(np.int32)
ntests = 5

time1 = []
for n in nlist1:
    u = np.random.rand(n)
    v = np.random.rand(n)

    t_start = time()
    for test in range(ntests):
        u.dot(v)     
    time1.append((time() - t_start)/ntests)


# In[3]:

# matrix-vector
nlist2 = np.linspace(1e2, 6e3, 20).astype(np.int32)
ntests = 5

time2 = []

for n in nlist2:
    print n,
    A = np.random.rand(n,n)
    u = np.random.rand(n)

    t_start = time()
    for test in range(ntests):
        np.dot(A, u)         
    time2.append((time() - t_start)/ntests)


# Out[3]:

#     100 410 721 1031 1342 1652 1963 2273 2584 2894 3205 3515 3826 4136 4447 4757 5068 5378 5689 6000
# 

# In[4]:

# matrix-matrix
nlist3 = np.linspace(1e2, 2e3, 20).astype(np.int32)

time3 = []
for n in nlist3:
    print n,
    A = np.random.rand(n,n)
    B = np.random.rand(n,n)

    t_start = time()
    np.dot(A, B) 
    time3.append(time() - t_start)


# Out[4]:

#     100 200 300 400 500 600 700 800 900 1000 1100 1200 1300 1400 1500 1600 1700 1800 1900 2000
# 

# In[5]:

# solve
nlist4 = np.linspace(1e2, 2e3, 20).astype(np.int32)

time4 = []
for n in nlist4:
    print n,
    A = np.random.rand(n,n)
    b = np.random.rand(n)

    t_start = time()
    la.solve(A,b)
    time4.append(time() - t_start)


# Out[5]:

#     100 200 300 400 500 600 700 800 900 1000 1100 1200 1300 1400 1500 1600 1700 1800 1900 2000
# 

# In[6]:

# inverse
nlist5 = np.linspace(1e2, 2e3, 12).astype(np.int32)
ntests = 1

time5 = []
for n in nlist5:
    print n,
    A = np.random.rand(n,n)

    t_start = time()
    la.inv(A)
    time5.append(time() - t_start)


# Out[6]:

#     100 272 445 618 790 963 1136 1309 1481 1654 1827 2000
# 

# In[7]:

pt.figure(figsize=(9, 5))

pt.loglog(nlist1, np.array(time1), linewidth=3, label='dot product')
pt.loglog(nlist2, np.array(time2), linewidth=3, label='matrix-vector product')
pt.loglog(nlist3, np.array(time3), linewidth=3, label='matrix-matrix product')
pt.loglog(nlist4, np.array(time4), linewidth=3, label='solve')
pt.loglog(nlist5, np.array(time5), linewidth=3, label='inverse')
pt.legend()
pt.grid()


# Out[7]:

# image file:

# In[ ]:



