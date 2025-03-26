# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 15:57:54 2025

@author: brand
"""

import requests
import json
import csv
import datetime
import pandas as pd

user_agent = 'DataScienceExampleProject/1.0 (Contact: brando.williams.m@gmail.com)'

# Function to retrieve GE prices for a specific item ID

def hist_ge_price(item_id):
    headers = {
        'User-Agent': user_agent
        }
    url = f"https://prices.runescape.wiki/api/v1/osrs/timeseries?timestep=24h&id={item_id}"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data.get('data', [])
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

def save_to_csv(data, item_id, all_data):
        for entry in data:
            try:
                timestamp = datetime.datetime.fromtimestamp(entry['timestamp'])
                all_data.append([item_id, timestamp, entry['avgHighPrice'], entry['avgLowPrice'], entry['highPriceVolume'], entry['lowPriceVolume']])
            except Exception as e:
                print(f"Error processing entry: {entry}")
                print(e)


#Normal Plank: 960
#Oak Plank: 8778
#Teak Plank: 8780
#Mahogany Plank: 8782

item_ids = [960, 8778, 8780, 8782]
all_data = []

for i in item_ids:
    historical_data = hist_ge_price(i)
    if historical_data:
        save_to_csv(historical_data, i, all_data)
        print(f"Data saved for: {i}")
    else:
        print(f"Failed to retrieve data for: {i}")
 
df = pd.DataFrame(all_data, columns=['Item ID', 'Timestamp', 'Average High Price', 'Average Low Price', 'High Price Volume', 'Low Price Volume']) 

# Create a mapping dictionary 
plank_names = { 960: 'Normal Plank', 8778: 'Oak Plank', 8780: 'Teak Plank', 8782: 'Mahogany Plank' } 
# Use the map function to replace item IDs with plank names 
df['Item ID'] = df['Item ID'].map(plank_names)
    
# Save to an Excel file 
df.to_excel('plank_data.xlsx', index=False) 
print('Data saved to plank_data.xlsx') 
### https://prices.runescape.wiki/osrs/faqs