
# coding: utf-8

# # Convex combinations

# In[2]:

import numpy as np
import matplotlib.pyplot as pt


# In[3]:

n_vectors = 3
vecs = np.random.randn(2, n_vectors)


# Let's make an array of random coefficients, in `coeffs`.

# In[4]:

n_coeffs = n_vectors


# In[5]:

# Random numbers between 0 and 1. Don't confuse with randn.
coeffs = np.random.rand(n_coeffs, 10000)

sum_of_first_two = np.sum(coeffs[:2], axis=0)
coeffs[2] = 1-sum_of_first_two # (*)

# First two coefficients guaranteed to be positive
# Third coefficcient could be negative
# All coefficients guaranteed to add up to one because of (*)
good_coeffs = coeffs[2] >= 0
print(good_coeffs)

coeffs = coeffs[:, good_coeffs]


# Now assemble the convex combinations:

# In[6]:

n_combinations = coeffs.shape[-1]
print(n_combinations)

combinations = np.zeros((2, n_combinations))


# Shape summary:
# 
# * combinations (output): 2 (X and Y) $\times$ `n_combinations`
# * coeffs (input): 3 (# of coefficients in conv. comb) $\times$ `n_combinations`
# * vecs (input): 2 (X and Y) $\times$ 3 (# of vectors in conv. comb.)

# In[7]:

for i in range(n_combinations):
    for j in range(n_vectors):
        combinations[:, i] += coeffs[j, i]*vecs[:, j]


# <!--
# for i in range(n_combinations):
#     for j in range(n_vectors):
#         combinations[:, i] += coeffs[j, i]*vecs[:, j]
# -->
# (edit this cell for solution)

# In[8]:

pt.plot(combinations[0], combinations[1], "o")


# Now do the same thing with a numpy one-liner:

# In[9]:

combinations = np.einsum("ji,kj->ki", coeffs, vecs)


# <!--
# combinations = np.einsum("ji,kj->ki", coeffs, vecs)
# -->
# (edit this cell for solution)

# In[10]:

pt.plot(combinations[0], combinations[1], "o")

