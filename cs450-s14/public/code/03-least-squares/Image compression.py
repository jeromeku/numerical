
# In[1]:

import numpy as np
import matplotlib.pyplot as pt


# In[2]:

from PIL import Image

rgb_img = np.array(Image.open("andreas.jpeg").resize((500,500)))
rgb_img.shape


# Out[2]:

#     (500, 500, 3)

# In[3]:

img = sum(rgb_img, axis=-1)


# In[4]:

imshow(img, cmap="gray")


# Out[4]:

#     <matplotlib.image.AxesImage at 0x2fac690>

# image file:

# In[5]:

u, sigma, vt = svd(img)
sigma

pt.plot(sigma)


# Out[5]:

#     [<matplotlib.lines.Line2D at 0x3349310>]

# image file:

# In[6]:

reduced_sigma = sigma.copy()
reduced_sigma[10:] = 0


# In[7]:

imshow(np.dot(np.dot(u,np.diag(reduced_sigma)),vt), cmap="gray")


# Out[7]:

#     <matplotlib.image.AxesImage at 0x3be3fd0>

# image file:
