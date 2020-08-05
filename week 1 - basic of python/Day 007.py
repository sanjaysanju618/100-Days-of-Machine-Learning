#!/usr/bin/env python
# coding: utf-8

# ## [Subprocess module](https://youtu.be/5XU-mAZVv4w)

# In[1]:


import subprocess


# In[2]:


subprocess.call('dir', shell=True)


# In[3]:


# Reflected in my CMD....

'''
27-07-2020  07:40 PM    <DIR>          .
27-07-2020  07:40 PM    <DIR>          ..
22-07-2020  07:23 PM                42 .gitignore
27-07-2020  07:38 PM    <DIR>          .ipynb_checkpoints
23-07-2020  07:28 PM                45 csv_file.csv
22-07-2020  07:15 PM            11,278 Day 001.ipynb
22-07-2020  07:14 PM             8,779 Day 002.ipynb
23-07-2020  07:39 PM            12,411 Day 003.ipynb
25-07-2020  06:54 PM            28,586 Day 004.ipynb
25-07-2020  08:18 PM             7,858 Day 005.ipynb
26-07-2020  09:22 PM             6,028 Day 006.ipynb
27-07-2020  07:40 PM               576 Day 007.ipynb
21-06-2020  05:14 PM           274,854 FB_DP.jpg
27-07-2020  07:30 PM    <DIR>          generate Exe
26-07-2020  09:29 PM               106 git_push.bat
25-07-2020  06:50 PM                18 open.bat
21-07-2020  01:13 PM               114 README.md
22-07-2020  07:14 PM                43 save.txt
              14 File(s)        350,738 bytes
               4 Dir(s)  33,598,025,728 bytes free
'''


# In[7]:


output = subprocess.check_output('dir', shell=True)


# In[8]:


output


# ## [Matplotlib Graphing Intro](https://youtu.be/H72jSxkLQHQ)

# In[9]:


from matplotlib import pyplot as plt


# In[13]:


plt.plot([5, 6, 7, 8], [7, 2, 3, 8])
plt.show()


# In[11]:





# In[ ]:




