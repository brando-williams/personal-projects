# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 13:27:16 2025

@author: brand
"""

import requests
import json
import csv
import datetime

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

def save_to_csv(data, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Timestamp', 'Average High Price', 'Average Low Price', 'High Price Volume', 'Low Price Volume'])
        for entry in data:
            try:
                timestamp = datetime.datetime.fromtimestamp(entry['timestamp'])
                writer.writerow([timestamp, entry['avgHighPrice'], entry['avgLowPrice'], entry['highPriceVolume'], entry['lowPriceVolume']])
            except Exception as e:
                print(f"Error processing entry: {entry}")
                print(e)

item_id = 19669
historical_data = hist_ge_price(item_id)

if historical_data:
    save_to_csv(historical_data, 'redwood_logs_example.csv')
    print('Data saved to redwood_logs_example.csv')
else:
    print("Failed to retrieve price data")
    
### https://prices.runescape.wiki/osrs/faqs