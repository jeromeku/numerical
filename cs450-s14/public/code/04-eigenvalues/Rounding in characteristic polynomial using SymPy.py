
# In[8]:

get_ipython().magic(u'load_ext sympy.interactive.ipythonprinting')

import sympy as sp


# Out[8]:

#     /usr/lib/python2.7/dist-packages/IPython/frontend.py:30: UserWarning: The top-level `frontend` package has been deprecated. All its subpackages have been moved to the top `IPython` level.
#       warn("The top-level `frontend` package has been deprecated. "
# 

# In[9]:

eps = sp.Symbol("epsilon")
lam = sp.Symbol("lambda")


# In[10]:

m = sp.Matrix([[1, eps], [eps, 1]])
m


# Out[10]:

#     ⎡1  ε⎤
#     ⎢    ⎥
#     ⎣ε  1⎦

# In[11]:

m.charpoly(lam)


# Out[11]:

#     PurePoly(lambda**2 - 2*lambda - epsilon**2 + 1, lambda, domain='ZZ[epsilon]')

# Observe the occurrence of $(1-\epsilon^2)$ above.
