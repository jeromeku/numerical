
# In[20]:

from __future__ import division

import numpy
import numpy.linalg as la


# In[21]:

nodes = [0, 1]
#nodes = [0, 0.5, 1]
#nodes = [3, 3.5, 4]
#nodes = [0, 1, 2]
#nodes = np.linspace(0, 1, 12)

max_degree = len(nodes)-1


# In[22]:

nodes = np.array(nodes)
powers = np.arange(max_degree+1)

Vt = nodes ** powers.reshape(-1, 1)

a = nodes[0]
b = nodes[-1]
rhs = 1/(powers+1) * (b**(powers+1) - a**(powers+1))

if len(nodes) <= 4:
    print Vt


# Out[22]:

#     [[1 1]
#      [0 1]]
# 

# In[23]:

weights = la.solve(Vt, rhs)

print weights


# Out[23]:

#     [ 0.5  0.5]
# 

# In[25]:

for i in range(len(nodes) + 1):
    approx = np.dot(weights, nodes**i)
    true = 1/(i+1)*(b**(i+1) - a**(i+1))
    
    print "Error at degree %d: %g" % (i, approx-true)


# Out[25]:

#     Error at degree 0: 0
#     Error at degree 1: 0
#     Error at degree 2: 0.166667
# 

# In[24]:



