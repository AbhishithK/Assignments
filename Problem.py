#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
Write a Python class to find the three elements that sum to zero from a set (array) of n real numbers.
'''

input_value= [-25, -10, -7, -3, 2, 4, 8, 10]
target=[]
class index():
    def __init__(self,index_value):
        self.index_value = index_value
    def summing(self):
        for i in range(len(input_value)):
            for j  in range(1,len(input_value)):
                for k in range(2,len(input_value)):
                    value1 = input_value[i]
                    value2 = input_value[j]
                    value3 = input_value[k]
#                     print(value1,value2,value3,'sum value',value1+value2+value3)
                    if value1+value2+value3 ==0:
                        target.append([input_value[i],input_value[j],input_value[k]])
                        return target
#         ,input_value[j],input_value[k])
index_value = index(([0,10,-1,-7,-3,20,10,7]))
print(index_value.summing())

