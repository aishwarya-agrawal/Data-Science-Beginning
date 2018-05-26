
# coding: utf-8


# In[19]:


import pandas as pd
import numpy as np


# In[20]:


#panda with dictionary
d=  { 'name': pd.Series(['Braud','Cummings','Heikkein','Allen'], index =['A','B','C','D']),
     'age' : pd.Series([22,38,26,35], index =['A','B','C','D']),
     'fare': pd.Series([7.25,71.83,8.03], index = ['A','B','D']),
     'survived?' : pd.Series(['False','True','True','False'],index =['A','B','C','D'])}


# In[21]:


df1 = pd.DataFrame(d)


# In[22]:


#panda with numpy array
df = pd.DataFrame(data=np.array([[1,2,3],[4,5,6]],dtype=int),columns=['A','B','C'])


# In[23]:


print(df1)

