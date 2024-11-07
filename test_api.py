from api_helper import NorenApiPy
import logging

#enable dbug to see request and responses
logging.basicConfig(level=logging.DEBUG)

#start of our program
api = NorenApiPy()

#credentials
user    = '0000001'
pwd     = 'Abc@1234'
factor2 = 'AAAAAAAAAA'
vc      = 'NIKHESHP'
app_key = 'test123api'
imei    = 'ag3tbbbb33'

#make the api call
ret = api.login(userid=user, password=pwd, twoFA=factor2, vendor_code=vc, api_secret=app_key, imei=imei)

print(ret)

