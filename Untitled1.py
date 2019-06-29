#!/usr/bin/env python
# coding: utf-8

# In[2]:


def BinarySearch(list,key):
    low=0
    high=len(list)-1
    while low<=high:
        mid=(low+high)//2
        if key==list[mid]:
         return 1
        if key<list[mid]:
            high=mid-1
        else:
            low=mid+1
    return -1
list=[1,43,56,78,90,98,99]
res=BS(list,9)
if res==-1:
    print("element not found")
else:
    print("found")
        


# In[22]:


def ispolindroome(s):
    if s==s[::-1]:
           return true
    else:
            return flase
print(ispolindroome(python))
print(ispolindroome(jalaj))


# In[20]:


def countofcharts(str):
    return len(str)
countofcharts("25410")


# In[23]:


def countuppercase(str):
    cnt=0
    
    return cnt
print(countuppercasae("application"))
print(countuppercase("test"))


# In[34]:


def count(str):
    lst=lst(str)
    return len(lst)
print(count("app"))


# In[38]:


def countuppercase(str):
    cnt=0
    lst=list(str)
    for x in range(len(lst)):
        if ord(lst[x]) >=65 and ord(lst[x])<=90:
            cnt=cnt+1
    return cnt
print(countuppercase("application"))
print(countuppercase("test"))


# In[39]:


def printdights(str):
    
    
    
    return
print(printdights("application1889")) #1889


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




