from azure.identity import DefaultAzureCredential
from azure.mgmt.consumption import ConsumptionManagementClient
from config import My_Config as cfg
import pandas as pd

credential = DefaultAzureCredential()
client = ConsumptionManagementClient(
    credential=credential,
    subscription_id=cfg.az_subscription_id()
    )

a = client.usage_details.list(scope='/subscriptions/' + cfg.az_subscription_id() + '/')

df = pd.DataFrame()

for i in a:
    df = df.append(i.as_dict(), ignore_index=True)

print(df.shape)
df.to_csv('01-Usage-August.csv')

print(f"Successful credential: {credential._successful_credential.__class__.__name__}")