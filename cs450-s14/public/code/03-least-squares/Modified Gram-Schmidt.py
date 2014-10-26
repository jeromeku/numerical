
# To illustrate that Modified Gram-Schmidt works, consider a $2\times 2$ matrix as in your example. I'll use sympy to make the algebra less tedious. You can make it a $4\times 3$ simply by adjusting the parameters.

# In[11]:

import sympy as sp
import sympy.matrices

from sympy import init_printing
init_printing()


# In[18]:

num_rows = 2
num_cols = 2

a = sp.Matrix([[
        # Uncomment this row for symbolic math, as shown below:
        "a%d%d" % (row, col)
        
        # Uncomment this row for numerical math, as shown below:
        row+col
        
        for col in xrange(num_cols)]
        for row in xrange(num_rows)])
a


# Out[18]:

#     ⎡a₀₀  a₀₁⎤
#     ⎢        ⎥
#     ⎣a₁₀  a₁₁⎦

# In[19]:

a[:,0]


# Out[19]:

#     ⎡a₀₀⎤
#     ⎢   ⎥
#     ⎣a₁₀⎦

# In[20]:

from sympy.matrices import zeros

r = zeros(num_rows, num_cols)
q = zeros(num_rows, num_cols)
r


# Out[20]:

#     ⎡0  0⎤
#     ⎢    ⎥
#     ⎣0  0⎦

# What follows is just Algorithm 3.3 from the book, typed up:

# In[21]:

a_mod = a.copy()

for k in range(num_cols):
    ak = a_mod[:,k]
    r[k,k] = ak.norm()
    q[:,k ] = ak/ak.norm()
    for j in range(k+1, num_cols):
        r[k,j] = q[:,k].dot(a[:,j])
        a_mod[:,j] = a_mod[:,j] - r[k,j] * q[:,k]


# In[22]:

print sp.simplify(q[:,0].norm())
print sp.simplify(q[:,1].norm())


# Out[22]:

#     1
#     1
# 

# In[24]:

q


# Out[24]:

