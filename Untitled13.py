#!/usr/bin/env python
# coding: utf-8

# In[1]:


str="application"
print(str)
print("str[0]=",str[0])
print("str[1]=",str[1])
print("str[-1]=",str[-1])
print("str[-3]=",str[-3])
print("str[1:5]=",str[1:5])
print("str[:5]=",str[:5])
print("str[5:-2]=",str[5:-2])
print("str[::-1]=",str[::-1])#used for reverse the string


# In[5]:


#palindrome of string
def palindrome(s):
    if s==s[::-1]:
        return True
    else:
        return False

print(palindrome("python"))
print(palindrome("jalaj"))


# In[10]:


def countofchars(str):
    return len(str)
countofchars("Gitam")


# In[9]:


def countdigits(n):
    return len(n)

countdigits("25410")


# In[14]:


def countuppercase(str):
    cnt=0
    lst=list(str)
    for x in range(len(lst)):
        if ord(lst[x])>=65 and ord(lst[x])<=90:
            cnt=cnt+1
    return cnt

print(countuppercase("AppLication"))
print(countuppercase("TesT"))
print(countuppercase("BlascwozwisckYZ"))


# In[ ]:


def printdigits(str):
    
    return

print(printdigits("application"))


# In[ ]:




