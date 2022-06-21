#!/usr/bin/env python
# coding: utf-8

# In[4]:


def sumvalue(array,target):
    b = []
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i]+array[j]==target:
                b.append([array[i],array[j]])
    if len(b)==0:
        return "No value adds up to 10"
    else:
        return b
array = [int(x) for x in input().split()] 
t = int(input())
a = sumvalue(array,t)
print(a)
    