#     ⎡                                                                   ⎛      a₀₀
#     ⎢                                                               a₀₀⋅⎜─────────
#     ⎢                                                                   ⎜   ______
#     ⎢                                                                   ⎜  ╱      
#     ⎢                                                                   ⎝╲╱  │a₀₀│
#     ⎢                                                             - ──────────────
#     ⎢                                                                             
#     ⎢                                                                             
#     ⎢        a₀₀                                                                  
#     ⎢────────────────────  ───────────────────────────────────────────────────────
#     ⎢   _________________             ____________________________________________
#     ⎢  ╱      2        2             ╱                                            
#     ⎢╲╱  │a₀₀│  + │a₁₀│             ╱  │      ⎛      a₀₀⋅a₀₁                a₁₀⋅a₁
#     ⎢                              ╱   │  a₀₀⋅⎜──────────────────── + ────────────
#     ⎢                             ╱    │      ⎜   _________________      _________
#     ⎢                            ╱     │      ⎜  ╱      2        2      ╱      2  
#     ⎢                           ╱      │      ⎝╲╱  │a₀₀│  + │a₁₀│     ╲╱  │a₀₀│  +
#     ⎢                          ╱       │- ────────────────────────────────────────
#     ⎢                         ╱        │                    _________________     
#     ⎢                        ╱         │                   ╱      2        2      
#     ⎢                      ╲╱          │                 ╲╱  │a₀₀│  + │a₁₀│       
#     ⎢                                                                             
#     ⎢                                                                   ⎛      a₀₀
#     ⎢                                                               a₁₀⋅⎜─────────
#     ⎢                                                                   ⎜   ______
#     ⎢                                                                   ⎜  ╱      
#     ⎢                                                                   ⎝╲╱  │a₀₀│
#     ⎢                                                             - ──────────────
#     ⎢                                                                             
#     ⎢                                                                             
#     ⎢        a₁₀                                                                  
#     ⎢────────────────────  ───────────────────────────────────────────────────────
#     ⎢   _________________             ____________________________________________
#     ⎢  ╱      2        2             ╱                                            
#     ⎢╲╱  │a₀₀│  + │a₁₀│             ╱  │      ⎛      a₀₀⋅a₀₁                a₁₀⋅a₁
#     ⎢                              ╱   │  a₀₀⋅⎜──────────────────── + ────────────
#     ⎢                             ╱    │      ⎜   _________________      _________
#     ⎢                            ╱     │      ⎜  ╱      2        2      ╱      2  
#     ⎢                           ╱      │      ⎝╲╱  │a₀₀│  + │a₁₀│     ╲╱  │a₀₀│  +
#     ⎢                          ╱       │- ────────────────────────────────────────
#     ⎢                         ╱        │                    _________________     
#     ⎢                        ╱         │                   ╱      2        2      
#     ⎣                      ╲╱          │                 ╲╱  │a₀₀│  + │a₁₀│       
#     
#     ⋅a₀₁                a₁₀⋅a₁₁       ⎞                                           
#     ─────────── + ────────────────────⎟                                           
#     ___________      _________________⎟                                           
#     2        2      ╱      2        2 ⎟                                           
#       + │a₁₀│     ╲╱  │a₀₀│  + │a₁₀│  ⎠                                           
#     ─────────────────────────────────── + a₀₁                                     
#         _________________                                                         
#        ╱      2        2                                                          
#      ╲╱  │a₀₀│  + │a₁₀│                                                           
#     ──────────────────────────────────────────────────────────────────────────────
#     ______________________________________________________________________________
#                     2                                                             
#     ₁       ⎞      │    │      ⎛      a₀₀⋅a₀₁                a₁₀⋅a₁₁       ⎞      
#     ────────⎟      │    │  a₁₀⋅⎜──────────────────── + ────────────────────⎟      
#     ________⎟      │    │      ⎜   _________________      _________________⎟      
#           2 ⎟      │    │      ⎜  ╱      2        2      ╱      2        2 ⎟      
#      │a₁₀│  ⎠      │    │      ⎝╲╱  │a₀₀│  + │a₁₀│     ╲╱  │a₀₀│  + │a₁₀│  ⎠      
#     ───────── + a₀₁│  + │- ───────────────────────────────────────────────── + a₁₁
#                    │    │                    _________________                    
#                    │    │                   ╱      2        2                     
#                    │    │                 ╲╱  │a₀₀│  + │a₁₀│                      
#                                                                                   
#     ⋅a₀₁                a₁₀⋅a₁₁       ⎞                                           
#     ─────────── + ────────────────────⎟                                           
#     ___________      _________________⎟                                           
#     2        2      ╱      2        2 ⎟                                           
#       + │a₁₀│     ╲╱  │a₀₀│  + │a₁₀│  ⎠                                           
#     ─────────────────────────────────── + a₁₁                                     
#         _________________                                                         
#        ╱      2        2                                                          
#      ╲╱  │a₀₀│  + │a₁₀│                                                           
#     ──────────────────────────────────────────────────────────────────────────────
#     ______________________________________________________________________________
#                     2                                                             
#     ₁       ⎞      │    │      ⎛      a₀₀⋅a₀₁                a₁₀⋅a₁₁       ⎞      
#     ────────⎟      │    │  a₁₀⋅⎜──────────────────── + ────────────────────⎟      
#     ________⎟      │    │      ⎜   _________________      _________________⎟      
#           2 ⎟      │    │      ⎜  ╱      2        2      ╱      2        2 ⎟      
#      │a₁₀│  ⎠      │    │      ⎝╲╱  │a₀₀│  + │a₁₀│     ╲╱  │a₀₀│  + │a₁₀│  ⎠      
#     ───────── + a₀₁│  + │- ───────────────────────────────────────────────── + a₁₁
#                    │    │                    _________________                    
#                    │    │                   ╱      2        2                     
#                    │    │                 ╲╱  │a₀₀│  + │a₁₀│                      
#     
#        ⎤
#        ⎥
#        ⎥
#        ⎥
#        ⎥
#        ⎥
#        ⎥
#        ⎥
#        ⎥
#     ───⎥
#     ___⎥
#      2 ⎥
#     │  ⎥
#     │  ⎥
#     │  ⎥
#     │  ⎥
#     │  ⎥
#     │  ⎥
#     │  ⎥
#     │  ⎥
#     │  ⎥
#        ⎥
#        ⎥
#        ⎥
#        ⎥
#        ⎥
#        ⎥
#        ⎥
#        ⎥
#        ⎥
#        ⎥
#     ───⎥
#     ___⎥
#      2 ⎥
#     │  ⎥
#     │  ⎥
#     │  ⎥
#     │  ⎥
#     │  ⎥
#     │  ⎥
#     │  ⎥
#     │  ⎥
#     │  ⎦

