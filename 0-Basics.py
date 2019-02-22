
# coding: utf-8

# # Introduction to Python and Jupyter
# 1. sfdsdf
# 1. sdfgsf
# 1. sdfsd

# Good practice to start with hello world:

# In[1]:


print('Hello World!')


# ## Basics

# Dynamically typed, i.e. no declaration required. Strings are arrays of letters.

# In[2]:


x = 5
y = "John"
print(x)
print(y)
print(y[1:3]) # Strings are list of letters, here second and third are selected
print(len(y)) # How long is John's name?


# Indentation for program structure and a comment:

# In[3]:


for i in range(1,10):
    print('Hello, World '+ str(i) + '!')
    # Greet some parallel worlds


# In[5]:


float('2')


# ## Data structures

# ### Lists

# In[9]:


l = ["apple", "banana", "cherry"]
print(l)
print(l[1]) # Print only the second item
l.append('pear') # Append an item
print(l)
print(l[1:3]) # Range of elements
print(l[-1]) # Final element
l[3] = 'orange' # Change item 4
print(l)
l[-1] = "melon"
print(l[-3:-1])


# Loop through lists

# In[12]:


for x in l[0:3:2]:
    print(x)


# Conditional statement based on list

# In[11]:


if "apple" in l:
    print("Yes, 'apple' is in the fruits list")


# List length

# In[14]:


len(l)


# ### Tuples
# Tuples are ordered and unchangeable

# In[15]:


t = ("apple", "banana", "cherry")
print(t)
print(t[1]) # Print only the second item
print(t[1:3]) # Range of elements
print(t[-1]) # Final element


# In[16]:


for x in t:
    print(x)


# ### Sets
# Sets are unordered data structures

# In[19]:


s = {"apple", "banana", "cherry"}
s2 = {"banana", "cherry", "orange"}
s.intersection(s2)


# In[20]:


for x in s.intersection(s2):
    print(x)


# Add items

# In[21]:


s.add('pear')
print(s)


# In[22]:


s.remove('banana')
print(s)


# ### Dictionaries (Dicts)
# Dicts support lookup

# In[23]:


d ={
  "make": "Bombardier",
  "model": "Traxx",
  "power": 5600
}
print(d)


# Access model

# In[24]:


d['model']


# Access power

# In[25]:


d['power']


# Change power

# In[26]:


d['power'] = 4200


# Add item

# In[27]:


d['year'] = 2016
print(d)


# ## Pandas

# In[28]:


import pandas as pd
import numpy as np


# Read list of all stations in Germany

# In[29]:


df = pd.read_csv(
    'http://download-data.deutschebahn.com/static/datasets/haltestellen/D_Bahnhof_2017_09.csv',
    sep = ';', # Separator default is ","
    decimal=",") # Grr


# Inspect import

# In[33]:


df.head()


# Access only a single column:

# In[35]:


df['NAME'].head()


# Names of all long distance stations

# In[36]:


df['VERKEHR'] == 'FV'


# In[37]:


df[df['VERKEHR'] == 'FV']['NAME']


# How many long distance stations are there in Germany?

# In[38]:


df[df['VERKEHR'] == 'FV']['NAME'].count()


# List all stations with Berlin in their name

# In[39]:


df[df['NAME'].str.contains('Berlin')]['NAME']


# Name, Lat and Lon of 'Berlin' Stations

# In[40]:


df2 = df[df['NAME'].str.contains('Berlin')][['NAME','LAENGE', 'BREITE']]
df2.head()


# Find southernmost 'Berlin' station

# In[41]:


df2.sort_values('BREITE', inplace = True)
df2.head()


# Export to JSON format

# In[42]:


df2.to_json('BerlinStations.json')


# Read data from AWS cloud storage (S3)

# In[43]:


df = pd.read_json('https://s3-eu-west-1.amazonaws.com/ifvworkshopdata/emma1000.json')


# In[44]:


df.head()


# In[45]:


df['v']

