
# coding: utf-8

# # Predicting Breast Cancer with Least Squares

# In[1]:

import numpy as np
import numpy.linalg as la


# In[2]:

import pandas as pd


# In[3]:

params = ["radius", "texture", "perimeter","area","smoothness","compactness","concavity","concave points","symmetry","fractal dimension"];
stats = ["(mean)", "(stderr)", "(worst)"]
labels = ["patient ID", "Malignant/Benign"]
i = 2
for p in params:
    for s in stats:
        labels.append(p + " " + s)


# This data comes from the [Wisconsin Diagnostic Breast Cancer](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Original%29) data set, via the [Klein book](http://resources.codingthematrix.com/).
# 
# Take a look at the raw data in a text editor now.

# In[4]:

train_data = pd.io.parsers.read_csv("breast-cancer-train.dat", header=None, names=labels)
validate_data = pd.io.parsers.read_csv("breast-cancer-validate.dat", header=None, names=labels)


# In[5]:

train_data


# In[6]:

train_data.describe()


# In[7]:

train_data["radius (mean)"].hist()


# Curious? Click [here](http://pandas.pydata.org/pandas-docs/stable/) to learn more about pandas.
# 
# (It is also installed in the virtual machine if you'd like to play around.)

# -----------------
# Now back on topic:
# 
# We'll read "malignant" as +1 and "benign" as -1.

# In[8]:

b_train = train_data["Malignant/Benign"].values
b_train = (b_train == "M").astype(np.float64)*2 -1

b_validate = validate_data["Malignant/Benign"].values
b_validate = (b_validate == "M").astype(np.float64)*2 -1

b_train


# We would like to discover coefficients $(w_i)$ on the "feature" columns of the data so that
# 
# $$\text{row}\cdot w \approx\begin{cases}+1 & \text{Malignant}\\-1& \text{Benign}\end{cases}$$
# 
# We'll read the "$\approx$" in the least-squares sense.

# Now extract the feature data. `DataFrame.values` returns the data as a `numpy` array.

# In[9]:

A_train = train_data.values[:, 2:]
A_validate = validate_data.values[:, 2:]

A_train.shape


# Now solve the least squares system:

# In[10]:

Q, R = la.qr(A_train, "complete")

w = la.solve(R[:30], Q.T.dot(b_train)[:30])


# Now compute the predictions, as a vector of +1/-1:

# In[11]:

predicted_train = A_train.dot(w)
predicted_train


# In[12]:

predicted_train[predicted_train > 0 ] = 1
predicted_train[predicted_train < 0 ] = -1


# Next, compute the fraction of values where our prediction disagrees with the training data. Use `np.where`:

# In[21]:

disagree_train = np.where(predicted_train != b_train)[0]
disagree_train


# In[22]:

len(disagree_train)/len(b_train)


# -------------
# Now perform the same check on the validation data:

# In[23]:

predicted_validate = A_validate.dot(w)
predicted_validate[predicted_validate > 0 ] = 1
predicted_validate[predicted_validate < 0 ] = -1

disagree_validate = np.where(predicted_validate != b_validate)[0]
len(disagree_validate)/len(b_validate)

