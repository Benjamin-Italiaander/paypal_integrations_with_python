#!/usr/bin/python
# this is a really dirty way of getting a acces token if you have your client ID and Client Secret
# the token is valid for 8 houres
import os
import urllib3
import json
import requests
from requests.auth import HTTPBasicAuth
import sys
import io
import subprocess

CLIENT_ID = "longsecretclient id cde"
CLIENT_SECRET = 'long secret'
TOKEN_URL = '"https://api-m.sandbox.paypal.com/v1/oauth2/token"'
headers = ' -H "Content-Type: application/json" '
data = ' -d "grant_type=client_credentials" '

# i pre build my command here
command_var=('curl -s -X POST ' +  TOKEN_URL + ' -u ' + CLIENT_ID + ":" + CLIENT_SECRET + headers + data)

# i execute my command here
paypal = str(subprocess.check_output(command_var, shell=True))

# Here i remove the first two characters from the string
paypal = paypal[2:]

# Here i remove the last one character from the string
paypal = paypal[:-1]

# Loading it insto json
json_str = json.loads(paypal)

# open the access_token key
token=(json_str["access_token"])

#And print the token
print(token)

# Just print the json_str to see more keys


