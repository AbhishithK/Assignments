#!/usr/bin/env python
# coding: utf-8

# In[12]:


def reverse_value(value):
    if value == list or value == str: 
        reverse = value[::-1]
        return reverse
    else:
        temp = str(value)
        reverse = temp[::-1]
        return reverse  

s = '1234abcd'
result = reverse_value(s)
print(result)


# In[ ]:




