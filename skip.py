#!/usr/bin/env python
# coding: utf-8

# In[1]:


bool = True 
if bool:												
	print("Python In Easy Steps" ) 
else	:												
	pass
title = "\nPython In Easy Steps\n"
for char in title:print(char , end ="")
for char in title:											
	if char == "y":																				
		print("*" , end	="")																				
		continue												
	print(char , end ="")
for char in title:												
	if char	== "y":																				
		print("*" , end	="")																				
		pass												
	print(char , end ="")


# In[ ]:




