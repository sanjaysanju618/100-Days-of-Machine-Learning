#!/usr/bin/env python
# coding: utf-8

# In[1]:


from cx_Freeze import setup, Executable


# In[2]:


setup(
    name='Flutter Widgets',
    version='0.1',
    description='These are all the Flutter Widgets',
    executables=[Executable('distthis.py')])


# In[ ]:




