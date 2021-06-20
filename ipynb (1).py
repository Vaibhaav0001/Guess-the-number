#!/usr/bin/env python
# coding: utf-8

# In[13]:


#GUESS THE NUMBER
import random
print("*** GUESS THE NUMBER ***")
print("You will be given 3 chances to guess the number")
print("Enter range from which you want to select")
n=int(input())
print("To")
m=int(input())

flag=0
no=random.randint(n,m)
for i in range(1,4):
    
    print("Guess your",i,"attempt")
    c=int(input())
    if no==c:
        print("Congrats you won in your",i,"attempt!!!")
        flag=1
        break
    else:
        print("Wrong guess!You lose your",i,"attempt")
        flag=0
if flag:
     print("$$$ You are a Champion $$$")
else:
    print("Better try next time")
    print("The number was",no)
   
        


# ### 
