from NorenRestApiPy.NorenApi import PriceType, BuyorSell, ProductType
from api_helper import NorenApiPy, get_time

import datetime
import logging
import time
import yaml
import pandas as pd
import hashlib

logging.basicConfig(level=logging.DEBUG)

#start of our program
api = NorenApiPy()

#credentials
user    = <uid>
pwd     = <password>
factor2 = <2nd factor>
vc      = <vendor code>
apikey  = <secret key>
imei    = <imei>

#Convert to SHA 256 for password and app key
pwd = hashlib.sha256(u_pwd.encode('utf-8')).hexdigest()
app_key=hashlib.sha256(u_app_key.encode('utf-8')).hexdigest()

ret = api.login(userid=uid, password=pwd, twoFA=factor2, vendor_code=vc, api_secret=app_key, imei=imei)
print(ret)