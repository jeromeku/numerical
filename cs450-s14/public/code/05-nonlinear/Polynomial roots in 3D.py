
# In[ ]:

import numpy as np

import mayavi.mlab as mlab


# Consider the three equations:
# 
# * $y=x^2+\delta$
# * $z=x^2-\delta$
# * $y=z^2+\delta$

# In[ ]:

delta = 0.5


# In[ ]:

res = 200j

x, z = np.mgrid[-3:3:res,-3:3:res]
y = x**2 + delta

mlab.mesh(x, y, z)

if 1:
    y, x = np.mgrid[-3:3:res,-3:3:res]
    z = x**2 - delta
    
    mlab.mesh(x, y, z)

if 1:
    x, z = np.mgrid[-3:3:res,-3:3:res]
    y = z**2 + delta
    
    mlab.mesh(x, y, z)


# In[ ]:

mlab.orientation_axes()
mlab.show()

