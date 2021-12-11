
from api_helper import NorenApiPy
import logging
import yaml

#enable dbug to see request and responses
logging.basicConfig(level=logging.DEBUG)

#start of our program
api = NorenApiPy()

#credentials
with open('cred.yml') as f:
    cred = yaml.load(f, Loader=yaml.FullLoader)
    print(cred)

ret = api.login(userid = cred['user'], password = cred['pwd'], twoFA=cred['factor2'], vendor_code=cred['vc'], api_secret=cred['apikey'], imei=cred['imei'])

ret = api.place_order(buy_or_sell='B', product_type='C',
                        exchange='NSE', tradingsymbol='INFY-EQ', 
                        quantity=1, discloseqty=0,price_type='SL-LMT', price=1500.00, trigger_price=1490.00,
                        retention='DAY', remarks='my_order_001')

print(ret)

orderno = ret['norenordno']

ret = api.modify_order(exchange='NSE', tradingsymbol='INFY-EQ', orderno=orderno,
                                   newquantity=2, newprice_type='SL-LMT', newprice=1505.00, newtrigger_price=1495.00)


print(ret)

ret = api.single_order_history(orderno=orderno)

for ord in ret:
    
    print(f"{ord['qty']} prc: {ord['prc']} trgprc: {ord['trgprc']} {ord['rpt']}")



