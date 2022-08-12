import boto3
import os
from config import My_Config as cfg
import pandas as pd

s3 = boto3.resource(
    service_name='s3',
    region_name='us-east-2',
    aws_access_key_id=cfg.aws_access_id(),
    aws_secret_access_key=cfg.aws_secret_key()
)

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

# Make dataframes
foo = pd.DataFrame({'x': [1, 2, 3], 'y': ['a', 'b', 'c']})
bar = pd.DataFrame({'x': [10, 20, 30], 'y': ['aa', 'bb', 'cc']})

# Save to csv
foo.to_csv('foo.csv')
bar.to_csv('bar.csv')

# Upload files to S3 bucket
#s3.Bucket('collectbill').upload_file(Filename='foo.csv', Key='foo.csv')
#s3.Bucket('collectbill').upload_file(Filename='bar.csv', Key='bar.csv')

for obj in s3.Bucket('collectbill').objects.all():
    print(obj)

# Download file and read from disc
s3.Bucket('collectbill').download_file(Key='foo.csv', Filename='foo2.csv')
pd.read_csv('foo2.csv', index_col=0)
