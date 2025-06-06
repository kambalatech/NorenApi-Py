from api_helper import NorenApiPy
import logging
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import yaml

#enable dbug to see request and responses
logging.basicConfig(level=logging.DEBUG)

#start of our program
api = NorenApiPy()

# Load existing YAML data
with open('cred.yml', 'r') as f:
    cred = yaml.load(f, Loader=yaml.FullLoader) or {}

#credentials
apikey_url = api.getOAuthURL(cred['oauth_url'],cred['API_KEY'])
logging.info(apikey_url)

# Redirect the user to the login url saved in apikey_url varibale obtained from api.getOAuthURL function
# Receive the authentication code and from the redirect url after the login.
# Once you have the authentication code, obtain the access_token using the api.getAccessToken function as follows.

auth_code = "your_auth_code_here"
if auth_code == "your_auth_code_here":
    auth_code = input("Enter your auth code here: ")

acc_tok, usrid, ref_tok, actid =  api.getAccessToken(auth_code,cred['SECRET_KEY'],cred['API_KEY'],cred['UID'])
logging.info(f"""\nAccess token is : {acc_tok} \nRefresh token is : {ref_tok} \nUser ID token is : {usrid} \nAccount ID is : {actid} \n""")

# Update values
cred['Access_token'] = acc_tok
cred['Account_ID'] = actid

# Log the updated credentials (optional)
logging.info(cred)

# Write the updated data back to the YAML file
with open('cred.yml', 'w') as f:
    yaml.dump(cred, f)

#make the api call
watchlistname = api.get_watch_list_names()
logging.info(f'watchlistname : {watchlistname}')
