#!/usr/bin/env python
# coding: utf-8

# In[7]:


a = 10 
b = 5 
print( "a =" , a , "\tb = " , b	)
#1010 ^	0101 = 1111 (decimal 15) 
a = a ^	b  
# 1111 ^ 0101 =	1010 (decimal 10) 
b = a ^	b 
#1111 ^	1010 = 0101 (decimal 5) 
a = a ^ b
print( "a =" , a , "\tb = " , b )


# In[ ]:




