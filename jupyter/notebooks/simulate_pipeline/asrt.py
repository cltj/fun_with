from datetime import datetime, timedelta
from azure.storage.blob import BlobClient, generate_blob_sas, BlobSasPermissions
from config import My_Config as cfg
import pandas as pd


# Env-vars
LOCAL_FILE_PATH = cfg.local_files_path()
CONTAINERNAME = cfg.new_container_name()
BLOBNAME = cfg.storage_blob_name()
ACCOUNTNAME = cfg.storage_account_name()
ACCOUNTKEY = cfg.storage_account_key()
QUERYSTRING = cfg.meter_sas_string()
CONNECTION_STRING = cfg.storage_connection_string()


account_name = ACCOUNTNAME
account_key = ACCOUNTKEY
container_name = CONTAINERNAME
blob_name = BLOBNAME


class Assert():
    """
    Summary: Asserts a truth about log analytics
    Params: None
    Returns: None
    """

    def get_blob_sas(account_name,account_key, container_name, blob_name):
        sas_blob = generate_blob_sas(account_name=account_name, 
                                    container_name=container_name,
                                    blob_name=blob_name,
                                    account_key=account_key,
                                    permission=BlobSasPermissions(read=True),
                                    expiry=datetime.utcnow() + timedelta(hours=1))
        return sas_blob


    def create_sas(table):
        blob = Assert().get_blob_sas(account_name,account_key, container_name, table)
        sas_url = 'https://'+account_name+'.blob.core.windows.net/'+container_name+'/'+table+'?'+blob
        return sas_url


    def get_data(table):
        sas_url = Assert().create_sas(table)
        df = pd.read_csv(sas_url)
        return df


    def assert_log_analytics_logic(tall):
        pay_g_price = 3.289 * tall
        if tall <= 85:
            price = 3.289 * tall
            savings = pay_g_price - price
            return price, savings
        elif tall >= 85 <= 180:
            price = 2.81 * tall
            savings = pay_g_price - price
            return price, savings
        elif tall >= 180 <= 260:
            price = 2.64 * tall
            savings = pay_g_price - price
            return price, savings
        elif tall >= 260 <= 310:
            price = 2.58 * tall
            savings = pay_g_price - price
            return price, savings
        elif tall >= 310 <= 400:
            price = 2.52 * tall
            savings = pay_g_price - price
            return price, savings
        else:
            return("Error")

    def main():
        df = Assert.get_data('meter_details_dim.csv')
        df = df[['meter_id', 'meter_category', 'meter_sub_category', 'resource_location','unit_of_measure']]
        df.columns
        df2 = Assert.get_data('consumption_details_fact.csv')
        df2 = df2[['meter_id', 'date', 'quantity','unit_price']]
        df2.columns
        df2 =pd.merge(df,df2[['meter_id', 'date', 'quantity','unit_price']], on = 'meter_id', how = 'left')
        df2.columns
        df2['Amount'] = df2.quantity * df2.unit_price
        df2 = df2.groupby('meter_category')['Amount'].nunique()
        tall = df2['Azure Monitor']

        price, savings = Assert.assert_log_analytics_logic(tall)
        print("Savings claim: " + str(savings))
