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
    def blob_sas_url():
        BLOB_SAS_URL = os.getenv("BLOB_SAS_URL")
        return BLOB_SAS_URL
    def blob_sas_token():
        BLOB_SAS_TOKEN = os.getenv("BLOB_SAS_TOKEN")
        return BLOB_SAS_TOKEN
    def storage_account_name():
        STORAGE_ACCOUNT_NAME = os.getenv("STORAGE_ACCOUNT_NAME")
        return STORAGE_ACCOUNT_NAME
    def storage_account_key():
        STORAGE_ACCOUNT_KEY = os.getenv("STORAGE_ACCOUNT_KEY")
        return STORAGE_ACCOUNT_KEY
    def storage_container_name():
        STORAGE_CONTAINER_NAME = os.getenv("STORAGE_CONTAINER_NAME")
        return STORAGE_CONTAINER_NAME
    def storage_account_url():
        STORAGE_ACCOUNT_URL = os.getenv("STORAGE_ACCOUNT_URL")
        return STORAGE_ACCOUNT_URL
    def storage_connection_string():
        STORAGE_CONNECTION_STRING = os.getenv("STORAGE_CONNECTION_STRING")
        return STORAGE_CONNECTION_STRING
    def gcp_data_path():
        GCP_DATA_PATH = os.getenv("GCP_DATA_PATH")
        return GCP_DATA_PATH
    def gcp_gbq_table():
        GCP_GBQ_TABLE = os.getenv("GCP_GBQ_TABLE")
        return GCP_GBQ_TABLE
    def gcp_credential_path():
        GCP_CREDENTIAL_PATH = os.getenv("GCP_CREDENTIAL_PATH")
        return GCP_CREDENTIAL_PATH
    def gcp_project_id():
        GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")
        return GCP_PROJECT_ID
    def gcp_dataset_location():
        GCP_DATASET_LOCATION = os.getenv("GCP_DATASET_LOCATION")
        return GCP_DATASET_LOCATION
    def local_files_path():
        LOCAL_FILES_PATH = os.getenv("LOCAL_FILES_PATH")
        return LOCAL_FILES_PATH
