#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


#1.Write a Python Program to find sum of array?
arr=np.array([1,2,3,4,5,6,7,8])
print(sum(arr))


# In[49]:


#2.Write a Python Program to find largest element in an array?
print(max(arr))


# In[50]:


#3.Write a Python Program for array rotation?
a=int(input("enter the number of rotation you want in array"))
np.roll(arr,a)


# In[51]:


#4.Write a Python Program to Split the array and add the first part to the end?
n=4 #index where i want to split
a=len(arr)
for i in range(0,n):
    x=arr[0]
    for j in range(0,a-1):
        arr[j]=arr[j+1]
    
    arr[a-1]=x
        
arr


# In[8]:


#5.Write a Python Program to check if given array is Monotonic?
arr1=np.array([5,6,7,8,9,56,124,6455])
mon=0

def monotic(b):
    if all(b[i] < b[i+1] for i in range(len(b)-1)):
        return 1
    
    if all(b[i] > b[i+1] for i in range(len(b)-1)):
            return 2
    
    else:
        return 3
   
b=monotic(arr1)
if b==1 or b==2:
    print ("the given array is monotic")
else:
    print("the given array is not monotic")


# In[ ]:





# In[ ]:




