from NorenRestApiPy.NorenApi import PriceType, BuyorSell, ProductType
from api_helper import NorenApiPy, get_time
import logging
import hashlib

logging.basicConfig(level=logging.DEBUG)

#start of our program
api = NorenApiPy()

#credentials
user        = '< user id>'
u_pwd       = '< password >'
factor2     = 'second factor'
vc          = 'vendor code'
api_secret  = 'secret key'
imei        = 'uniq identifier'

u_app_key='{0}|{1}'.format(user,api_secret)

#Convert to SHA 256 for password and app key
pwd = hashlib.sha256(u_pwd.encode('utf-8')).hexdigest()
app_key=hashlib.sha256(u_app_key.encode('utf-8')).hexdigest()

ret = api.login(userid=user, password=pwd, twoFA=factor2, vendor_code=vc, api_secret=app_key, imei=imei)
print(ret)