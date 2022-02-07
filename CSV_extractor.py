import boto3
from pprint import pprint as pp
import pandas as pd


class CSVextract:

    def __init__(self, bucket_name, filetype, object_name):
        self.bucket_name = bucket_name
        self.filetype = filetype
        self.object_name = object_name

        self.s3_client = boto3.client("s3")
        self.s3_resource = boto3.resource("s3")
        self.bucket = self.s3_resource.Bucket(self.bucket_name)
        self.contents = self.bucket.objects.all()
        self.files = [item.key for item in self.contents]

        bucket_name = 'data-26-final-project-files'
        prefix1 = 'Academy'
        prefix2 = 'Talent'
        file_type = '.csv'

    def extract(self):
        csv_list = []
        for file in self.files:
            if self.filetype in file:
                if self.object_name in file:
                    file_csv = self.s3_client.get_object(Bucket=self.bucket_name, Key=file)
                    df = pd.read_csv(file_csv['Body'])

                    if self.object_name == 'Academy':
                        start_date = file[-14:-4]
                        course_name = file.split('/')[1][:-15]
                        df.insert(2, 'start_date', start_date, True)
                        df.insert(2, 'course_name', course_name, True)
                    csv_list.append(df)

        df = pd.concat(csv_list, join="outer", ignore_index=True) # 12 csv files combined
        df.to_csv(f"{self.object_name}.csv", index=False)

        return df

    def localCSV(self):
        return pd.read_csv(f"{self.object_name}.csv")
