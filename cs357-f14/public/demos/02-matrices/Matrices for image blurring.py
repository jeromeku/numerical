
# coding: utf-8

# # Matrices for image blurring

# In[1]:

import numpy as np
import matplotlib.pyplot as pt


# In[30]:

from PIL import Image

with Image.open("cat.jpeg").resize((500,500)) as img:
    img = np.array(img).sum(axis=-1)
    
h, w = img.shape


# In[31]:

pt.figure(figsize=(8,8))
pt.imshow(img, cmap="gray")


# Now make a Gaussian with as many pixels as the image is wide.

# In[38]:

x = np.linspace(-1, 1, w)
gaussian = np.exp(-500*x**2)
gaussian = np.roll(gaussian, -w//2)
pt.plot(x, gaussian)


# Now, fill a $w\times w$ matrix with shifted versions of this:

# In[39]:

A = np.zeros((w,w))
for i in range(w):
    A[:, i] = np.roll(gaussian, i)


# Multiply the cat by this.

# In[40]:

blurrycat = np.einsum("nx,yx->yn", A, img)


# In[43]:

pt.figure(figsize=(8,8))
pt.imshow(blurrycat, cmap="gray")


# In[ ]:



