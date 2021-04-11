import requests
import pandas as pd
import time
from time import sleep
import csv
from datetime import datetime
import os

os.chdir('/Users/JohnMassaro/Desktop')


#Functions below return data from Kraken BTC exchange. Data is packed into dictionaries inside lists inside dictionaries, etc. Functions unpack nested items and convert desired string into float object 


#Get and return BTC ask price from Kraken
#Return as float 
def ask_price():        
        while True:
                request = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
                json = request.json()
                values = json.values()
                values_list = [*values]
                XBT = values_list[1]
                XBT_values = XBT.values()
                XBT_values_list = [*XBT_values]
                data = XBT_values_list[0]
                data_values = data.values()
                data_1 = [*data_values]
                Ask_price = float(data_1[0][0])
                return(Ask_price)
                
#Get and return BTC bid price from Kraken
#Return as float
def bid_price():     
        while True:
                request = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
                json = request.json()
                values = json.values()
                values_list = [*values]
                XBT = values_list[1]
                XBT_values = XBT.values()
                XBT_values_list = [*XBT_values]
                data = XBT_values_list[0]
                data_values = data.values()
                data_1 = [*data_values]
                Bid_price = float(data_1[1][0])
                return(Bid_price)
                
                
#Get and return BTC last trade closed from Kraken
def last_trade_closed():
        while True:
                request = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
                json = request.json()
                values = json.values()
                values_list = [*values]
                XBT = values_list[1]
                XBT_values = XBT.values()
                XBT_values_list = [*XBT_values]
                data = XBT_values_list[0]
                data_values = data.values()
                data_1 = [*data_values]
                last_trade_closed = float(data_1[2][0])
                return(last_trade_closed)
                
                
#Get and return BTC volume today from Kraken
#Return as float
def volume_today():       
        while True:
                request = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
                json = request.json()
                values = json.values()
                values_list = [*values]
                XBT = values_list[1]
                XBT_values = XBT.values()
                XBT_values_list = [*XBT_values]
                data = XBT_values_list[0]
                data_values = data.values()
                data_1 = [*data_values]
                volume_today = float(data_1[3][0])
                return(volume_today)
                
        
                
#Get and return BTC 24 hour volume from Kraken
#Return as float
def volume_24():
        while True:
                request = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
                json = request.json()
                values = json.values()
                values_list = [*values]
                XBT = values_list[1]
                XBT_values = XBT.values()
                XBT_values_list = [*XBT_values]
                data = XBT_values_list[0]
                data_values = data.values()
                data_1 = [*data_values]
                volume_24 = float(data_1[3][1])
                return(volume_24)
                
        
                
#Get and return BTC price today from Kraken
#Return as float
def volume_price_today():      
        while True:
                request = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
                json = request.json()
                values = json.values()
                values_list = [*values]
                XBT = values_list[1]
                XBT_values = XBT.values()
                XBT_values_list = [*XBT_values]
                data = XBT_values_list[0]
                data_values = data.values()
                data_1 = [*data_values]
                volume_price_today = float(data_1[4][0])
                return(volume_price_today)
                
        
                
#Get and return BTC 24 hour price from Kraken
#Return as float
def volume_price_24():      
        while True:
                request = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
                json = request.json()
                values = json.values()
                values_list = [*values]
                XBT = values_list[1]
                XBT_values = XBT.values()
                XBT_values_list = [*XBT_values]
                data = XBT_values_list[0]
                data_values = data.values()
                data_1 = [*data_values]
                volume_price_24 = float(data_1[4][1])
                return(volume_price_24)
                
        
                
#Get and return BTC number of trades today from Kraken
#Return as float
def trade_numbers_today():
        while True:
                request = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
                json = request.json()
                values = json.values()
                values_list = [*values]
                XBT = values_list[1]
                XBT_values = XBT.values()
                XBT_values_list = [*XBT_values]
                data = XBT_values_list[0]
                data_values = data.values()
                data_1 = [*data_values]
                trade_numbers_today = float(data_1[5][0])
                return(trade_numbers_today)
                
        
        
#Get and return BTC 24 hour number of trades from Kraken
#Return as float
def trade_numbers_24(): 
        while True:
                request = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
                json = request.json()
                values = json.values()
                values_list = [*values]
                XBT = values_list[1]
                XBT_values = XBT.values()
                XBT_values_list = [*XBT_values]
                data = XBT_values_list[0]
                data_values = data.values()
                data_1 = [*data_values]
                trade_numbers_24 = float(data_1[5][1])
                return(trade_numbers_24)
                
        
                
#Get and return BTC low today from Kraken
#Return as float
def low_today():
        while True:
                request = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
                json = request.json()
                values = json.values()
                values_list = [*values]
                XBT = values_list[1]
                XBT_values = XBT.values()
                XBT_values_list = [*XBT_values]
                data = XBT_values_list[0]
                data_values = data.values()
                data_1 = [*data_values]
                low_today = float(data_1[6][0])
                return(low_today)
                
        
                
#Get and return BTC 24 hour low from Kraken
#Return as float
def low_24():
        while True:
                request = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
                json = request.json()
                values = json.values()
                values_list = [*values]
                XBT = values_list[1]
                XBT_values = XBT.values()
                XBT_values_list = [*XBT_values]
                data = XBT_values_list[0]
                data_values = data.values()
                data_1 = [*data_values]
                low_24 = float(data_1[6][1])
                return(low_24)
                
        
        
#Get and return BTC high today from Kraken
def high_today():
        while True:
                request = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
                json = request.json()
                values = json.values()
                values_list = [*values]
                XBT = values_list[1]
                XBT_values = XBT.values()
                XBT_values_list = [*XBT_values]
                data = XBT_values_list[0]
                data_values = data.values()
                data_1 = [*data_values]
                high_today = float(data_1[7][0])
                return(high_today)
                
        
                
#Get and return BTC 24 hour highfrom Kraken
#Return as float
def high_24():    
        while True:        
                request = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
                json = request.json()
                values = json.values()
                values_list = [*values]
                XBT = values_list[1]
                XBT_values = XBT.values()
                XBT_values_list = [*XBT_values]
                data = XBT_values_list[0]
                data_values = data.values()
                data_1 = [*data_values]
                high_24 = float(data_1[7][1])
                return(high_24)

        
#print results from above and now time -- WORKS
def print_cases():
        while True:
                print(ask_price())
                print(datetime.now())
                print('------------')
                time.sleep(1)
#print_cases()

#write results to csv continuously
#ISSUE -- WRITES SAME NUMBERS OVER AND OVER TO CSV
def write_to_csv():
        
        #establishing column headers 
        columns = ['Ask Price', 'Bid Price', 'Last Trade Closed', 'Volume Today', 'Volume Last 24 Hours', 'Price Today', 'Price Last 24 Hours', \
                   'Number of Trades Today', 'Number of Trades Last 24 Hours', 'Low Today', 'Low Last 24 Hours', 'High Today', 'High Last 24 Hours', 'Time']

        #putting function output data into list so I can write to CSV
        final_data = [ask_price(), bid_price(), last_trade_closed(), volume_today(), volume_24(), volume_price_today(),volume_price_24(), \
                      trade_numbers_today(), trade_numbers_24(), low_today(), low_24(), high_today(), high_24(), datetime.now()]

        #write headers
        with open('BTC.csv', 'w') as file:
                writer = csv.writer(file)
                writer.writerow(columns)

        #write function data output data to CSV
        while True:
            with open('BTC.csv', 'a') as file:
                    writer = csv.writer(file)
                    writer.writerow(final_data)
            time.sleep(3)
                   


write_to_csv()
 
  


    
