
# coding: utf-8

# In[9]:

import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as pt


# In[10]:

with open("nixon.txt") as textf:
    nixon = textf.read()
with open("clinton.txt") as textf:
    clinton = textf.read()
with open("rail-transport.txt") as textf:
    rail = textf.read()


# In[11]:

print(nixon[:500])


# How would you turn this into a vector?

# In[12]:

nixon_vec = [ord(c) for c in nixon]


# In[13]:

print nixon_vec[:300]


# Let's try another way.

# In[14]:

def split_into_words(s):
    import re
    return re.split("[., \n\t]+", s)


# In[17]:

print split_into_words(nixon)[:300]


# In[18]:


word_numbers = {}

def learn(s):
    for word in split_into_words(s):
        if word not in word_numbers:
            word_numbers[word] = len(word_numbers)
            
def string_to_vec(s):
    result = np.zeros(len(word_numbers))
    for word in split_into_words(s):
        result[word_numbers[word]] += 1
    return result


# In[19]:


learn(nixon)
learn(clinton)
learn(rail)

nixon_v = string_to_vec(nixon)
clinton_v = string_to_vec(clinton)
rail_v = string_to_vec(rail)


# Plotting could give some insight on this data.

# In[20]:

pt.plot(nixon_v)


# In[21]:

pt.plot(clinton_v)


# In[22]:

pt.plot(rail_v)


# Now we need a measure of similarity.

# In[23]:

def angle_cos(x, y):
    return np.dot(x, y)/(la.norm(x)*la.norm(y))


# In[24]:

print angle_cos(nixon_v, clinton_v)


# In[27]:

print angle_cos(clinton_v, rail_v)


# In[28]:

print angle_cos(nixon_v, rail_v)

