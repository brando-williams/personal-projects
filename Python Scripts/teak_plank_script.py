# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 15:57:55 2025

@author: brand
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns

# Load dataset into Spyder
df = pd.read_csv('teak_plank_example.csv', header=0)

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
plt.title('Average Buy Price Distribution from 2024-2025')
plt.xlabel('Instant Buy Price')
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
plt.title('Average Buy Price for a Teak Plank from 2024-2025')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()

# Plot the distribution of numerical features
plt.figure(figsize=(12,6))
sns.histplot(df['Average Low Price'], kde=True)
plt.title('Average Sell Price Distribution')
plt.xlabel('Instant Sell Price')
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
plt.title('Average Sell Price for Teak Plank from 2024-2025')
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
plt.title('Difference between Buy and Sell Price from 2024-2025')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()

print(df.loc[df['Difference'] < 0])

df['ROI'] = (df['Difference'] / df['Average Low Price']) * 100

sns.lineplot(data=df, x='Timestamp', y='ROI')
locator = mdates.MonthLocator()
plt.gca().xaxis.set_major_locator(locator)
formatter = mdates.DateFormatter("%b '%y")
plt.gca().xaxis.set_major_formatter(formatter)
plt.gcf().autofmt_xdate()
plt.title('ROI for Teak Plank from 2024-2025')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()

# What was the average buy and sell volume?
plt.figure(figsize=(12,6))
sns.histplot(df['High Price Volume']/1000, kde=True)
plt.title('Buy Trade Volume Distribution from 2024-2025')
plt.xlabel('Volume')
plt.ylabel('Count')
plt.show()

sns.lineplot(data=df, x='Timestamp', y=(df['High Price Volume']/1000))
plt.axvline(x=event_date1, color='red', linestyle='--', linewidth=1, label='Event 1')
plt.axvline(x=event_date2, color='red', linestyle='--', linewidth=1, label='Event 2')
locator = mdates.MonthLocator()
plt.gca().xaxis.set_major_locator(locator)
formatter = mdates.DateFormatter("%b '%y")
plt.gca().xaxis.set_major_formatter(formatter)
plt.gcf().autofmt_xdate()
plt.title('Average Trade Volume for Buying from 2024-2025')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.show()

plt.figure(figsize=(12,6))
sns.histplot(df['Low Price Volume']/1000, kde=True)
plt.title('Sell Trade Volume Distribution from 2024-2025')
plt.xlabel('Volume')
plt.ylabel('Count')
plt.show()

sns.lineplot(data=df, x='Timestamp', y=(df['Low Price Volume']/1000))
plt.axvline(x=event_date1, color='red', linestyle='--', linewidth=1, label='Event 1')
plt.axvline(x=event_date2, color='red', linestyle='--', linewidth=1, label='Event 2')
locator = mdates.MonthLocator()
plt.gca().xaxis.set_major_locator(locator)
formatter = mdates.DateFormatter("%b '%y")
plt.gca().xaxis.set_major_formatter(formatter)
plt.gcf().autofmt_xdate()
plt.title('Average Trade Volume for Selling from 2024-2025')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.show()

df['Volume_Difference'] = (df['High Price Volume']/1000) - (df['Low Price Volume']/1000)

print(df.loc[df['Volume_Difference'] < 0])

sns.lineplot(data=df, x='Timestamp', y='Volume_Difference')
locator = mdates.MonthLocator()
plt.gca().xaxis.set_major_locator(locator)
formatter = mdates.DateFormatter("%b '%y")
plt.gca().xaxis.set_major_formatter(formatter)
plt.gcf().autofmt_xdate()
plt.title('Volume Difference between Buying and Selling from 2024-2025')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.show()

df['Volume_Difference'].describe().round(2)
