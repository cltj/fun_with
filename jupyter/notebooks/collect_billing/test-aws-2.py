import boto3
import os
from config import My_Config as cfg
import pandas as pd
import datetime

s3 = boto3.resource(
    service_name='s3',
    region_name='us-east-2',
    aws_access_key_id=cfg.aws_access_id(),
    aws_secret_access_key=cfg.aws_secret_key()
)


def make_folders():
    six_months_ago = datetime.datetime.now() - datetime.timedelta(days=180)
    six_months_ago = six_months_ago.strftime("%Y%m01")

    """Make a dictionary of all months in the last 6 months"""
    months = {}
    for i in range(7):
        months[i] = datetime.datetime.strptime(six_months_ago, "%Y%m%d") + datetime.timedelta(days=30*i)
        months[i] = months[i].strftime("%Y%m01")

    """Pair each month with the next month"""
    folders = {}
    for i in range(6):
        folders[i] = str(months[i]+'-'+months[i+1])

    """Make the last month pair manually and replace the last month with the current month"""
    folders[5] = str(months[5]+'-'+datetime.datetime.now().strftime("%Y%m01"))

    print(folders)
    print(len(folders))

    #"""Make the folders"""
    #for i in range(len(folders)):
    #    if not os.path.exists(folders[i]):
    #        os.makedirs(folders[i])

    return folders


"""make a new dataframe and import s3 bucket files into it"""
def make_df():
    df = pd.DataFrame()
    for obj in s3.Bucket('collectbill').objects.all():
        if obj.key.endswith('.parquet'):
            print(obj.key)
            df = df.append(pd.read_parquet(obj.key, index_col=0))
            df.shape
    return df

make_df()

# Need to convert type to parquet 
# look for tools that can gather all files in a folder and convert to parquet