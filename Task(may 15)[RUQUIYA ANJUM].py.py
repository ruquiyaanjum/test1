#!/usr/bin/env python
# coding: utf-8

# In[1]:


#task1 ( Try to extract data from index one to index 300 with a jump of 3 )

s= "this is My First Python programming class and i am learNING python string and its function"

print(s[1:300:3])


# In[2]:


#task 2 (Try to reverse a string without using reverse function )

print(s[::-1])


# In[3]:


#task 3 ( Try to split a string after conversion of entire string in uppercase ).

print(s.upper())
print(s.split(" "))


# In[4]:


#task4 (try to convert the whole string into lower case)

print(s.lower())


# In[5]:


#task5(Try to capitalize the whole string )

print(s.capitalize())


# In[ ]:


#task6 (Write a diference between isalnum() and isalpha())

* isalnum() is a alphabet + numeric for example "rtyuuuu5677"

* isalpha() is a alphabet character only


# In[7]:


#task7 (Try to give an example of expand tab)

s="Ruquiya\tAnjum\tLearning\ta\tPython Code"
print(s.expandtabs())  #3 spaces.


# In[8]:


#task 8 (Give an example of strip , lstrip and rstrip)
x="   ruquiyaanjum  "
print(x.strip()) # removing the space before and after of string
print(x.lstrip())#removing left side space.
print(x.rstrip()) #right side striping means removing right side space.


# In[9]:


#task9((Replace a string charecter by another charector by taking your own example))

name="ruquiyaanjum"
print(name.replace("r","l")) # here  used replace option and replaced "r" as "l".


# In[10]:


#task 10 (Try  to give a defination of string center function with and exmple )
name = "ruquiya"
print(name.center(30,"s")) #here center is like printing name in between of s character.


# In[ ]:


#task 11 (Write your own definition of compiler and interpretor without copy paste form internet in your own language).
COMPILER: c and c++ are compiled language (high level language),computer works on machine language soo compiler will convert the "c code" to compiler to "machine language".

INTERPRETER : Basically it is instruction (read the line , one by one)(line by line).


# In[ ]:


#task 12 (Python is a interpreted of compiled language give a clear ans with your understanding)

Python is both compiled and interpreter language(partially) , the source code get first get compiled(bytecode) and that bytecode will interpreter in machine languages.Using bytecode(to achieve portability).
run on pvm(python virtual machine).


# In[ ]:


#task 13  ( Try to write a usecase of python with your understanding .)

Usecase of python is: Python used in many fields such as  web development, data science, gaming and scripting(automation).

