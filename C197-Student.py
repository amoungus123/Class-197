#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('Name: ')
print('Clean the data and then plot a heatmap which displays the extereme UVB value throughout the day of every month in 2015 in northern taiwan')
print('Then plot a heatmap which displays amount of Carbon monoxide release throughout the day every of month in 2015 in northern taiwan')
print('Then plot a heatmap which displays amount of sulfur dioxide release throughout the day every of month in 2015 in northern taiwan')
print('Plot both Corbon monoxide and sulfure dioxide plots beside each other to compare and find which month during which time had the most clean air in northern taiwan')


# # Activity 1- Plot a heatmap to show maximum UVB value throughout various different times of the day

# In[2]:


#predefine code for image
from IPython.display import Image
Image(filename='UV.png') 
#predefine code end


# In[3]:


# Import all the libraries and read 2015_Air_quality_in_northern_Taiwan.csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

dataframe = pd.read_csv('2015_Air_quality_in_northern_Taiwan.csv')
dataframe


# In[4]:


# Create a new column which displays the month and time extracted from the time column
dataframe['month'] = pd.DatetimeIndex(dataframe['time']).month
dataframe['time_hours'] = pd.DatetimeIndex(dataframe['time']).time

dataframe


# In[5]:


# Clean the data by replacing the null, 0 and values ending with # to nan values
dataframe.replace( '', float('nan') ,inplace=True)
dataframe.replace( '0', float('nan') ,inplace=True)
dataframe.replace('.#$', float('nan') ,inplace=True, regex=True)
dataframe.replace('.x$', float('nan') ,inplace=True, regex=True)
df = dataframe.dropna()
df


# In[6]:


# Set the type of 'UVB' column to float
df['UVB'] = df['UVB'].astype(float)
df['UVB'].dtypes


# In[7]:


#groupby the month and time for getting the maximum of UVB value
new_dataframe = df.groupby(['month','time_hours'])['UVB'].max().reset_index()
new_dataframe


# In[8]:


# Plot a heatmap to show the UV value for through various times of the day 

plt.figure(figsize=(10,8))
heatmap_df = pd.pivot_table(values ='UVB', index ='time_hours',  
                    columns ='month', data = new_dataframe)
sns.heatmap(heatmap_df, cmap ='plasma') 


# Conclusion - In the month of 5th to 8th (i.e from May to August) at the time between 11 am to 1 pm, the UVB rays can affect people the most and may lead to sun burn and skin cancer.

# # Activity 2 Plot a heatmap to show when the air was most clean as per release of Carbon monoxide and Sulfur dioxide at various different times of the day
# 
# 

# Carbon monoxide - is a colorless, odorless, and tasteless flammable gas that is slightly less dense than air. It is an toxic air. 
# 
# Sulfur dioxide - It is a toxic gas responsible for the smell of burnt matches. 

# In[9]:


#predefine code for image
from IPython.display import Image
Image(filename='air.jpg') 
#predefine code end


# In[10]:


# Clean the data by replacing the null, 0 and values ending with x to nan values
dataframe.replace( '', float('nan') ,inplace=True)
dataframe.replace( '0', float('nan') ,inplace=True)
dataframe.replace('.#$', float('nan') ,inplace=True, regex=True)
dataframe.replace('.x$', float('nan') ,inplace=True, regex=True)
df = dataframe.dropna()
df


# In[11]:


# Set the type of 'SO2' column to float 
df['SO2'] = df['SO2'].astype(float)
df['SO2'].dtypes


# In[12]:


# Set the type of 'CO' column to float 
df['CO'] = df['CO'].astype(float)
df['CO'].dtypes




# In[13]:


#Groupby the month and time for getting the maximum of CO and SO2
final_dataframe = df.groupby(['month', 'time_hours'])['CO', 'SO2'].max().reset_index()
final_dataframe



# In[14]:


# Plot a heatmap to show the the amount of carbon monoxide release through various different times of the day 
plt.figure(figsize=(10,8))
heatmap_df_co = pd.pivot_tables(values = 'CO', index ='time_hours', columns ='month', data = final_dataframe)
sns.heatmap(heatmap_df_co. cmap = 'plasma')


# Conclusion - In the month of 3th to 7th (i.e from March to July) between 12 pm to 2 pm the air contained least amount of Carbon monoxide

# In[ ]:


# Plot a heatmap to show the amount Sulfur dioxide released through various different times of the day 
plt.figure(figsize=(10,8))
heatmap_df_so2 = pd.pivot_tables(values = 'SO2', index ='time_hours', columns ='month', data = final_dataframe)
sns.heatmap(heatmap_df_so2. cmap = 'plasma')



# Conclusion - 

# In[ ]:


# plot both the amount of carbon monoxide and sulfur dioxide released during different hours of the day
# and find the time and month during which both the gases where at its minimum which is clean air
fig, (ax1, ax2) = plt.subplots(ncols=2,figsize=(15,7))

sns.heatmap(heatmap_df_so2, cmap = 'plama', ax=ax1)
ax1.title.set_text('SO2')
sns.heatmap(heatmap_df_co, cmap = 'plama', ax=ax2)
ax1.title.set_text('CO')





# Conclusion -

# In[ ]:




