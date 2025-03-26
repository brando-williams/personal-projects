# personal-projects

## Portfolio
Collection of side projects involving Old School Runescape.

### Project 1: Web scraping OSRS Wiki for Plank data

#### Scripts: EXAMPLE.py, redwood_logs script.py, teak_plank_pull.py 
**Details**: This script fetches historical price data for items in Old School RuneScape by using their item_id and saves the information into a CSV file. Specifically, using the hist_ge_price function sends a GET request to the RuneScape Wiki API to retrieve time series data, extracting the relevant data field when the request is successful. The script also logs any error messages if the request fails. Different item_id values can be set in the code, such as 19669 for redwood logs, with the output saved to a file named redwood_logs_example.csv. If the data retrieval fails, the script displays an error message.

**Output files**: abby_whip_example.csv, plank_data.xlsx, plank_example.csv, redwood_logs_example.csv, teak_plank_example.csv

#### Script: teak_plank_script.py 
**Details:** This script builds upon the earlier python request scripts and analyzes price and trade volume data for teak planks in Old School Runescape from 2024 to 2025. It loads in the data from the teak_plank_example.csv, converts the timestamp variable from a string to datetime format, and checks for any missing or duplicated entries. Using python libraries like Pandas, Numpy, Matplotlib, and Seaborn, the script visualizes distributions and trends in prices and trade volumes over time. Key events, such as announcements related to OSRS' new skill "Sailing," are marked with vertical lines to highlight their potential impact on buying and selling prices of these planks. The script also calculates metrics like price differences, return on investment, and trade column differences, displaying them through different line plots. By doing so, the script attempts to provide meaningful insights into market trends and support a data-driven exploration of game-related economic activities.
