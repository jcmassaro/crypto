import requests
import pandas as pd
import time
from time import sleep
import csv
from datetime import datetime
import os
from twilio.rest import Client

os.chdir('/Users/JohnMassaro/Desktop')

#Loading in Twilio data to send SMS alert
account = 'XXXXXXX'
token = 'XXXXXX'
client = Client(account, token, region = 'us1', edge = 'ashburn')




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
def print_askPriceInfo(ask_price_info_dict):
      print("last: ", ask_price_info_dict["last"],
            "\nhigh: ", ask_price_info_dict["high"], 
            "\nlow: ",  ask_price_info_dict["low"])      
      print()

        

        
isAskPriceSet = False
ask_price_info_dict = {"low":-1, "high":-1, "last":-1}

while True:
    request = requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')
    data_list = parse_data(request)
    curr_askPrice = int(ask_price(data_list))

    #set initial ask price details 
    if (not isAskPriceSet):
      ask_price_info_dict["low"]     = curr_askPrice
      ask_price_info_dict["high"]    = curr_askPrice
      ask_price_info_dict["last"]    = curr_askPrice
      isAskPriceSet = True
      print_askPriceInfo(ask_price_info_dict)


    #save data from subsequent requests
    if (curr_askPrice < ask_price_info_dict["low"]):
      ask_price_info_dict["low"]  = curr_askPrice
    if (curr_askPrice > ask_price_info_dict["high"]):
      ask_price_info_dict["high"] = curr_askPrice


    #keep track of dips/bumps
    if (ask_price_info_dict["last"] < curr_askPrice):
      print("\n[--------------- bump ---------------]")
    if (ask_price_info_dict["last"] > curr_askPrice):
      print("\n[--------------- dip ---------------]")
    if (ask_price_info_dict["last"] == curr_askPrice):
      print("...")
    else:
      ask_price_info_dict["last"] = curr_askPrice
      print_askPriceInfo(ask_price_info_dict)             

    time.sleep(3)  


#piece to look at % dip from ATH 
    if isAskPriceSet == True:
      all_time_high_price = ask_price_info_dict["high"]
      print('ATH:', all_time_high_price)
      dip_calc = ((all_time_high_price - curr_askPrice)/curr_askPrice)*100
      if dip_calc >= .001:
        print('Dip of ' + str(dip_calc) +'%')
        message = client.messages.create(to='XXXXXX', from_='XXXXX', body = 'Bitcoin is at a ' + str(dip_calc) + '%' + ' dip.')
        time.sleep(600)

