
# In[1]:

from __future__ import division

import numpy as np
import numpy.linalg as la


# In[2]:

n = 5

A_dp = np.eye(n) + np.random.randn(n, n)
A_sp = A_dp.astype(np.float32)
x_dp = np.ones(n, np.float64)
b_dp = np.dot(A_dp, x_dp)
b_sp = b_dp.astype(np.float32)


# Can we solve $Ax=b$ to DP (double precision) accuracy using (almost) only SP matrix operations?

# 1) Solve $Ax=b$ in SP and compute DP residual $r_0=b-Ax_0$

# In[3]:

x0_sp = la.solve(A_sp, b_sp)
r0_dp = b_dp - np.dot(A_dp, x0_sp.astype(np.float64))

print la.norm(r0_dp)


# Out[3]:

#     3.12732473678e-07
# 

# 2) Solve $Az_0=r_0$
# 

# In[4]:

z0_sp = la.solve(A_sp, r0_dp.astype(np.float32))

print la.norm(z0_sp)


# Out[4]:

#     2.06476e-07
# 

# 3) Use $x_1 = x_0 + z_0$ as improved solution

# In[5]:

x1_dp = (
      x0_sp.astype(np.float64)
    + z0_sp.astype(np.float64)
    )
print repr(float(x0_sp[0]))
print repr(float(z0_sp[0]))
print repr(float(x1_dp[0]))


# Out[5]:

#     1.0000001192092896
#     -1.192092469182171e-07
#     1.0000000000000426
# 

# In[6]:

la.norm(x0_sp-x_dp)


# Out[6]:

#     2.0647654623614278e-07

# In[7]:

la.norm(x1_dp-x_dp)


# Out[7]:

#     5.1599458938384882e-14

# In[ ]:



