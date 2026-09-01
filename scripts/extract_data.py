import pandas as pd

def extract_data():
    data = pd.read_csv('data/sample_transactions.csv')
    print('Data extracted successfully')