from google.cloud import bigquery
from config import My_Config as cfg
import os
import pandas as pd
import pandas_gbq


credential_path = "/mnt/c/dev/cl/fun_with/jupyter/notebooks/collect_billing/cert/gcp-prices.privkey.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
project_id='gcp-prices-358310'
dataset_location='EU' # 'europe-west4'

client = bigquery.Client(project=project_id, location=dataset_location)
query = """SELECT * FROM `gcp-prices-358310.billing.gcp_billing_export_resource_v1_017DA2_854255_CCEB23`"""

s = pandas_gbq.read_gbq(query, project_id=project_id, dialect='standard')
df = pd.DataFrame(s, index=s.columns)
if not os.path.exists('gcp'):
    os.makedirs('gcp')

df.to_parquet('gcp/GCP-Billing-Data.parquet', index=False)


print('DONE')