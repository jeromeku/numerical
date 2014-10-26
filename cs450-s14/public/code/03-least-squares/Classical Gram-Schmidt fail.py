
# In[1]:

import numpy as np
import numpy.linalg as la


# In[2]:

# http://fgiesen.wordpress.com/2013/06/02/modified-gram-schmidt-orthogonalization/

np.set_printoptions(precision=13)

if 0:
    eps = 1e-8

    A = np.array([
        [1,  1,  1],
        [eps,eps,0],
        [eps,0,  eps]
        ])
else:
    A = np.random.randn(3, 3)

A


# Out[2]:

#     array([[ 0.5253995478494,  0.0728870856098, -0.1239374131572],
#            [ 1.4521672418306,  0.2884259189745, -0.9646423363317],
#            [ 1.9552560268667, -0.4250653013151,  0.4126165423083]])

# In[3]:

def test_orthogonality(orthogonal_vectors):
    Q = np.array(orthogonal_vectors)

    print "Q:"
    print Q
    
    print "Q^T Q:"
    QtQ = np.dot(Q.T, Q)
    QtQ[np.abs(QtQ) < 1e-15] = 0
    print QtQ


# In[7]:

orthogonal_vectors = []

for k in range(len(A.T)):
    q0 = q = A[:, k]
    for prev_q in orthogonal_vectors:
        q = q - np.dot(prev_q, q0)*prev_q
    q = q/la.norm(q)
    
    orthogonal_vectors.append(q)

test_orthogonality(orthogonal_vectors)


# Out[7]:

#     Q:
#     [[ 0.2108719041425  0.5828350493858  0.7847524101592]
#      [ 0.2104899290795  0.7568976003929 -0.6187083418506]
#      [ 0.95458212313   -0.2956506853143 -0.0369275300254]]
#     Q^T Q:
#     [[ 1.  0.  0.]
#      [ 0.  1.  0.]
#      [ 0.  0.  1.]]
# 

# <!--
# This code:
# q = q - np.dot(prev_q, q0)*prev_q
# will fail for the second example above.
# -->
# <!--
# Modified Gram-Schmidt uses:
# q = q - np.dot(prev_q, q)*prev_q
# which works.
# -->
# (Edit this cell to see instructions.)

# * Mathematically: fine.
# * Issue with computed solution?
# * Pros/cons of `q0`?
# * Fix?

# In[8]:

my_A = A.copy()
orthogonal_vectors = []

for k in range(len(A.T)):
    q = my_A[:, k]
    q = q/la.norm(q)
    
    for j in range(k+1, len(A.T)):
        ...
        
    orthogonal_vectors.append(q)

test_orthogonality(orthogonal_vectors)


# Out[8]:

#     Q:
#     [[ 0.2108719041425  0.5828350493858  0.7847524101592]
#      [ 0.2104899290795  0.7568976003929 -0.6187083418506]
#      [ 0.95458212313   -0.2956506853143 -0.0369275300254]]
#     Q^T Q:
#     [[ 1.  0.  0.]
#      [ 0.  1.  0.]
#      [ 0.  0.  1.]]
# 

# <!--
# my_A[:, j] -= np.dot(my_A[:, j], q)*q
# -->
# (Edit this cell to see solution.)

# In[ ]:



