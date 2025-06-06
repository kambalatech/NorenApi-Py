import time
import logging
import datetime as dt
import sys
import creds
from pprint import pprint
import pyotp
today = dt.datetime.today().strftime("%b%d")
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api_helper import NorenApiPy
import yaml

#logging.basicConfig(level=logging.DEBUG)
api = NorenApiPy()

creds = {}
creds['user'] = ''
creds['pwd'] = ''
creds['vc'] = ''
creds['api_secret'] = ''
creds['imei'] = 'imei-ka'

token = ''
creds['factor2'] = pyotp.TOTP(token).now()

with open('cred.yml') as f:
    cred = yaml.load(f, Loader=yaml.FullLoader)
    print(cred)

"""
def login():
    _session = api.login(
        userid=creds.get('user'),
        password=creds.get('pwd'),
        vendor_code=creds.get('vc'),
        api_secret=creds.get('api_secret'),
        imei=creds.get('imei'),
        twoFA=creds.get('factor2'),
    )

    if _session and _session["stat"] == "Ok":
        uname = _session["uname"]
        logging.info(f"Logged in as {uname.split()[0]} ({_session['actid']})\n")
        return _session
    else:
        logging.warning("login failed")
        logging.debug(_session)
        sys.exit(1)
"""
injected_headers = api.injectOAuthHeader(cred['Access_token'],cred['UID'],cred['Account_ID'])

def logout():
    if ret := api.logout()["stat"] == "Ok":
        logging.info("Logout success")
    else:
        logging.info("Failed to log out")
        logging.debug(ret)


#login()

tick = time.time()
ret = api.place_order(
    buy_or_sell="B",
    product_type="I",
    exchange="NSE",
    tradingsymbol="MIDCAPETF-EQ",
    quantity=1,
    discloseqty=0,
    price_type="MKT",
    price=0,
    trigger_price=None,
    retention="DAY",
    remarks=f"killswitch_test_latency",
)
tock = time.time()


pprint(ret)
print(f"Time to place order  = {tock-tick}s = {(tock-tick)*1000}ms")
logout()