# In[25]:

r


# Out[25]:

#     ⎡   _________________                                                         
#     ⎢  ╱      2        2                                                       a₀₀
#     ⎢╲╱  │a₀₀│  + │a₁₀│                                                  ─────────
#     ⎢                                                                       ______
#     ⎢                                                                      ╱      
#     ⎢                                                                    ╲╱  │a₀₀│
#     ⎢                                                                             
#     ⎢                                 ____________________________________________
#     ⎢                                ╱                                            
#     ⎢                               ╱  │      ⎛      a₀₀⋅a₀₁                a₁₀⋅a₁
#     ⎢                              ╱   │  a₀₀⋅⎜──────────────────── + ────────────
#     ⎢                             ╱    │      ⎜   _________________      _________
#     ⎢                            ╱     │      ⎜  ╱      2        2      ╱      2  
#     ⎢                           ╱      │      ⎝╲╱  │a₀₀│  + │a₁₀│     ╲╱  │a₀₀│  +
#     ⎢         0                ╱       │- ────────────────────────────────────────
#     ⎢                         ╱        │                    _________________     
#     ⎢                        ╱         │                   ╱      2        2      
#     ⎣                      ╲╱          │                 ╲╱  │a₀₀│  + │a₁₀│       
#     
#                                                                                   
#     ⋅a₀₁                a₁₀⋅a₁₁                                                   
#     ─────────── + ────────────────────                                            
#     ___________      _________________                                            
#     2        2      ╱      2        2                                             
#       + │a₁₀│     ╲╱  │a₀₀│  + │a₁₀│                                              
#                                                                                   
#     ______________________________________________________________________________
#                     2                                                             
#     ₁       ⎞      │    │      ⎛      a₀₀⋅a₀₁                a₁₀⋅a₁₁       ⎞      
#     ────────⎟      │    │  a₁₀⋅⎜──────────────────── + ────────────────────⎟      
#     ________⎟      │    │      ⎜   _________________      _________________⎟      
#           2 ⎟      │    │      ⎜  ╱      2        2      ╱      2        2 ⎟      
#      │a₁₀│  ⎠      │    │      ⎝╲╱  │a₀₀│  + │a₁₀│     ╲╱  │a₀₀│  + │a₁₀│  ⎠      
#     ───────── + a₀₁│  + │- ───────────────────────────────────────────────── + a₁₁
#                    │    │                    _________________                    
#                    │    │                   ╱      2        2                     
#                    │    │                 ╲╱  │a₀₀│  + │a₁₀│                      
#     
#        ⎤
#        ⎥
#        ⎥
#        ⎥
#        ⎥
#        ⎥
#        ⎥
#     ___⎥
#      2 ⎥
#     │  ⎥
#     │  ⎥
#     │  ⎥
#     │  ⎥
#     │  ⎥
#     │  ⎥
#     │  ⎥
#     │  ⎥
#     │  ⎦

# In[23]:

sp.simplify(q * r - a)


# Out[23]:

#     ⎡0  0⎤
#     ⎢    ⎥
#     ⎣0  0⎦