import boto3
from pprint import pprint as pp
import pandas as pd

s3_client = boto3.client("s3")
s3_resource = boto3.resource("s3")

bucket_name = 'data-26-final-project-files'
prefix1 = 'Academy'
prefix2 = 'Talent'
file_type = '.csv'

bucket = s3_resource.Bucket(bucket_name)
contents = bucket.objects.all()
files = [item.key for item in contents]

# combined_data = pd.concat(list_csv, join="outer", ignore_index=True)
# counter = 0
talent_list = []
academy_list = []

for file in files:
    if '.csv' in file:
        if 'Talent' in file:
            #print(file)
            file_csv = s3_client.get_object(Bucket=bucket_name, Key=file)
            df = pd.read_csv(file_csv['Body'])
            talent_list.append(df)
        else:
            #print(file)

            file_csv = s3_client.get_object(Bucket=bucket_name, Key=file)
            df = pd.read_csv(file_csv['Body'])
            academy_list.append(df)

talent_data = pd.concat(talent_list, join="outer", ignore_index=True) # 12 csv files combined
academy_data = pd.concat(academy_list, join="outer", ignore_index=True) # this is 36 csv files combined

print(f"\n********************* Talent Data  *****************************************\n")
print(talent_data.info())
print("\n")
print(talent_data.isnull().sum())

print(f"\n********************* academy Data  *****************************************\n")
print(academy_data.info())
print("\n")
print(academy_data.isnull().sum())


        # file_csv = s3_client.get_object(Bucket=bucket_name, Key=file)
#         df = pd.read_csv(file_csv['Body'])
#         print(f"\n********************* Checking for Null values file{counter, file}   *****************************************\n")
#         print(df.isnull().sum())
#
#         print(f"\n********************* Checking for Duplicates  file{counter, file}  *****************************************\n")
#         print(df.duplicated().sum())
#         counter +=1


# # testing on an individual files
# file_csv = s3_client.get_object(Bucket=bucket_name, Key=files[9])
# df = pd.read_csv(file_csv['Body'])
# #print(f"\n********************* Checking for Null values file{files[9]}   *****************************************\n")
# #print(df.isnull().sum())
# #print(f"% of Null={df.isnull().sum() / len(df)}")
#
# #print(f"\n********************* Checking for Duplicates  file{files[9]}  *****************************************\n")
# #print(df.duplicated().sum())
# pd.set_option('display.max_columns', None)
# pp(df.head(3))

