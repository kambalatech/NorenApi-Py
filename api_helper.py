from NorenRestApiPy.NorenApi import  NorenApi
from threading import Timer
import pandas as pd
import time

class SymbolItem:
    def __init__(self):
        self.df = None
        self.key = None
        self.counter  = 0
        self.lasttime = 0    

def get_time(time_string):
    data = time.strptime(time_string,'%d-%m-%Y %H:%M:%S')

    return time.mktime(data)


class NorenApiPy(NorenApi):
    def __init__(self):
        NorenApi.__init__(self, host='http://rama.kambala.co.in/NorenWClient/', websocket='ws://rama.kambala.co.in:5551/NorenWS/', eodhost='http://kurma.kambala.co.in/chartApi/getdata/')

    
    