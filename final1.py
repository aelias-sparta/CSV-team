import boto3
from pprint import pprint as pp
import pandas as pd
from extract_csv import ExtractCSV
from transform_talent import TransformTalent

s3_client = boto3.client("s3")
s3_resource = boto3.resource("s3")

bucket_name = 'data-26-final-project-files'
prefix1 = 'Academy'
prefix2 = 'Talent'
file_type = '.csv'

bucket_contents = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=prefix2)
bucket = s3_resource.Bucket(bucket_name)

contents = bucket.objects.all()

files = [item.key for item in contents]
for file in files:
    if file_type in file:
        pp(file)

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
data = ExtractCSV('data-26-final-project-files', 'Talent')
data1 = TransformTalent(data.df)
print(data1.df.head())
data2 = ExtractCSV('data-26-final-project-files', 'Academy')
print(data2.df.head())
# print(len(data.csv_file_names))
# data1 = TransformTalent(data.df)
# print(data1.df.invited_date)