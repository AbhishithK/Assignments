#!/usr/bin/env python
# coding: utf-8

# In[3]:


def pow(x,n):
    value = x**n
    return value

x = int(input("Enter number: "))
n = int(input("Enter the power: "))
result = pow(x,n)
print(result)

