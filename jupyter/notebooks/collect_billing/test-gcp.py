from config import My_Config as cfg
import requests
import os
from google.oauth2 import id_token
from google.auth.transport.requests import Request


def auth_gcp():
    credential_path = "/mnt/c/dev/cl/fun_with/jupyter/notebooks/collect_billing/cert/gcp-prices-358310-5df8416c6aa3.json"
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
    token = id_token.fetch_id_token(Request(), cfg.gcp_client_id())
    return token

def get_gcp_prices():
    token = auth_gcp()
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }
    url = "https://cloudbilling.googleapis.com/v1/services"
    response = requests.get(url, headers=headers)
    return response


def main():
    response = get_gcp_prices()
    print(response.text)


if __name__ == "__main__":
    main()