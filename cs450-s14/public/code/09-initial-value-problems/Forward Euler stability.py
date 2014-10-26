
# In[7]:

import numpy as np
import matplotlib.pyplot as pt


# We'll integrate
# 
# $$ y'=\alpha y$$
# 
# with $y'(0) = 1$,
# 
# using forward Euler.

# In[119]:

# alpha = 1; h = 0.1; final_t = 20
# alpha = -1; h = 0.1; final_t = 20
#alpha = -1; h = 1; final_t = 20
#alpha = -1; h = 1.5; final_t = 20
#alpha = -1; h = 2; final_t = 20
alpha = -1; h = 2.5; final_t = 20


# In[120]:

t_values = [0]
y_values = [1]

def f(y):
    return alpha * y


# In[121]:

while t_values[-1] < final_t:
    t_values.append(t_values[-1] + h)
    y_values.append(y_values[-1] + h*f(y_values[-1]))


# In[122]:

mesh = np.linspace(0, final_t, 100)
pt.plot(t_values, y_values)
pt.plot(mesh, np.exp(alpha*mesh), label="true")
pt.legend()


# Out[122]:

#     <matplotlib.legend.Legend at 0x78d2550>

# image file:

# In[ ]:



