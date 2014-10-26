
# coding: utf-8

# In[10]:

import numpy as np
import matplotlib.pyplot as pt


# In[11]:

from PIL import Image


# In[18]:


def load_image(name):
    with Image.open(name).resize((500,500)) as img:
        return np.sum(np.array(img), axis=-1).astype(np.float32)/(3*255)


# In[19]:


andreas = load_image("andreas.jpeg")


# In[25]:

# keep
pt.imshow(andreas, cmap="gray")


# Let's get a little creative... (`vmin` and `vmax` as keyword arguments on `imshow` might be handy)

# In[30]:

pt.imshow(3*andreas, cmap="gray", vmin=0, vmax=1)


# ---------------------

# In[23]:

dicaprio = load_image("dicaprio.jpeg")


# Now let's try something truly scary...

# In[24]:

pt.imshow(andreas + dicaprio, cmap="gray")


# In[ ]:



