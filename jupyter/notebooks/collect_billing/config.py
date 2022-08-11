import os
from dotenv import load_dotenv


class My_Config():
    load_dotenv()
    def client_id():
        CLIENT_ID = os.getenv("CLIENT_ID")
        return CLIENT_ID
    def client_secret():
        CLIENT_SECRET = os.getenv("CLIENT_SECRET")
        return CLIENT_SECRET
    def tenant_id():
        TENANT_ID = os.getenv("TENANT_ID")
        return TENANT_ID
    def subscription_id():
        SUBSCRIPTION_ID = os.getenv("SUBSCRIPTION_ID")
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