
# coding: utf-8

# # Matrices for graph traversal

# In[1]:

import numpy as np


# In[182]:


n = 5

# Make a sparsely populated random matrix
A = np.zeros((n, n))

from random import randrange, uniform
for i in range(n*n//2):
    i, j = randrange(n), randrange(n)
    w = round(uniform(0, 1), 1)
    A[i, j] = w
    
A


# For a reason that will become clear in a minute, we need the columns of $A$ to be normalized to sum to 1:

# In[183]:

A_cols = np.sum(A, axis=0)
A_cols[A_cols == 0] = 1
A = A/A_cols

print(A)
print(np.sum(A, axis=0))


# This short piece of code exports the matrix in a format that's readable to the [dot](http://graphviz.org) graph drawing tool.

# In[184]:

def to_dot(A, vec=None):
    lines = ['digraph mygraph { size="2,2";']
    for i in range(n):
        for j in range(n):
            if A[i, j]:
                lines.append("%d -> %d [label=\"%0.1f\"];" % (j, i, A[i, j]))
    if vec is not None:
        for i, vec_i in enumerate(vec):
            assert 0<=vec_i<=1
            lines.append(
                '%d [style="filled", fillcolor="#ff%02xff"];'
                % (i, int(255*(1-vec_i))))
    lines.append("}")
    return "\n".join(lines)


# See?

# In[185]:

print(to_dot(A))


# In[186]:

get_ipython().magic(u'load_ext gvmagic')


# In[187]:

get_ipython().magic(u'dotstr to_dot(A)')


# Another thing we can do is plot distributions on the graph:

# In[188]:

d = np.zeros((n,))
d[4] = 1
get_ipython().magic(u'dotstr to_dot(A, d)')


# Now, how would we model the spread of this distribution across the graph?

# In[189]:

d = np.dot(A, d)
print(np.sum(d))
get_ipython().magic(u'dotstr to_dot(A, d)')


# More questions:
# 
# * How would you find the steady state of this traversal?
# * Any predictions about `np.sum(d)`?
