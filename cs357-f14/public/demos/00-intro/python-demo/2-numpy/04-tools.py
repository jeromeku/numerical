
# coding: utf-8

# ### Other tools
# 
# * `numpy.linalg`
# * `scipy`
# * `matplotlib`

# In[1]:

import numpy as np
import matplotlib.pyplot as pt


# In[4]:

x = np.linspace(-10, 10, 100)
pt.plot(x, np.sin(x)+x*0.5)


# In[5]:

pic = np.sin(x)[:,np.newaxis]  * np.cos(x)
pt.imshow(pic)

