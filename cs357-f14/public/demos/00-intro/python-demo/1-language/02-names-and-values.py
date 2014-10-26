
# coding: utf-8

# Define and reference a variable:

# In[22]:

a = 3*2 + 5


# In[23]:

a


# In[24]:

a = "interesting"*3


# In[25]:

a


# No type declaration needed!
# 
# (But values still have types--let's check.)

# In[26]:

type(a)


# Python variables are like *pointers*.
# 
# (if that word makes sense)

# In[27]:

a = [1,2,3]


# In[28]:

b = a


# In[29]:

b.append(4)


# In[30]:

b


# In[31]:

a


# You can see this pointer with `id()`.

# In[33]:

print(id(a), id(b))


# The `is` operator tests for object sameness.

# In[34]:

a is b


# This is a **stronger** condition than being equal!

# In[36]:

a = [1,2,3]
b = [1,2,3]
print("IS   ", a is b)
print("EQUAL", a == b)


# What do you think the following prints?

# In[38]:

a = [1,2,3]
b = a
a = a + [4]
print(b)


# In[39]:

a is b


# Why is that?

# -----
# How could this lead to bugs?

# ----------
# * To help manage this risk, Python provides **immutable** types.
# 
# * Immutable types cannot be changed in-place, only by creating a new object.
# 
# * A `tuple` is an immutable `list`.

# In[40]:

a = [1,2,3]
type(a)


# In[41]:

a = (1,2,3)
type(a)


# Let's try to change that tuple.

# In[42]:

a[2] = 0


# *Bonus question:* How do you spell a single-element tuple?

# In[43]:

a = (3,)
type(a)

