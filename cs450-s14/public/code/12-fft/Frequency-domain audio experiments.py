
# In[20]:

from __future__ import division
import numpy as np
import matplotlib.pyplot as pt


# In[21]:

wave = 60*load("cs450.npy")


# In[22]:

plot(wave)


# Out[22]:

#     [<matplotlib.lines.Line2D at 0x69a00d0>]

# image file:

# In[23]:

from simple_audio import play
play(wave)


# In[5]:

n = 256

integers = arange(n)

omega = exp(1j*2*np.pi/n)
dft_matrix = omega ** (integers * integers[:, newaxis])

inv_dft_matrix = 1./n*dft_matrix.T.conj()


# In[6]:

chunked = wave.reshape(-1, n)
transformed = np.dot(inv_dft_matrix, chunked.T).T


# In[8]:

imshow(log10(1e-4+abs(transformed)).T); colorbar()


# Out[8]:

#     <matplotlib.colorbar.Colorbar instance at 0x4f95320>

# image file:

# In[17]:

modified = transformed.copy()

#modified[:,5:-5] *= 1e-2

#modified *= 1e-2
#modified[:,5:-5] /= 1e-2

nshift = 3
modified.fill(0)
modified[:, nshift:n/2] = transformed[:, 0:n/2-nshift]
modified[:, n/2:n-nshift] = transformed[:, n/2+nshift:]

imshow(log10(1e-4+abs(modified)).T); colorbar()


# Out[17]:

#     -c:10: DeprecationWarning: using a non-integer number instead of an integer will result in an error in the future
#     -c:11: DeprecationWarning: using a non-integer number instead of an integer will result in an error in the future
# 

#     <matplotlib.colorbar.Colorbar instance at 0x6477c68>

# image file:

# In[18]:

chunked = modified.reshape(-1, n)
result = np.dot(dft_matrix, chunked.T).T

result = result.reshape(-1)


# In[19]:

play(result.real)


# In[13]:

play(wave.real)


# In[ ]:



