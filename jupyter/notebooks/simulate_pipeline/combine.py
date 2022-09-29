from config import My_Config as cfg
import pandas as pd
import numpy as np
import os

# Env-vars
LOCAL_FILE_PATH = cfg.local_files_path()
CONTAINERNAME = cfg.new_container_name()
BLOBNAME = cfg.storage_blob_name()
ACCOUNTNAME = cfg.storage_account_name()
QUERYSTRING = cfg.blob_query_string()
CONNECTION_STRING = cfg.storage_connection_string()


class Combine():
    """
    Summary: Authenticates the client, gets the data and stores it in .parquet format
    Params: None
    Returns: None
    """

    def create_sas(table):    
        sas_url = f"https://{ACCOUNTNAME}.blob.core.windows.net/{CONTAINERNAME}/{table}{QUERYSTRING}"
        return sas_url


    def get_data(table):
        sas_url = Combine.create_sas(table)
        df = pd.read_csv(sas_url)
        return df


    def get_new_index(table,index,reference):
        # get dim table
        data = Combine.get_data(table)
        print(data.columns)
        # get index col and ref col
        df = data.loc[:[index,reference]]
        # converting to dict
        data_dict = df.to_dict()  
        print(data_dict)
        # display
        return data_dict
    


    def merge_index_with_facts(table,index,reference):
        # get fact table
        fact_table = ''
        df = Combine.get_data(fact_table)
        # get new index from dim
        data_dict = Combine.get_new_index(table,index,reference)
        # merge index
        """ 
        for reference in fact_table:
            if refererence in data_dict['reference']:
            reference.replace(data_dict['index'])
            
        """
        ## if string == string => replace with index number
        print("Done!!!")
    
    
    def main():
        Combine.get_new_index('meter_details_dim.csv',)
        print("Done!!!")