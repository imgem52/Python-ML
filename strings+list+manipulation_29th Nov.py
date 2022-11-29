#!/usr/bin/env python
# coding: utf-8

# In[3]:


a="My name is Murtuza"
print(a)


# In[4]:


a='My name is Murtuza'
print(a)


# In[6]:


a="I have teacher's who name is Murtuza, teaching me Python"
print(a)


# In[7]:


#is string iterable


# In[44]:


a='My name is Murtuza'
print(a)


# In[43]:


range(a)


# In[38]:


range(10)


# In[55]:


a="Murtuza"


# In[56]:


len(a)


# In[57]:


for i in a:
    print(i,end="")


# In[59]:


for i in range(len(a)):
    print(a[i],end="")


# In[60]:


a

# SLICING
# In[85]:


a="I have teacher's who name is Murtuza, teaching me Python"
a


# In[83]:


a="name"


# In[84]:


a[1:3]


# In[ ]:





# In[75]:


len(a)     # number of characters 


# In[77]:


a[0]      # it is starting from zero index


# In[81]:


a[55]


# In[82]:


a[:56] # before semicolon if nothing is there by default it will take zero


# In[87]:


a[0:56]    # forward slicing


# In[92]:


a[0:56:3]    # step size(jump activity)


# In[95]:


a[100]


# In[101]:


a[0:6]


# In[105]:


a[::3]   # by default entire str is printed with 2 semicolons step size


# In[104]:


a[0:56:3]


# In[106]:


a


# In[108]:


a[-6:-2]


# In[110]:


a[-1]


# In[113]:


a[-5:-1]


# In[116]:


a[-28:-2]


# In[118]:


a[-28:-2:-2]


# In[132]:


a="I love India"


# In[123]:


a[::-1]   # reverse the string using slicing operations


# In[143]:


c='india'
c


# In[144]:


c.capitalize()


# In[163]:


c.center(50,"*")


# In[150]:


c.count("i")


# In[169]:


c= 'loveIndia'


# In[172]:


c.isupper()


# In[152]:


c.find("i")


# In[153]:


a=[1,2]
if a


# In[ ]:


st="I am going to be master in Python"


# In[5]:


a="Murtuza"


# In[6]:


a.replace("u", "mu")


# In[7]:


a="I\tlove\tIndia"


# In[8]:


a.expandtabs()


# In[133]:


a.capitalize()


# In[129]:


b=[2,3,4]


# In[130]:


type(b)

# 29th November 2022
# In[ ]:


a="My name is Rakesh , my organisation name is XYZ"


# In[45]:


a=int(input())
b=int(input())
type(a+b)
a+b
## Type casting


# In[49]:


a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
if a>b:
    print("{} is greater number".format(a))
else:
    print("The greater number is",b)


# In[50]:


# To print the greatest number among all numbers given

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the first number: "))
if a>b:
    x=a
else:
    x=b
    if x>c:
        print("The greatest number among all is: ", x)
    else:
        print("The greatest number among all is : ", c)


# In[55]:


#a.center(15,"@")


# In[57]:


a="I love India"


# In[58]:


a.find("I")


# In[67]:


for i in range(10):
    print(i+1, end=" ")


# In[73]:


for i in range(1,11):
    if i%2!=0:
        print(i, end=" ")


# In[74]:


[i for i in range(1,11) if i%2!=0]


# In[94]:


a="I love India, I love Pune"


# In[88]:


a.find("I")   # Find by default will give me lowest index


# In[82]:


a[10]


# In[78]:


len(a)


# In[92]:


# finding the occurences of any charachter in string 
for i in range(len(a)):
    if (a[i]=="l" or a[i]=="L"):
        print("The index of l: {}".format(i))


# In[105]:


a="I xy name, I love Pune"


# In[107]:


# find the indexes of word in string
b=a.find("name")
for i in range(len("name")):
    print(b+i)


# In[106]:


b=a.find("name")
b


# In[109]:


a="my\tname\tis\tRakesh"


# In[110]:


a


# In[111]:


a.expandtabs()


# In[114]:


a="my name is Rakesh"
a


# In[115]:


a.replace("Rakesh","Murtuza")


# In[116]:


a


# In[117]:


a.split()


# In[119]:


b=a.split("n")
b


# In[120]:


type(b)   # splitting operation on string the result is list 


# In[121]:


a


# In[122]:


a.capitalize()


# In[123]:


a.upper()


# In[124]:


a.lower()


# In[125]:


a.swapcase()


# In[127]:


" ".join(a)


# In[ ]:


# Mutablity of list 


# In[128]:


l=[22,55,1,20]


# In[130]:


l[0]=88


# In[131]:


l


# In[137]:


a


# In[134]:


a[0]="T"


# In[154]:


a="           my name is Rakesh         "
a


# In[142]:


a[0]


# In[143]:


a.replace("my","All")


# In[146]:


for i in reversed(a):
    print(i, end= " ")


# In[147]:


a.count("a")


# In[153]:


a.strip()


# In[155]:


a.lstrip()


# In[156]:


a.rstrip()


# In[157]:


a


# In[ ]:




