import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api_helper import NorenApiPy
import datetime
import logging
import time
import yaml
import pandas as pd

#sample
logging.basicConfig(level=logging.DEBUG)

#flag to tell us if the websocket is open
socket_opened = False

#application callbacks
def event_handler_order_update(message):
    print("order event: " + str(message))


SYMBOLDICT = {}
def event_handler_quote_update(inmessage):
    global SYMBOLDICT


    #feedtime in string 
    feedtime = int(inmessage['ft'])
    inmessage['feedtime'] = str(datetime.datetime.fromtimestamp( feedtime ))
    print("quote event: {0}".format(time.strftime('%d-%m-%Y %H:%M:%S')) + str(inmessage))

    symbol = inmessage['e'] + '|' + inmessage['tk']

    new_df = pd.DataFrame([inmessage])
    if symbol in SYMBOLDICT:
        #new update message (inmessage) might not include all fields, 
        #you can merge the new data with the previous data. 
        #If a field is missing in the new data, the previous value should be retained.
        # Retrieve the last row (latest data) from the existing DataFrame
        last_row = SYMBOLDICT[symbol].iloc[-1].copy()
        # Update the last row with any new data provided in `inmessage`
        for key, value in inmessage.items():
            last_row[key] = value

        new_upd_df = pd.DataFrame([last_row])

        # If the symbol already exists, append the new data
        SYMBOLDICT[symbol] = pd.concat([SYMBOLDICT[symbol], new_upd_df], ignore_index=True)
    else :
        SYMBOLDICT[symbol] = new_df

    print(SYMBOLDICT[symbol])
  
def open_callback():
    global socket_opened
    socket_opened = True
    print('app is connected')
    
    api.subscribe('NSE|1594', feed_type='d')
    #api.subscribe(['NSE|22', 'BSE|522032'])

#end of callbacks

def get_time(time_string):
    data = time.strptime(time_string,'%d-%m-%Y %H:%M:%S')

    return time.mktime(data)

#start of our program
api = NorenApiPy()

#yaml for parameters
with open('..\\cred.yml') as f:
    cred = yaml.load(f, Loader=yaml.FullLoader)
    print(cred)

ret = api.login(userid = cred['user'], password = cred['pwd'], twoFA=cred['factor2'], vendor_code=cred['vc'], api_secret=cred['apikey'], imei=cred['imei'])

if ret != None:   
    ret = api.start_websocket(order_update_callback=event_handler_order_update, subscribe_callback=event_handler_quote_update, socket_open_callback=open_callback)
    
    while True:
        if socket_opened == True:
            print('q => quit')
            prompt1=input('what shall we do? ').lower()    

            print('Fin') #an answer that wouldn't be yes or no
            break   

        else:
            continue

    