import boto3
import os
from config import My_Config as cfg
import pandas as pd
import datetime

# Working aws authentication and client for consumption api

session = boto3.Session(
    aws_access_key_id=cfg.aws_access_id(),
    aws_secret_access_key=cfg.aws_secret_key()
)


#Initiate S3 Resource
s3 = session.resource('s3')

# Select Your S3 Bucket
your_bucket = s3.Bucket('collectbill')

# Iterate All Objects in Your S3 Bucket Over the for Loop
for s3_object in your_bucket.objects.all():
   
    #Use this statement if your files are available directly in your bucket. 
    #your_bucket.download_file(s3_object.key, 'test-00001.snappy.parquet')

    #use below three line ONLY if you have sub directories available in S3 Bucket
    #Split the Object key and the file name.
    #parent directories will be stored in path and Filename will be stored in the filename
    if s3_object.key.endswith('.parquet'):
        path, filename = os.path.split(s3_object.key)

        #Create sub directories if its not existing
        os.makedirs(path)
        
        #Download the file in the sub directories or directory if its available. 
        your_bucket.download_file(s3_object.key, path+'/'+filename)

        #Read the file and convert it to pandas dataframe
        #df = pd.read_parquet(path+'/'+filename)
        #print(df)
        #print(df.shape)
        #print(df.head())
