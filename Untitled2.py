#!/usr/bin/env python
# coding: utf-8

# In[5]:


x=int(input("enter the number"))
while(x!=0):
    r=x%10
    if(r==0):
        print("zero")
    elif(r==1):
        print("one")
    elif(r==2):
        print("two")
    elif(r==3):
        print("three")
    elif(r==4):
        print("four")
    elif(r==5):
        print("five")
    elif(r==6):
        print("six")
    elif(r==7):
        print("seven")
    elif(r==8):
        print("eight")
    elif(r==9):
        print("nine")
    x=x//10


# In[ ]:





# In[8]:


x=int(input("enter the first number"))
y=int(input("enter the second number"))
z=int(input("enter the third number"))
while(y<=z):
    print(y)
    y=y+1


# In[ ]:


x=int(input("enter the number"));
y= int(input("enter lower limit"));
z= int(input("enter upper limit"));


cnt=0;
while(y!=z):
    buffer=y;
    while(y!=10):
        r=11%10;
        if(r==x):
            cnt=cnt+1;
            y=y//10;
            y=buffer;
            y=y+1;
print(cnt);


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




