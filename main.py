import boto3
from pprint import pprint as pp
import pandas as pd
from CSV_extractor import CSVextract
from transformation import TransformTalent


# #declare the file information
bucket_name = 'data-26-final-project-files'
# object_name = 'Academy'
object_name= 'Talent'
file_type = '.csv'

csv_df = CSVextract(bucket_name=bucket_name, filetype=file_type, object_name=object_name)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

print("\n*************************** Talent Transformation ***********************************\n")
# csv_df.extract()
df = csv_df.localCSV()
df = TransformTalent(df).df
print(df.head(10))