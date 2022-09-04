from google.cloud import bigquery
from config import My_Config as cfg
import os
import numpy as np
import pandas as pd
import pandas_gbq

# Working google authentication and client for billing api

credential_path = "/mnt/c/dev/cl/fun_with/jupyter/notebooks/collect_billing/cert/gcp-prices.privkey.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

project_id='gcp-prices-358310'
dataset_location='EU' # 'europe-west4'

client = bigquery.Client(project=project_id, location=dataset_location)

query = """SELECT * FROM `gcp-prices-358310.billing.gcp_billing_export_resource_v1_017DA2_854255_CCEB23`"""

s = pandas_gbq.read_gbq(query, project_id=project_id, dialect='standard')

df = pd.DataFrame(s, index=s.columns)
len_row, len_col = df.shape

print(df.head())
print(df.columns)

#Make a directory if it doesn't exist
if not os.path.exists('gcp'):
    os.makedirs('gcp')

#df.to_csv('gcp/3GCP-Billing-Data.csv', index=False)
df.to_parquet('gcp/3GCP-Billing-Data.parquet', index=False)

#df2 = pd.read_csv('GCP-Billing-Data.csv')
#print(df2.head())
#len_row, len_col = df2.shape

# Export billing to storage is depricated

