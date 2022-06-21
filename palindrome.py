#!/usr/bin/env python
# coding: utf-8

# In[9]:


def palindrome(a):
    value = str(a)
    return value==value[::-1]

a = input("")
result = palindrome(a)
print(result)
    

