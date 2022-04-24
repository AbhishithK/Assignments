#!/usr/bin/env python
# coding: utf-8

# In[9]:


l = [(2, 5), (1, 2),(4, 4),(2, 3),(2, 1)]
for index in range(0,len(l)):
    for next_index in range(index +1,len(l)):
        num = l[index]
        current_value = num[-1]
        num2 = l[next_index]
        next_value = num2[-1]
        if next_value < current_value:
            l[next_index] = num
            l[index] = num2
            current_value = next_value
print(l)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




