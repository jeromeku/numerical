
# coding: utf-8

# In[32]:

import numpy as np
import matplotlib.pyplot as pt


# In[33]:

from PIL import Image

with Image.open("andreas.jpeg").resize((500,500)) as img:
    rgb_img = np.array(img)
rgb_img.shape


# In[34]:

img = np.sum(rgb_img, axis=-1)


# In[35]:

pt.imshow(img, cmap="gray")


# In[36]:

u, sigma, vt = np.linalg.svd(img)
sigma

pt.plot(sigma)


# In[45]:


compressed_img = (
    sigma[0] * np.outer(u[:, 0], vt[0])
    )

pt.imshow(compressed_img, cmap="gray")


# In[37]:



