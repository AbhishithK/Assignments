#!/usr/bin/env python
# coding: utf-8

# In[97]:


a = [int(num) for num in input("Enter value: ").split()]
odd_day = 0
even_day = 0
for i in a:
    if i%2 ==0:
        even_day+=1
    else:
        odd_day+=1
print("Number of Even number:",even_day)
print("Number of Odd number :",odd_day)

