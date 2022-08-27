from datetime import datetime
from random import randint
from google.cloud import bigquery
from azure.identity import DefaultAzureCredential
from azure.mgmt.consumption import ConsumptionManagementClient
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

    s3 = session.resource('s3')
    bucket = s3.Bucket('collectbill')
    count = 1
    for s3_object in bucket.objects.all():
        if s3_object.key.endswith('.parquet'):
            path, filename = os.path.split(s3_object.key)
            bucket.download_file(s3_object.key, 'local/'+str(count)+filename)
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
    credential_path = "/mnt/c/dev/cl/fun_with/jupyter/notebooks/collect_billing/cert/gcp-prices.privkey.json"
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
    project_id='gcp-prices-358310'
    dataset_location='europe-west4'
    client = bigquery.Client(project=project_id, location=dataset_location)

    query = """SELECT * FROM `gcp-prices-358310.12345.gcp_billing_export_v1_017DA2_854255_CCEB23`"""
    s = pandas_gbq.read_gbq(query, project_id=project_id, dialect='standard')
    df = pd.DataFrame(s, index=s.columns)
    df.to_parquet('local/GCP-Billing-Data.parquet', index=False)


def upload_parquet():
    path= '/mnt/c/dev/cl/fun_with/jupyter/notebooks/collect_billing/local'
    for file in os.listdir(path):
        if file.endswith(".parquet"):
        # Prints only parquet file present in local folder
            print(file)


def main():
    aws_billing()
    azure_billing()
    gcp_billing()
    upload_parquet()
    print("Done!!!")


if __name__ == '__main__':
    main()
