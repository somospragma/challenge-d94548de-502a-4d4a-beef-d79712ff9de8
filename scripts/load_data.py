import pandas as pd
import boto3

def load_data():
    data = pd.read_csv('data/transformed_transactions.csv')
    s3 = boto3.client('s3')
    s3.upload_file('data/transformed_transactions.csv', 'my-bucket', 'transformed_transactions.csv')
    print('Data loaded successfully')