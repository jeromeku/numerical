
# In[1]:

from __future__ import division

import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as pt


# **Mini-Introduction to `sympy`**

# In[2]:

import sympy as sym

# Enable "pretty-printing" in IPython
sym.init_printing()


# In[9]:

x = sym.Symbol("x")

myexpr = (x**2-3)**2
myexpr


# Out[9]:

#             2
#     ⎛ 2    ⎞ 
#     ⎝x  - 3⎠ 

# In[11]:

myexpr.expand()


# Out[11]:

#      4      2    
#     x  - 6⋅x  + 9

# In[10]:

sym.integrate(myexpr, x)


# Out[10]:

#      5             
#     x       3      
#     ── - 2⋅x  + 9⋅x
#     5              

# In[16]:

sym.integrate(myexpr, (x, -1, 1))


# Out[16]:

#     72/5

# **Orthogonal polynomials**

# In[22]:

def inner_product(f1, f2):
    return sym.integrate(f1*f2, (x, -1, 1))


# In[23]:

inner_product(1, 1)


# Out[23]:

#     2

# In[24]:

inner_product(1, x)


# Out[24]:

#     0

# In[63]:

#basis = [1, x, x**2, x**3]
basis = [1, x, x**2, x**3, x**4, x**5]


# In[64]:

# Now for plain old Gram-Schmidt
orth_basis = []

for q in basis:
    for prev_q in orth_basis:
        q = q - inner_product(prev_q, q)*prev_q
    q = q / sym.sqrt(inner_product(q, q))
    
    orth_basis.append(q)


# In[65]:

orth_basis


# Out[65]:

#     ⎡                                                                  ⎛        2 
#     ⎢                    ____ ⎛ 2   1⎞      ____ ⎛ 3   3⋅x⎞        ___ ⎜ 4   6⋅x  
#     ⎢  ___    ___    3⋅╲╱ 10 ⋅⎜x  - ─⎟  5⋅╲╱ 14 ⋅⎜x  - ───⎟  105⋅╲╱ 2 ⋅⎜x  - ──── 
#     ⎢╲╱ 2   ╲╱ 6 ⋅x           ⎝     3⎠           ⎝      5 ⎠            ⎝      7   
#     ⎢─────, ───────, ─────────────────, ───────────────────, ─────────────────────
#     ⎣  2       2             4                   4                       16       
#     
#         ⎞            ⎛         3      ⎞⎤
#       3 ⎟       ____ ⎜ 5   10⋅x    5⋅x⎟⎥
#     + ──⎟  63⋅╲╱ 22 ⋅⎜x  - ───── + ───⎟⎥
#       35⎠            ⎝       9      21⎠⎥
#     ─────, ────────────────────────────⎥
#                         16             ⎦

# (Note: normalization different than in the book.)

# In[66]:

mesh = np.linspace(-1, 1, 100)

pt.figure(figsize=(8,8))
for f in orth_basis:
    f = sym.lambdify(x, f)
    pt.plot(mesh, [f(xi) for xi in mesh])


# Out[66]:

# image file:

# In[ ]:



