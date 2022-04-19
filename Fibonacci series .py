#!/usr/bin/env python
# coding: utf-8

# In[62]:


n = int(input("Enter the value where you want to end the series - ")) 
#Example if you want the series to end before 50 enter value 50
x = 0
y = 1
z = 0
while z < n:
    print(y,end = " ")
    z = x+y
    x = y
    y = z

