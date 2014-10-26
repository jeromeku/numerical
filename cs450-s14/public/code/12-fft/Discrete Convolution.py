
# In[1]:

from __future__ import division
import numpy as np
import matplotlib.pyplot as pt


# In[3]:

n = 2048

spikes = np.zeros(n)
spikes[730] = 1
spikes[1512] = 0.3
pt.plot(spikes)


# Out[3]:

#     [<matplotlib.lines.Line2D at 0x36682d0>]

# image file:

# In[5]:

pattern = np.zeros_like(spikes)
pattern[n/2-100:n/2+100] = np.sin(np.linspace(-pi, pi, 200))


# Out[5]:

#     -c:2: DeprecationWarning: using a non-integer number instead of an integer will result in an error in the future
# 

# In[9]:

pt.plot(np.convolve(pattern, spikes))


# Out[9]:

#     [<matplotlib.lines.Line2D at 0x3f72910>]

# image file:

# # Now with the FFT

# In[8]:

spikes_hat = np.fft.ifft(spikes)
pattern_hat = np.fft.ifft(pattern)

convolved = np.fft.fft(spikes_hat * pattern_hat)
pt.plot(convolved.real)


# Out[8]:

#     [<matplotlib.lines.Line2D at 0x3ec34d0>]

# image file:

# In[8]:



