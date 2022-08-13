import os
from dotenv import load_dotenv


class My_Config():
    load_dotenv()
    def az_client_id():
        CLIENT_ID = os.getenv("AZ_CLIENT_ID")
        return CLIENT_ID
    def az_client_secret():
        CLIENT_SECRET = os.getenv("AZ_CLIENT_SECRET")
        return CLIENT_SECRET
    def az_tenant_id():
        TENANT_ID = os.getenv("AZ_TENANT_ID")
        return TENANT_ID
    def az_subscription_id():
        SUBSCRIPTION_ID = os.getenv("AZ_SUBSCRIPTION_ID")
        return SUBSCRIPTION_ID
    def aws_user():
        AWS_USER = os.getenv("AWS_USER")
        return AWS_USER
    def aws_secret_key():
        AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
        return AWS_SECRET_KEY
    def aws_access_id():
        AWS_ACCESS_ID = os.getenv("AWS_ACCESS_ID")
        return AWS_ACCESS_ID
    def google_application_credentials():
        GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
        return GOOGLE_APPLICATION_CREDENTIALS
    def gcp_prices_api_key():
        GCP_PRICES_API_KEY = os.getenv("GCP_PRICES_API_KEY")
        return GCP_PRICES_API_KEY
    def gcp_client_id():
        GCP_CLIENT_ID = os.getenv("GCP_CLIENT_ID")
        return GCP_CLIENT_ID
    def gcp_client_secret():
        GCP_CLIENT_SECRET = os.getenv("GCP_CLIENT_SECRET")
        return GCP_CLIENT_SECRET