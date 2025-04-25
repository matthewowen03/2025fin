#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Fibonnaci


# In[2]:


def fibonacci(n):
    if n<=2:
        print("please enter a number which is greater than 2!")
        
    else:
        fib = [1,1]
        ratio = [1]
        for i in range(2,n):
            fib_new = fib[i-1] + fib[i-2]
            fib.append(fib_new)
            ratio_new = fib[i-1] / fib_new
            ratio.append(ratio_new)
        print(fib)
        print(ratio)


# In[3]:


fibonacci(2)


# In[4]:


fibonacci(7)


# In[7]:


fibonacci(10)


# In[ ]:




