import boto3
import pandas as pd

class ExtractCSV:
    """Extracting CSV files from an AWS S3 Bucket"""
    def __init__(self, bucket_name, prefix):
        self.bucket_name = bucket_name
        self.prefix = prefix

        self.s3_client = boto3.client("s3")
        self.s3_resource = boto3.resource("s3")

        self.csv_file_names = []
        self.df = self.extract()

    def extract(self):
        bucket = self.s3_resource.Bucket(self.bucket_name)
        contents = bucket.objects.all()
        files = [item.key for item in contents]
        table = []

        for file in files:
            if '.csv' in file and self.prefix in file:
                self.csv_file_names.append(file)
                csv_file = self.s3_client.get_object(Bucket=self.bucket_name, Key=file)
                df1 = pd.read_csv(csv_file['Body'])
                table.append(df1)

        df = pd.concat(table, axis=0, ignore_index=True)

        return df