#!/usr/bin/env python
# coding: utf-8

# In[1]:


title ="Python In Easy Steps"
try:												
	print(titel)
except NameError as msg:												
	print(msg)
day = 32
try:												
	if day > 31:																				
		raise ValueError("Invalid Day Number")												
	#More statements to execute get	added here. 
except ValueError as msg:												
	print("The Program found An" , msg) 
finally	:												
	print("But Today Is Beautiful Anyway.") 


# In[ ]:




