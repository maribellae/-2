#!/usr/bin/env python
# coding: utf-8

#  # VI.9.2. e)  МАКАРОВА МАРИЯ 

# In[113]:


import numpy as np
import decimal
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import pylab
from sympy import diff, symbols, cos, sin, exp , ln, sqrt
from sympy import *
x, y = symbols('x y')


# In[114]:


b1=[0,0,0,0]
b2=[0,0,0]
b3=[0,0]
b4=[0]
a=[0,2,3,5,7]
b=[-1,0,2,3,5]
res=[-1,0,0,0,0]


# In[115]:


for i in range(4):
    b1[i] = (b[i+1]-b[i])/(a[i+1]-a[i])
    print(b1[i])
res[1] = b1[0]   


# In[116]:


for i in range(3):
    b2[i] = (b1[i+1]-b1[i])/(a[i+2]-a[i])
    print(b2[i])
    
res[2] = b2[0] 


# In[117]:


for i in range(2):
    b3[i] = (b2[i+1]-b2[i])/(a[i+3]-a[i])
    print(b3[i])
res[3] = b3[0]    


# In[118]:


for i in range(1):
    b4[i] = (b3[i+1]-b3[i])/(a[i+4]-a[i])
    print(format(b4[i], '.5f'))
res[4] = b4[0]     


# In[119]:


res


# In[120]:


from scipy.misc import derivative
def ff(x):
    return(res[0] + res[1]*(x-a[0]) + res[2]*(x-a[0])*(x-a[1])+ res[3]*(x-a[0])*(x-a[1])*(x-a[2])+res[4]*(x-a[0])*(x-a[1])*(x-a[2])*(x-a[3]))
derivative(ff, 3.0, dx=1e-6)


# Конец :)
