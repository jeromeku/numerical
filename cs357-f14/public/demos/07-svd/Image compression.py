
# coding: utf-8

# In[1]:

import numpy as np
import matplotlib.pyplot as pt


# In[2]:

from PIL import Image

with Image.open("andreas.jpeg").resize((500,500)) as img:
    rgb_img = np.array(img)
rgb_img.shape


# In[3]:

img = np.sum(rgb_img, axis=-1)


# In[4]:

pt.imshow(img, cmap="gray")


# In[5]:

u, sigma, vt = np.linalg.svd(img)
sigma

pt.plot(sigma)


# In[11]:


compressed_img = (
    sigma[0] * np.outer(u[:, 0], vt[0])
    )

pt.imshow(compressed_img, cmap="gray")


# In[37]:



