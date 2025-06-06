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

#application callbacks
#order messages
def event_handler_order_update(message):
    print("order event: " + str(message))

#market ticks 
def event_handler_quote_update(message):
    print("quote event: {0}".format(time.strftime('%d-%m-%Y %H:%M:%S')) + str(message))

#websocket open is success
def event_open_callback():
    print('app is connected')

#websocket errors and disconnect is callbacked here
def event_error_callback(error_msg):
    print(f'socket disconnect {error_msg}')

#end of callbacks

#start of our program
api = NorenApiPy()

#yaml for parameters
with open('..\\cred.yml') as f:
    cred = yaml.load(f, Loader=yaml.FullLoader)
    print(cred)

#ret = api.login(userid = cred['user'], password = cred['pwd'], twoFA=cred['factor2'], vendor_code=cred['vc'], api_secret=cred['apikey'], imei=cred['imei'])
ret = injected_headers = api.injectOAuthHeader(cred['Access_token'],cred['UID'],cred['Account_ID'])

if ret != None:   
    ret = api.start_websocket(order_update_callback=event_handler_order_update, 
                              subscribe_callback=event_handler_quote_update, 
                              socket_open_callback=event_open_callback,
                              socket_error_callback=event_error_callback)
    
    while True:
        print('q => quit')
        prompt1=input('what shall we do? ').lower()    

        print('Fin') #an answer that wouldn't be yes or no
        break   

        
    