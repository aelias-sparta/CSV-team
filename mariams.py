import boto3
from pprint import pprint as pp
import csv

import pandas
import pandas as pd
import pymongo
import io


# Connect to S3
s3_client = boto3.client('s3')               # Low-level functional API (max 1000 obj)
s3_resource = boto3.resource('s3')           # High-level functional API
bucket_name = 'data-26-final-project-files'

# A function to pull specific objects from the bucket list and convert into a dataframe
def get_obj_convertdf(key):
    s3_object = s3_client.get_object(Bucket=bucket_name, Key=key)
    dataframe = pd.read_csv(s3_object["Body"])
    return dataframe

# Store the bucket contents via client server
academy_contents = s3_client.list_objects_v2(Bucket=bucket_name, Prefix="Academy")
talent_contents = s3_client.list_objects_v2(Bucket=bucket_name, Prefix="Talent")
bucket = s3_resource.Bucket(bucket_name)


# Find all the CSV files inside (48 files, 36 academy, 12 talent)
academy_data = []
talent_data = []
for obj in bucket.objects.all():                                       # Loop through all the objects inside
    file_key = obj.key                                                 # Store the file key
    if file_key.endswith('.csv') and 'Academy' in file_key:            # Check if it is a CSV file
        df = get_obj_convertdf(file_key)
        academy_data.append(df)
    elif file_key.endswith('.csv') and 'Talent' in file_key:
        df = get_obj_convertdf(file_key)
        talent_data.append(df)

# Combine dataframes
academy_df = pandas.concat(academy_data, join='outer', ignore_index=True)
talent_df = pandas.concat(talent_data, join='outer', ignore_index=True)






















