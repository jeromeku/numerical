
# In[1]:

from __future__ import division
import numpy as np
import matplotlib.pyplot as pt


# In[2]:

from simple_audio import play


# In[3]:

sample_rate = 44100
count = (sample_rate//1024) * 1024


# In[4]:

t = np.linspace(0, 1, sample_rate)[:count]


# In[5]:

x = np.sin(440*2*np.pi*t)
#x = np.sin(880*2*np.pi*t)
#x = 0.5 * (np.sin(880*2*np.pi*t) + np.sin(440*2*np.pi*t))
#x = 0.5 * (np.sin(1209*2*np.pi*t) + np.sin(697*2*np.pi*t))


# In[6]:

play(x)


# In[7]:

pt.plot(x[:500])


# Out[7]:

#     [<matplotlib.lines.Line2D at 0x2e3c650>]

# image file:

# In[ ]:



