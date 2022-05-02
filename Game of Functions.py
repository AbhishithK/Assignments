#!/usr/bin/env python
# coding: utf-8

# In[4]:


def sum_value(l):
    total = 0
    for val in l:
        total = total + val
    return total

value = (8,2,3,0,7)
result = sum_value(value)
print(result)

