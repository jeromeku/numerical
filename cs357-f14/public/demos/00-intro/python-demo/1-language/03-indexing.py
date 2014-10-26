
# coding: utf-8

# The `range` function lets us build a list of numbers.

# In[12]:

list(range(10, 20))


# Notice anything funny?
# 
# Python uses this convention everywhere.

# In[13]:

a = list(range(10, 20))
type(a)


# Let's talk about indexing.
# 
# Indexing in Python starts at 0.

# In[14]:

a[0]


# And goes from there.

# In[15]:

a[1]


# In[16]:

a[2]


# What do negative numbers do?

# In[6]:

a[-1]


# In[17]:

a[-2]


# You can get a sub-list by *slicing*.

# In[19]:

a[3:7]


# Start and end are optional.

# In[20]:

a[3:]


# In[21]:

a[:3]


# Again, notice how the end entry is not included:

# In[23]:

print(a[:3])
print(a[3])


# Slicing works on any collection type! (`list`, `tuple`, `str`, `numpy` array)

# In[24]:

a = "CS357"
a[-3:]

