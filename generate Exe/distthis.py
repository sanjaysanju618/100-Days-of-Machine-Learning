#!/usr/bin/env python
# coding: utf-8

# In[1]:


import urllib.request
import re


# In[2]:


google_html = urllib.request.urlopen('https://sanjaysanju618.github.io/100-Days-Of-Flutter-Widgets/')


# In[3]:


respData = google_html.read()


# In[4]:


paras = re.findall(r'alt="(.*?)" width="150"></a>',str(respData))


# In[6]:


for para in paras:
    print('Day', paras.index(para),'-', para)

if(input('\nPress any key to continue . . .')):
	exit()

