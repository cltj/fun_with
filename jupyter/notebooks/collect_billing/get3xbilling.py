from google.cloud import bigquery
from azure.identity import DefaultAzureCredential
from azure.mgmt.consumption import ConsumptionManagementClient
from azure.storage.blob import BlobServiceClient
from config import My_Config as cfg
import boto3
import os
import pandas as pd
import pandas_gbq


def aws_billing():
    session = boto3.Session(
        aws_access_key_id=cfg.aws_access_id(),
        aws_secret_access_key=cfg.aws_secret_key()
    )

    # LOCAL_FILES_PATH = cfg.local_files_path()
    s3 = session.resource('s3')
    bucket = s3.Bucket('collectbill')
    count = 1
    filenames = []
    for s3_object in bucket.objects.all():
        if s3_object.key.endswith('.parquet'):
            path, filename = os.path.split(s3_object.key)
            bucket.download_file(s3_object.key, 'local/'+str(count)+filename)
            filenames.append(s3_object.key)
            count += 1


def azure_billing():
    credential = DefaultAzureCredential()
    client = ConsumptionManagementClient(
        credential=credential,
        subscription_id=cfg.az_subscription_id()
        )

    usage = client.usage_details.list(scope='/subscriptions/' + cfg.az_subscription_id() + '/')
    df = pd.DataFrame()
    for item in usage:
        df = df.append(item.as_dict(), ignore_index=True)
    df.to_parquet('local/Azure-Billing-Data.parquet')


def gcp_billing():
    credential_path = cfg.gcp_credential_path()
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
    project_id=cfg.gcp_project_id()
    dataset_location=cfg.gcp_dataset_location()
    client = bigquery.Client(project=project_id, location=dataset_location)

    query = """SELECT * FROM `gcp-prices-358310.12345.gcp_billing_export_v1_017DA2_854255_CCEB23`"""
    data = pandas_gbq.read_gbq(query, project_id=project_id, dialect='standard')
    df = pd.DataFrame(data)
    df.to_parquet('local/GCP-Billing-Data.parquet', index=False)


def upload_parquet():
    CONNECTION_STRING = cfg.storage_connection_string()
    BILLING_CONTAINER = cfg.storage_container_name()
    LOCAL_FILES_PATH = cfg.local_files_path()
    
    class AzureBlobFileUploader:
        def __init__(self):
            print("Intializing AzureBlobFileUploader")
            # Initialize the connection to Azure storage account
            self.blob_service_client =  BlobServiceClient.from_connection_string(CONNECTION_STRING)
        
        def upload_all_images_in_folder(self):
            # Get all files with parquet extension and exclude directories
            all_file_names = [f for f in os.listdir(LOCAL_FILES_PATH)
                            if os.path.isfile(os.path.join(LOCAL_FILES_PATH, f)) and ".parquet" in f]
            
            for file_name in all_file_names: # Upload each file
                self.upload_file(file_name)
        
        def upload_file(self,file_name):
            blob_client = self.blob_service_client.get_blob_client(container=BILLING_CONTAINER, blob=file_name) # Create blob with same name as local file name
            upload_file_path = os.path.join(LOCAL_FILES_PATH, file_name)
            
            print(f"uploading file - {file_name}")
            with open(upload_file_path, "rb") as data: # Uploads to cltj
                blob_client.upload_blob(data,overwrite=True)

    azure_blob_file_uploader = AzureBlobFileUploader() # Initialize class and upload files
    azure_blob_file_uploader.upload_all_images_in_folder()


def cleanup_files():
    LOCAL_FILES_PATH = cfg.local_files_path()
    for f in os.listdir(LOCAL_FILES_PATH):
        if not f.endswith(".parquet"):
            continue
        os.remove(os.path.join(LOCAL_FILES_PATH, f))


def main():
    aws_billing()
    azure_billing()
    gcp_billing()
    upload_parquet()
    cleanup_files()
    print("Done!!!")


if __name__ == '__main__':
    main()