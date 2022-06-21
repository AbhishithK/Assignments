#!/usr/bin/env python
# coding: utf-8

# In[9]:


def balancebracket(s):
    stack = []
    for i in range(len(s)):
        if s[i]=="[" or s[i]=="(" or s[i]=="{":
            stack.append(s[i])
        elif len(stack)!=0 and stack[-1] =="[" and s[i]=="]":
            stack.pop()
        elif len(stack)!=0 and stack[-1] =="{" and s[i]=="}":
            stack.pop()
        elif len(stack)!=0 and stack[-1] =="(" and s[i]==")":
            stack.pop()
        else:
            return False

    if len(stack) == 0:
        return True
    else:
        return False
    
s = input()
function = balancebracket(s)
print(function)
            

