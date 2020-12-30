#!/usr/bin/env python
# coding: utf-8

# In[9]:


# 1) Write lambda functions to find area of square, rectangle and triangle

triArea=lambda a,b:0.5*a*b
recArea=lambda a,b:a*b
squareArea=lambda a:a*a
print("Enter Length and Breadth of Rectangle")
l=int(input())
b=int(input())
print("Enter height and breadth of triangle")
h=int(input())
b1=int(input())
print("Enter side of square")
s=int(input())
print("Area of Rectanle:::",recArea(l,b))
print("Area of Trianlge:::",triArea(h,b1))
print("Area of Square:",squareArea(s))


# In[4]:


# 2) Count the number of characters (character frequency) in a string. 

string=input("Enter the String :")
s=0
for i in string:
    s=s+1
print("String is ",string,"Frequency=",s)


# In[6]:


# 3) Add ‘ing’ at the end of a given string. If it already ends with ‘ing’, then add ‘ly’

string=input("Enter the String :")
if string.endswith('ing'):
    str1=string+'ly'
else:
    str1=string+'ing'
print("New String:",str1)


# In[8]:


# 4) Accept a list of words and return length of longest word.


word=input("Enter the Word ").split()
li={}
for i in word:
    li[i]=len(i)
    v=list(li.values())
    k=list(li.keys())
print("Longest String is:",k[v.index(max(v))],"Length:",max(v))


# In[ ]:




