#!/usr/bin/env python
# coding: utf-8

# In[46]:


n = 9
def fib(n):
    x = 0
    y = 1
    for i in range(n):
        print(y)
        z = x+y
        x = y
        y = z
fib(n)


# In[ ]:




