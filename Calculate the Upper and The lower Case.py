#!/usr/bin/env python
# coding: utf-8

# In[39]:


def upper_lower_count(l):
    global upper
    global lower
    upper = 0
    lower = 0
    for value in l:
        if value.isupper():
            upper+=1
        elif value.islower():
            lower+=1
    return upper
    return lower

s = 'The quick Brow Fox'
result = upper_lower_count(s)
print('No. of Upper case characters : ',upper)
print('No. of Upper case characters : ',lower)

