from google.cloud import bigquery
import os

credential_path = "/mnt/c/dev/cl/fun_with/jupyter/notebooks/collect_billing/cert/gcp-prices.privkey.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

project_id='gcp-prices-358310'
dataset_location='europe-west4'
client = bigquery.Client(project=project_id, location=dataset_location)

query = """SELECT * FROM `gcp-prices-358310.12345.gcp_billing_export_v1_017DA2_854255_CCEB23`"""

query_job = client.query(query)
rows = query_job.result()  # Waits for job to complete.
for row in rows:
    print(row)

