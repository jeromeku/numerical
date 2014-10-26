
# coding: utf-8

# `for` loops in Python always iterate over something list-like:

# In[2]:

for i in range(10):
    print(i)


# **Note** that Python does block-structuring by leading spaces.
# 
# Also note the trailing "`:`".

# ---
# `if`/`else` are as you would expect them to be:

# In[3]:

for i in range(10):
    if i % 3 == 0:
        print("{0} is divisible by 3".format(i))
    else:
        print("{0} is not divisible by 3".format(i))


# `while` loops exist too:

# In[5]:

i = 0
while True:
    i += 1
    if i**3 + i**2 + i + 1 == 3616:
        break

print("SOLUTION:", i)


# ----
# Building lists by hand can be a little long. For example, build a list of the squares of integers below 50 divisible by 7:

# In[6]:

mylist = []
for i in range(50):
    if i % 7 == 0:
        mylist.append(i**2)


# In[7]:

mylist


# Python has a something called *list comprehension*:

# In[8]:

mylist = [i**2 for i in range(50) if i % 7 == 0]


# In[9]:

mylist

