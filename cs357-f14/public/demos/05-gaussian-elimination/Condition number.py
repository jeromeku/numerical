
# coding: utf-8

# # Condition number

# In[8]:

import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as pt


# In[97]:

np.random.seed(17)
A = np.random.randn(2, 2)
Ainv = la.inv(A)


# In[98]:

phi = np.linspace(0, 2*np.pi, 15)
xs = np.array([
    np.cos(phi),
    np.sin(phi)
])

pt.plot(xs[0], xs[1], "x")
pt.grid()


# In[99]:

Axs = np.einsum("ik,kj->ij", A, xs)
Axs.shape


# In[100]:

pt.figure(figsize=(10, 5))

pt.subplot(121)
pt.title("$x$")
pt.plot(xs[0], xs[1], "x")
pt.gca().set_aspect("equal")

pt.subplot(122)
pt.title("$Ax$")
pt.plot(Axs[0], Axs[1], "v")
pt.gca().set_aspect("equal")


# In[104]:

# ys has axes: XY x Npoints x Npoints

perturbation_size = 0.1
ys = perturbation_size * xs[:, :, np.newaxis] + xs[:, np.newaxis, :]

Ays = np.einsum("ik,kjl->ijl", A, ys)
Ays.shape


# In[102]:

pt.figure(figsize=(10, 5))

pt.subplot(121)
pt.title("$y$")
pt.plot(ys[0], ys[1])
pt.gca().set_aspect("equal")

pt.subplot(122)
pt.title("$Ax$")
pt.plot(Ays[0], Ays[1])
pt.gca().set_aspect("equal")


# In[103]:

norm = la.norm(A, 2)
print(norm)

pt.plot(Ays[0], Ays[1])

ax = pt.gca()
ax.set_aspect("equal")
ax.add_artist(pt.Circle([0, 0], norm, alpha=0.3, lw=0))


# Now we want a $\kappa$ with $\frac{\|\Delta b\|}{\|b\|}\le \kappa \frac{\|\Delta x\|}{\|x\|}$.
# 
# Consider $\|x\|=1$. Equivalent: $\|\Delta b\|\le \kappa \|\Delta x\|\|b\|$.
# 
# Which $\kappa$ does the job?

# In[117]:

kappa = la.norm(A, 2)*la.norm(Ainv, 2)


# In[118]:

pt.plot(Ays[0], Ays[1])

ax = pt.gca()
ax.set_aspect("equal")
for i in range(Ays.shape[2]):
    b = Axs[:, i]
    norm_delta_y = kappa * perturbation_size * la.norm(b)
    ax.add_artist(pt.Circle(b, norm_delta_y, alpha=0.3, lw=0))


# In[ ]:



