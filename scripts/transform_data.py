import pandas as pd

def transform_data():
    data = pd.read_csv('data/sample_transactions.csv')
    data['amount'] = data['amount'].astype(float)
    data.to_csv('data/transformed_transactions.csv', index=False)
    print('Data transformed successfully')