import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api_helper import NorenApiPy
import logging
import yaml

#enable dbug to see request and responses
logging.basicConfig(level=logging.DEBUG)

#start of our program
api = NorenApiPy()

#credentials
with open('/home/ubuntu/workspace/daily_price_series/NorenApi-Py/cred.yml') as f:
    cred = yaml.load(f, Loader=yaml.FullLoader)
    print(cred)

ret = api.login(userid = cred['user'], password = cred['pwd'], twoFA=cred['factor2'], vendor_code=cred['vc'], api_secret=cred['apikey'], imei=cred['imei'])

ret =api.get_daily_price_series(exchange="NSE",tradingsymbol="ACC-EQ",startdate="1667297289",enddate="1670231374")
print(ret)