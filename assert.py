#!/usr/bin/env python
# coding: utf-8

# In[1]:


chars = ["Alpha" ,"Beta" ,"Gamma" ,"Delta" ,"Epsilon"]
def display(elem):
	assert type(elem) is int , "Argument Must Be Integer!"												
	print("List Element" , elem , "=" , chars[elem])
elem = 4 
display(elem)
elem = elem / 2 
display(elem)    


# In[ ]:




