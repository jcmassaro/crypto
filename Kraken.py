import requests
import pandas as pd
import time
from time import sleep
import csv
from datetime import datetime
import os

os.chdir('/Users/JohnMassaro/Desktop')


#Functions below return data from Kraken BTC exchange. Data is packed into dictionaries inside lists inside dictionaries, etc. Functions unpack nested items and convert desired string into float object 


#parse the data into a list, which can be used each time the functions are called
def parse_data(request):
        json = request.json()
        values = json.values()
        values_list = [*values]
        XBT = values_list[1]
        XBT_values = XBT.values()
        XBT_values_list = [*XBT_values]
        data_dict = XBT_values_list[0]
        data_dict_values = data_dict.values()
        data_list = [*data_dict_values]
        return data_list


#Get and return BTC ask price from Kraken
#Return as float 
def ask_price(data_list):        
        return float(data_list[0][0])
                
#Get and return BTC bid price from Kraken
#Return as float
def bid_price(data_list):     
        return float(data_list[1][0])

                
#Get and return BTC last trade closed from Kraken
def last_trade_closed(data_list):
        return float(data_list[2][0])                
                
#Get and return BTC volume today from Kraken
#Return as float
def volume_today(data_list):       
        return float(data_list[3][0])
                
#Get and return BTC 24 hour volume from Kraken
#Return as float
def volume_24(data_list):
        return float(data_list[3][1])
        
                
#Get and return BTC price today from Kraken
#Return as float
def volume_price_today(data_list):      
        return float(data_list[4][0])                
                
#Get and return BTC 24 hour price from Kraken
#Return as float
def volume_price_24(data_list):      
        return float(data_list[4][1])        
                
#Get and return BTC number of trades today from Kraken
#Return as float
def trade_numbers_today(data_list):
        return float(data_list[5][0])                
        
        
#Get and return BTC 24 hour number of trades from Kraken
#Return as float
def trade_numbers_24(data_list): 
        return float(data_list[5][1])
                
                
#Get and return BTC low today from Kraken
#Return as float
def low_today(data_list):
        return float(data_list[6][0])


#Get and return BTC 24 hour low from Kraken
#Return as float
def low_24(data_list):
        return float(data_list[6][1])
                
        
#Get and return BTC high today from Kraken
def high_today(data_list):
        return float(data_list[7][0])
                
                
#Get and return BTC 24 hour highfrom Kraken
#Return as float
def high_24(data_list):    
        return float(data_list[7][1])

        
#print results from above and now time -- WORKS
# def print_cases():
#         while True:
#                 print(ask_price())
#                 print(datetime.now())
#                 print('------------')
#                 time.sleep(1)
# print_cases()

#write results to csv continuously
#ISSUE -- WRITES SAME NUMBERS OVER AND OVER TO CSV
def write_to_csv():
        #establishing column headers 
        columns = ['Ask Price', 'Bid Price', 'Last Trade Closed', 'Volume Today', 'Volume Last 24 Hours', 'Price Today', 'Price Last 24 Hours', \
                   'Number of Trades Today', 'Number of Trades Last 24 Hours', 'Low Today', 'Low Last 24 Hours', 'High Today', 'High Last 24 Hours', 'Time']

        #write headers
        with open('BTC.csv', 'a') as file:
                writer = csv.writer(file)
                writer.writerow(columns)

                while True:
                        #make new request every 3 seconds, save the result of requested data as a list, then 
                        request = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
                        data_list = parse_data(request)

                        #putting function output data into list so I can write to CSV
                        final_data = [ask_price(data_list), bid_price(data_list), last_trade_closed(data_list), volume_today(data_list), volume_24(data_list), volume_price_today(data_list),volume_price_24(data_list), \
                                        trade_numbers_today(data_list), trade_numbers_24(data_list), low_today(data_list), low_24(data_list), high_today(data_list), high_24(data_list), str(datetime.now())]

                        #write function data output data to CSV
                        writer.writerow(final_data)
                        print(final_data)
                        time.sleep(3)
                   


#write_to_csv()
 
ask_price_list = []
while True:
    request = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
    data_list = parse_data(request)
    
    
    ask_price_list.append(int(ask_price(data_list)))
    print(ask_price_list)

    for i in range(1):
        if ask_price_list[i-1] < ask_price_list[i]:
            print('Dip')
        elif ask_price_list[i-1] > ask_price_list[i]:
            print('Bump')
        else:
            print('No change')
        

    
            

    time.sleep(3)  


    
