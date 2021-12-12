#!/usr/bin/env python
# coding: utf-8

# In[11]:


class powervalue():
    def __init__(self,value,power):
        self.value = value
        self.power = power
    def nthvalue(self):
        return self.value ** self.power
input1 = powervalue(10,2)
print(input1.nthvalue())

