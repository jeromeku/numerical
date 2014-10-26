
# coding: utf-8

# # Traffic flow
# 
# An application of nullspace finding

# ![A traffic network](traffic.jpeg)
# 
# ([Source](http://aix1.uottawa.ca/~jkhoury/networks.htm))

# In[143]:

import numpy as np
import scipy.linalg as la


# In[30]:

flow_vars = ["x", "y", "z", "u", "v", "w", "t"]


# In[29]:

nodes = [
    ["-x", "-v", 800], # A
    ["+x", "-y", "+u", -400], # B
    ["+y", "-z", -600], # C
    ["+v", "+w", -600-400], # F
    ["-u", "-w", "+t", 0], # E
    ["+z", "-t", 1600-400], # D
]


# Represent [Kirchhoff's first law](https://en.wikipedia.org/wiki/Kirchhoff's_circuit_laws) in matrix form:
# 
# * What size matrix $A$?
# * What size RHS $b$?

# In[31]:

A = np.zeros((len(nodes), len(flow_vars)))
b = np.zeros(len(nodes))


# In[32]:

for i, node in enumerate(nodes):
    b[i] = node[-1]
    node_connections = node[:-1]
    
    for cnx in node_connections:
        j = flow_vars.index(cnx[1])
        if cnx[0] == "+":
            A[i,j] = +1
        elif cnx[0] == "-":
            A[i,j] = -1
        else:
            raise RuntimeError("invalid connection")


# Take a look at $A$ and $b$:
# 
# * Notice something about $A$? (Look at each column)

# In[33]:

A


# In[34]:

b


# What's $\operatorname{dim} N(A)$?

# --------------
# Can we find the traffic flow?

# In[39]:

la.solve(A, b)


# ------------------
# Now find the nullspace:

# In[103]:

PT, L, U = la.lu(A.T)

# rearrange L/U shape to make L square
m,n = L.shape
N = max(m,n)
Lnew = np.eye(N)
Lnew[:m,:n] = L

Unew = np.zeros(A.T.shape)
Unew[:n, :n] = U

U = Unew
L = Lnew

P = PT.T


# In[104]:

la.norm(
    P.dot(A.T) - L.dot(U))


# In[105]:

U


# Now find $N(U^T)$ as NUT:

# In[110]:

NUT = np.eye(len(flow_vars))[:, -2:]
NUT


# In[116]:

U.T.dot(NUT)


# Now find $N(A)$ as `NA`:

# In[112]:

NA = P.T.dot(la.solve(L.T, NUT))


# In[114]:

A.dot(NA)


# In[117]:

NA


# ------------
# Suppose a peculiar solution to $Ax=b$ fell from the sky:
# 
# (We'll learn what this snippet does soon.)

# In[131]:

x = la.lstsq(A, b)[0]
x


# In[133]:

la.norm(A.dot(x) - b)


# Negative numbers? Is that OK? What does that mean?

# ----------------
# * What does the nullspace give us? (Think "circuit".)

# In[139]:

y = x - 2 * NA[:, 0] + 3 * NA[:, 1]
y


# Can we close $u$ street to traffic? (4th entry)

# In[140]:

y = x - 120 * NA[:, 0]
y


# In[141]:

np.dot(A, y) - b


# In[ ]:



