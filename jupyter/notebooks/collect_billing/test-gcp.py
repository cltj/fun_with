from config import My_Config as cfg
import requests
import os


from google.oauth2 import id_token
from google.auth.transport import requests

token = id_token.fetch_id_token(requests.Request(), cfg.google_application_credentials())
print(token)

#billing_accounts = requests.get(
#    url='https://cloudbilling.googleapis.com/v1/billingAccounts', 
#    headers=[
#        {'scope':'https://www.googleapis.com/auth/cloud-billing', 
#        'auth':cfg.google_application_credentials()}
#        ]
#    )
#
#print(billing_accounts.json())

