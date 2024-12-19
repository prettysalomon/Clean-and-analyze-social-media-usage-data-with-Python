#!/usr/bin/env python
# coding: utf-8

# # Clean & Analyze Social Media

# ## Introduction
# 
# Social media has become a ubiquitous part of modern life, with platforms such as Instagram, Twitter, and Facebook serving as essential communication channels. Social media data sets are vast and complex, making analysis a challenging task for businesses and researchers alike. In this project, we explore a simulated social media, for example Tweets, data set to understand trends in likes across different categories.
# 
# ## Prerequisites
# 
# To follow along with this project, you should have a basic understanding of Python programming and data analysis concepts. In addition, you may want to use the following packages in your Python environment:
# 
# - pandas
# - Matplotlib
# - ...
# 
# These packages should already be installed in Coursera's Jupyter Notebook environment, however if you'd like to install additional packages that are not included in this environment or are working off platform you can install additional packages using `!pip install packagename` within a notebook cell such as:
# 
# - `!pip install pandas`
# - `!pip install matplotlib`
# 
# ## Project Scope
# 
# The objective of this project is to analyze tweets (or other social media data) and gain insights into user engagement. We will explore the data set using visualization techniques to understand the distribution of likes across different categories. Finally, we will analyze the data to draw conclusions about the most popular categories and the overall engagement on the platform.
# 
# ## Step 1: Importing Required Libraries
# 
# As the name suggests, the first step is to import all the necessary libraries that will be used in the project. In this case, we need pandas, numpy, matplotlib, seaborn, and random libraries.
# 
# Pandas is a library used for data manipulation and analysis. Numpy is a library used for numerical computations. Matplotlib is a library used for data visualization. Seaborn is a library used for statistical data visualization. Random is a library used to generate random numbers.

# In[6]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random


# In[7]:


# Simulate social media data
random.seed(42)  # For reproducibility
categories = ['Tech', 'Health', 'Sports', 'Politics', 'Entertainment']
data = {
    'Category': [random.choice(categories) for _ in range(1000)],
    'Likes': [random.randint(0, 500) for _ in range(1000)],
    'Shares': [random.randint(0, 100) for _ in range(1000)],
    'Comments': [random.randint(0, 50) for _ in range(1000)],
}

# Create a DataFrame
social_media_df = pd.DataFrame(data)


# In[8]:


# View the first few rows
print(social_media_df.head())

# Basic information
print(social_media_df.info())

# Descriptive statistics
print(social_media_df.describe())


# In[9]:


# Check for missing values
print(social_media_df.isnull().sum())


# In[10]:


plt.figure(figsize=(10, 6))
sns.histplot(social_media_df['Likes'], kde=True, bins=30, color='blue')
plt.title('Distribution of Likes', fontsize=16)
plt.xlabel('Likes', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.show()


# In[11]:


plt.figure(figsize=(10, 6))
sns.barplot(x='Category', y='Likes', data=social_media_df, ci=None, palette='viridis')
plt.title('Average Likes by Category', fontsize=16)
plt.xlabel('Category', fontsize=12)
plt.ylabel('Average Likes', fontsize=12)
plt.show()


# In[12]:


plt.figure(figsize=(8, 6))
sns.heatmap(social_media_df[['Likes', 'Shares', 'Comments']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap', fontsize=16)
plt.show()


# In[13]:


print(social_media_df.groupby('Category')['Likes'].mean().sort_values(ascending=False))


# In[14]:


social_media_df['Engagement'] = social_media_df['Likes'] + social_media_df['Shares'] + social_media_df['Comments']
print(social_media_df.groupby('Category')['Engagement'].mean().sort_values(ascending=False))


# In[15]:


plt.figure(figsize=(10, 6))
sns.boxplot(x='Category', y='Engagement', data=social_media_df, palette='Set2')
plt.title('Engagement Distribution by Category', fontsize=16)
plt.xlabel('Category', fontsize=12)
plt.ylabel('Engagement', fontsize=12)
plt.show()


# In[ ]:




