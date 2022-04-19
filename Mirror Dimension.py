#!/usr/bin/env python
# coding: utf-8

# In[77]:


a = input("Enter the value - ")
for i in range(len(a)):
    print(a[-i-1],end="")

