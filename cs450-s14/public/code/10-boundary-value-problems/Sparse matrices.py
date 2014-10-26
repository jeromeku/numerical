
# In[49]:

from __future__ import division

import numpy as np
import matplotlib.pyplot as pt

import scipy.sparse as sps


# #### Building a sparse matrix

# In[50]:

data = [5, 6, 7]
rows = [1, 1, 2]
columns = [2, 4, 6]

A = sps.coo_matrix(
        (data, (rows, columns)),
        shape=(10, 10), dtype=np.float64)
A


# Out[50]:

#     <10x10 sparse matrix of type '<type 'numpy.float64'>'
#     	with 3 stored elements in COOrdinate format>

# In[51]:

A.todense()


# Out[51]:

#     matrix([[ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
#             [ 0.,  0.,  5.,  0.,  6.,  0.,  0.,  0.,  0.,  0.],
#             [ 0.,  0.,  0.,  0.,  0.,  0.,  7.,  0.,  0.,  0.],
#             [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
#             [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
#             [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
#             [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
#             [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
#             [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.],
#             [ 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.]])

# In[52]:

A.nnz


# Out[52]:

#     3

# In[53]:

pt.spy(A)


# Out[53]:

#     <matplotlib.lines.Line2D at 0x333c8d0>

# image file:

# For a COO matrix, the juicy attributes are `data`, `row`, and `col`.

# In[ ]:




# Coordinate format is not the only format. For Compressed Sparse Row, look in `data`, `indptr`, and `indices`.

# In[47]:




# #### How about performance?

# In[43]:

fill_percent = 5

size = 1000
nentries = size**2 * fill_percent // 100

data = np.random.randn(nentries)
rows = (np.random.rand(nentries)*size).astype(np.int32)
columns = (np.random.rand(nentries)*size).astype(np.int32)

B_coo = sps.coo_matrix(
        (data, (rows, columns)),
        shape=(size, size), dtype=np.float64)

B_csr = sps.csr_matrix(B_coo)

B_dense = B_coo.todense()


# In[48]:

vec = np.random.randn(size)

from time import time
start = time()

for i in xrange(200):
    B_dense.dot(vec)
    
print "time: %g" % (time() - start)


# Out[48]:

#     time: 0.282632
# 

# In[ ]:



