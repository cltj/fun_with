import boto3
import os
from config import My_Config as cfg


session = boto3.Session(
    aws_access_key_id=cfg.aws_access_id(),
    aws_secret_access_key=cfg.aws_secret_key()
)


s3 = session.resource('s3')
bucket = s3.Bucket('collectbill')
count = 1
filenames = []
for s3_object in bucket.objects.all():
    if s3_object.key.endswith('.parquet'):
        path, filename = os.path.split(s3_object.key)
        bucket.download_file(s3_object.key, 'aws/aws-billing-data-'+str(count)+'.parquet')
        filenames.append(s3_object.key)
        count += 1


print('DONE')