
# coding: utf-8

# # Power Iteration and its Variants

# In[2]:

import numpy as np
import numpy.linalg as la


# Let's  prepare a matrix with some random or deliberately chosen eigenvalues:

# In[3]:

n = 6

if 1:
    np.random.seed(70)
    eigvecs = np.random.randn(n, n)
    eigvals = np.sort(np.random.randn(n))
    # Uncomment for near-duplicate largest-magnitude eigenvalue
    # eigvals[1] = eigvals[0] + 1e-3

    A = np.dot(la.solve(eigvecs, np.diag(eigvals)), eigvecs)
    print(eigvals)
    
else:
    # Complex eigenvalues
    np.random.seed(40)
    A = np.random.randn(n, n)
    print(la.eig(A)[0])


# Let's also pick an initial vector:

# In[4]:

x0 = np.random.randn(n)
x0


# ### Power iteration

# In[5]:

x = x0


# Now implement plain power iteration.
# 
# Run the below cell in-place (Ctrl-Enter) many times.

# In[6]:

x = np.dot(A, x)
x


# * What's the problem with this method?
# * Does anything useful come of this?
# * How do we fix it?

# ### Normalized power iteration

# Back to the beginning: Reset to the initial vector.

# In[7]:

x = x0/la.norm(x0)


# Implement normalized power iteration.
# 
# Run this cell in-place (Ctrl-Enter) many times.

# In[8]:

x = np.dot(A, x)
nrm = la.norm(x)
x = x/nrm

print(nrm)
print(x)


# * What do you observe about the norm?
# * What about the sign?
# * What is the vector $x$ now?
# 
# Extensions:
# 
# * Now try the matrix variants above.
# * Suggest a better way of estimating the eigenvalue. [Hint](https://en.wikipedia.org/wiki/Rayleigh_quotient)

# ------
# What if we want the smallest eigenvalue (by magnitude)?
# 
# Once again, reset to the beginning.

# In[9]:

x = x0/la.norm(x0)


# Run the cell below in-place many times.

# In[10]:

x = la.solve(A, x)
nrm = la.norm(x)
x = x/nrm

print(1/nrm)
print(x)


# * What's the computational cost per iteration?
# * Can we make this method search for a specific eigenvalue?
# * What is this [method](https://en.wikipedia.org/wiki/Inverse_iteration) called?

# --------------
# Can we feed an estimate of the current approximate eigenvalue back into the calculation? (Hint: Rayleigh quotient)
# 
# Reset once more.

# In[11]:

x = x0/la.norm(x0)


# Run this cell in-place (Ctrl-Enter) many times.

# In[12]:

sigma = np.dot(x, np.dot(A, x))/np.dot(x, x)
x = la.solve(A-sigma*np.eye(n), x)
x = x/la.norm(x)

print(sigma)
print(x)


# * What's this [method](https://en.wikipedia.org/wiki/Rayleigh_quotient_iteration) called?
# * What's a reasonable stopping criterion?
# * Computational downside of this iteration?
