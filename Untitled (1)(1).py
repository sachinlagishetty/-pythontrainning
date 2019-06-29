#!/usr/bin/env python
# coding: utf-8

# In[9]:


def ispalindrome(s):
    if s==s[::-1]:
         return true
    else:
         return false
print(ispalindrome("python"))
print(ispalindrome("jalaj"))


# In[6]:


def countofdigits(n):
    return len(n)
countofdigits("25410")


# In[18]:


def countuppercase(str):
    cnt=0
    lst=list(str)
    for x in range(len(lst)):
        if ord(lst[x])>=65 and ord(lst[x])<=90:
            cnt=cnt+1
    return cnt
print(countuppercase("application"))
print(countuppercase("TeST"))


# In[19]:


def count(str):
    lst=list(str)
    return len(str)
print( count("app"))


# In[1]:


def sumofdigits(str):
    sum=0
    lst=list(str)
    for x in range(len(lst)):
        if ord(lst[x])>=48 and ord(lst[x])<=57:
            sum=sum+ord(lst[x])-48;
    return sum
sumofdigits("application1889")
    


# In[9]:


def sumofdigits(str):
    sum=0
    lst=list(str)
    for x in range(len(lst)):
        if ord(lst[x])>=48 and ord(lst[x])<=57:
            ac=ord(lst[x])-48
            if(ac%2==0):
                sum=sum+ac;
    return sum
sumofdigits("application1889")
    


# In[ ]:





# In[ ]:




