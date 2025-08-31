#!/usr/bin/env python
# coding: utf-8

# # STEP 1: Ask Phase – Defining the Business Task  
# 
# **Business Task:**  
# Analyze Fitbit smart device usage data to discover insights about user activity, sleep, and wellness that can inform Bellabeat’s marketing strategy and guide how their products can encourage healthier lifestyles.  
# 
# **Key Questions:**  
# 1. What are the patterns in daily activity, sleep, and calorie burn among users?  
# 2. How does activity intensity (steps, active minutes) relate to calories burned?  
# 3. Do users with more consistent sleep patterns engage in more daily activity?  
# 4. How do different user segments (low, medium, high activity) behave?  
# 5. What opportunities exist for Bellabeat to use these insights in product development and marketing campaigns?  
# 
# **Deliverables:**  
# - A cleaned dataset prepared for analysis.  
# - Exploratory data analysis (EDA) and visualizations showing trends and relationships.  
# - Key insights and actionable recommendations for Bellabeat’s strategy. 

# 
# 

# # STEP 2: Prepare Phase – Understanding the Data  
# 
# **Dataset Source:**  
# This dataset is the *FitBit Fitness Tracker Data* available on Kaggle. It includes personal fitness tracking data from 30 Fitbit users, generated via surveys and data logs.  
# 
# **Data Files Used:**  
# - `dailyActivity_merged.csv` → daily activity (steps, distances, calories, minutes)  
# - `sleepDay_merged.csv` → sleep logs (minutes asleep, time in bed)  
# - `weightLogInfo_merged.csv` → weight logs (kg, pounds, BMI, date)  
# 
# **Timeframe:**  
# - The data covers a short period of 2 months in 2016.  
# 
# **Limitations:**  
# - Small sample size (only 30 users).  
# - Data is self-reported by participants, which may affect accuracy.  
# - Limited timeframe (only 2 months).  
# - Not representative of Bellabeat’s entire customer base.

# # Import libraries

# In[46]:


import pandas as pd


# In[47]:


import matplotlib.pyplot as plt


# In[48]:


import seaborn as sns


# In[49]:


import numpy as np


# ## LOADING THE DATASET 

# In[50]:


base_path = r"C:\Users\computer1\Desktop\Fitabase_Data"
activity = pd.read_csv(base_path + r"\dailyActivity_merged.csv")
calories = pd.read_csv(base_path + r"\dailyCalories_merged.csv")
intensities = pd.read_csv(base_path + r"\dailyIntensities_merged.csv")
steps = pd.read_csv(base_path + r"\dailySteps_merged.csv")
sleep = pd.read_csv(base_path + r"\sleepDay_merged.csv")
weight = pd.read_csv(base_path + r"\weightLogInfo_merged.csv")
datasets = {
    "activity": activity,
    "calories": calories,
    "intensities": intensities,
    "steps": steps,
    "sleep": sleep,
    "weight": weight
}


# In[51]:


for name, df in datasets.items():
    print(f"{name}: {df.shape} columns={list(df.columns)}\n")


# ## STEP 3: Process Phase – Data Cleaning
# 
# Objective:
# Prepare the dataset for analysis by handling errors, duplicates, missing values, and ensuring consistency.
# 
# Steps in Cleaning:
# 
# Import necessary Python libraries (Pandas, NumPy).
# 
# Load the datasets (dailyActivity_merged.csv, sleepDay_merged.csv, weightLogInfo_merged.csv).
# 
# Check the structure of each dataset (rows, columns, data types).
# 
# Standardize column names for readability.
# 
# Identify and remove duplicates.
# 
# Handle missing or null values.
# 
# Ensure date columns are in proper datetime format.
# 
# Merge datasets where needed (e.g., activity + sleep).
# 
# Goal:
# Ensure the datasets are clean, consistent, and analysis-ready so that we can extract accurate insights in the next phase.

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




