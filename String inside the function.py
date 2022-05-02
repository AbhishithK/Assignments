#!/usr/bin/env python
# coding: utf-8

# In[21]:


def reversestring(a):
    for i in range(1,len(a)+1):
        print(a[-i],end="")
    
a = "1234abcd"
result = reversestring(a)

