import os
from config import My_Config as cfg
from azure.storage.blob import BlobServiceClient, ContainerClient

# Connecting to Azure Storage with blobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(conn_str=cfg.storage_connection_string())

# Connecting to Azure Storage with containerClient
container_client = ContainerClient(
    account_url=cfg.storage_account_url(), 
    container_name=cfg.storage_container_name(), 
    credential=cfg.storage_account_key()
    )

# Check right connection and container
if container_client.get_container_properties():
    print("Connection to container client was successful")
    container_name = container_client.container_name
    print("Connected to container: " + container_name)
else:
    print("Connection to container client was not successful")

# Reference the local file
path = os.path.join(cfg.gcp_data_path(), "GCP-Billing-Data.parquet")


# Upload the local file to Azure Storage container
with open(path, "rb") as data:
    container_client.upload_blob(name="GCP-Billing-Data.parquet", data=data)
    print("Uploaded file to container")

print("Done!!")