#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=[ int(x) for x in input("Enter 10 values: ").split() ]
c=[]
aval=[]
b=max(a)
for num in range(1,b+1):
      for i in range(2,num):
          if (num%i)==0:
              break
      else:
          aval.append(num)
for i in a:
    for j in aval:
        if i%j==0: 
           c.append(i)
from collections import Counter
e=Counter(c)
f=e.most_common(1)
f


# In[207]:


lower_num=int(input('Enter your lower number: "'))
upper_num=int(input('Enter your upper number: "'))
a=range(lower_num, upper_num)
aval=[]
b=max(a)
for num in range(1,b+1):
      for i in range(2,num):
          if (num%i)==0:
              break
      else:
          aval.append(num)
c=[]
for i in a:
    for j in aval:
        if i%j==0: 
           c.append(i)
from collections import Counter
e=Counter(c)
f=e.most_common(1)
f


# In[208]:





# In[208]:





# In[208]:





# In[ ]:




