# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 14:23:42 2025

@author: brand
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns

# Load dataset into Spyder
df = pd.read_csv('redwood_logs_example.csv', header=0)

# Change data type of Timestamp from str to dt
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Print first few entries
print(df.head())

# Are there any missing values?
print(df.isnull().sum())

# Are there any duplicate values?
print(df.duplicated().sum())

# Setting style for plots
sns.set(style='whitegrid')

# Plot the distribution of numerical features
plt.figure(figsize=(12,6))
sns.histplot(df['Average High Price'], kde=True)
plt.title('Average High Price Distribution')
plt.xlabel('Price')
plt.ylabel('Count')
plt.show()

event_date1 = pd.to_datetime('2024-08-22 19:00:00')
event_date2 = pd.to_datetime('2024-12-11 19:00:00')
sns.lineplot(data=df, x='Timestamp', y='Average High Price')
plt.axvline(x=event_date1, color='red', linestyle='--', linewidth=1, label='Event 1')
plt.axvline(x=event_date2, color='red', linestyle='--', linewidth=1, label='Event 2')
locator = mdates.MonthLocator()
plt.gca().xaxis.set_major_locator(locator)
formatter = mdates.DateFormatter("%b '%y")
plt.gca().xaxis.set_major_formatter(formatter)
plt.gcf().autofmt_xdate()
plt.title('Average High Price for Redwood Logs from 2024-2025')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()

# Plot the distribution of numerical features
plt.figure(figsize=(12,6))
sns.histplot(df['Average Low Price'], kde=True)
plt.title('Average Low Price Distribution')
plt.xlabel('Price')
plt.ylabel('Count')
plt.show()


sns.lineplot(data=df, x='Timestamp', y='Average Low Price')
plt.axvline(x=event_date1, color='red', linestyle='--', linewidth=1, label='Event 1')
plt.axvline(x=event_date2, color='red', linestyle='--', linewidth=1, label='Event 2')
locator = mdates.MonthLocator()
plt.gca().xaxis.set_major_locator(locator)
formatter = mdates.DateFormatter("%b '%y")
plt.gca().xaxis.set_major_formatter(formatter)
plt.gcf().autofmt_xdate()
plt.title('Average Low Price for Redwood Logs from 2024-2025')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()


#######

df['Difference'] = df['Average High Price'] - df['Average Low Price']


sns.lineplot(data=df, x='Timestamp', y='Difference')
locator = mdates.MonthLocator()
plt.gca().xaxis.set_major_locator(locator)
formatter = mdates.DateFormatter("%b '%y")
plt.gca().xaxis.set_major_formatter(formatter)
plt.gcf().autofmt_xdate()
plt.title('Average Low Price for Redwood Logs from 2024-2025')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()

print(df.loc[df['Difference'] < 0])

df['ROI'] = (df['Difference'] / df['Average Low Price']) * 100
