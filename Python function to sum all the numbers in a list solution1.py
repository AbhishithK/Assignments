#!/usr/bin/env python
# coding: utf-8

# In[28]:


def sum_value(l,n):
    if n == 0:
        return l[n];
    return l[n] + sum_value(l,n-1)

value = (8,2,3,0,7)
result = sum_value(value,len(value)-1)
print(result)


# In[ ]:




