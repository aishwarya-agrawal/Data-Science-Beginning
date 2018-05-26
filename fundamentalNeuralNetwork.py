
# coding: utf-8

# In[91]:


import numpy as np


# In[92]:


def relu(input):
    output = max(input,0)
    return output


# In[93]:


input_data = np.array([2,3])


# In[94]:


weights = {'node_0':np.array([1,1]),
          'node_1':np.array([-1,1]),
          'output':np.array([2,-1])
         }


# In[95]:


node_0_input = (input_data * weights['node_0']).sum()
node_0_output = relu(node_0_input)


# In[96]:


node_1_input = (input_data * weights['node_1']).sum()
node_1_output = relu(node_1_input)


# In[97]:


hidden_layer_values = np.array([node_0_value,node_1_value]) 


# In[98]:


output_input = (hidden_layer_values * weights['output']).sum()
output_output = relu(output_input)


# In[99]:


print(output_output)

