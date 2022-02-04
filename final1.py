import boto3
from pprint import pprint as pp
import pandas as pd

s3_client = boto3.client("s3")
s3_resource = boto3.resource("s3")

bucket_name = 'data-26-final-project-files'
prefix1 = 'Academy'
prefix2 = 'Talent'
file_type = '.csv'

bucket_contents = s3_client.list_objects_v2(Bucket=bucket_name , Prefix=prefix2)
bucket = s3_resource.Bucket(bucket_name)

contents = bucket.objects.all()

files = [item.key for item in contents]
for file in files:
    if file_type in file:
        pp(file)