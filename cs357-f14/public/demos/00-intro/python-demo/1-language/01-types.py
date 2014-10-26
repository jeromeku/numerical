
# coding: utf-8

# Let's evaluate some simple expressions.

# In[1]:

3*2


# In[2]:

5+3*2


# You can use `type()` to find the *type* of an expression.

# In[3]:

type(5+3*2)


# Now add decimal points.

# In[4]:

5+3.5*2


# In[5]:

type(5+3.0*2)


# Strings are written with single (``'``) or double quotes (`"`)

# In[6]:

"hello"


# Multiplication and addition work on strings, too.

# In[7]:

3 * 'hello' + "eagpggpu"


# Lists are written in brackets (`[]`) with commas (`,`).

# In[8]:

[5, 3, 7]


# List entries don't have to have the same type.

# In[9]:

["hi there", 15, [1,2,3]]


# "Multiplication" and "addition" work on lists, too.

# In[10]:

[1,2,3] * 4 + [5, 5, 5]


# Hmmmmmm. Was that what you expected?

# In[11]:

import numpy as np

np.array([1,2,3]) * 4 + np.array([5,5,5])

