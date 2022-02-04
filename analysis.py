from pprint import pprint as pp
import csv
import pandas
import pandas as pd
import pymongo
import io

academy_df = pd.read_csv('academy_data.csv')
talent_df = pd.read_csv('talent_data.csv')

pp(academy_df.head())
