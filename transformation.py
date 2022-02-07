import pandas as pd

class TransformTalent:
    """Transforming the columns for the Talent df"""
    def __init__(self, df):
        self.df = df
        self.clean_id()
        self.clean_dob()
        self.clean_phone_numbers()
        self.clean_invited_date()



    def clean_id(self):
        self.df = self.df.drop(columns='id')
        self.df.index.name = 'id'

    def clean_dob(self):
        self.df['dob'] = pd.to_datetime(self.df['dob'], dayfirst=True)

    def clean_phone_numbers(self):
        self.df['phone_number'] = self.df['phone_number'].str.replace(' ', '', regex=True)
        self.df['phone_number'] = self.df['phone_number'].str.replace('(', '', regex=True)
        self.df['phone_number'] = self.df['phone_number'].str.replace(')', '', regex=True)
        self.df['phone_number'] = self.df['phone_number'].str.replace('-', '', regex=True)

    def clean_invited_date(self):
        self.df['invited_date'] = self.df['invited_date'].astype(str)
        self.df['invited_date'] = self.df['invited_date'].str.slice(0, -2)
        self.df['month'] = self.df['month'].astype(str)
        self.df['month'] = self.df['month'].str.capitalize()
        self.df['month'] = self.df['month'].str.replace(' ', '/', regex=True)
        self.df['invited_date'] = self.df['invited_date'].str.cat(self.df['month'], '/')
        self.df['invited_date'] = self.df['invited_date'].str.replace('n/Nan', '', regex=True)
        self.df['invited_date'] = pd.to_datetime(self.df['invited_date'])
        self.df = self.df.drop(columns='month')