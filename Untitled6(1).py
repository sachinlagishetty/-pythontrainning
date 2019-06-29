#!/usr/bin/env python
# coding: utf-8

# In[1]:


s="python programming";
print(s.replace("gra","application"))


# In[3]:


t1=("python","programming",1889,2019,"machine learning","ai")
print("t1[0]=",t1[0])
print("t1[2]=",t1[2])
print("t1[-1]=",t1[-1])


# In[8]:


t1=("python","programming",1889,2019,"machine learning","ai")
print(t1)
del t1
print(t1)


# In[9]:


t1=("python","programming")
t2=(1889,2019,"machine learning","ai")
t3=t1+t2
print(t3)


# In[ ]:


t1=("python","programming",1889,2019,"machine learning","ai")
print()


# In[5]:


contacts={}
cdef addcontact(name,phone):
    if name not in contacts:
        contacts[name]=phone
        print("contact %s added"% name)
    else:
        print("contact %s already exists "% name)
    return
addcontact("anil",9551325644)
addcontact("shashank",9876543210)


# In[12]:


def importcontacts(newcontacts):
    contacts.update(newcontacts)
    print(len(newcontacts.keys()),"contacts added successfully")
    return
newcontacts={'dinesh':9556542130}
importcontacts(newcontacts)


# In[15]:


def deletecontacts(name):
    if name in contacts:
        del contacts[name]
        print(name,":is deleted from the contacts")
    else:
        print(name,":is not exist in contacts")
    return
deletecontacts("shashank")


# In[ ]:





# In[ ]:




