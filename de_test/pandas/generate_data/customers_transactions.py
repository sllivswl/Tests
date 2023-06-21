import os
import sys

sys.path.append('../')
from generator import *
import pandas as pd

from ast import literal_eval
from collections import Counter


def load_data(data_name: str) -> pd.DataFrame():
    return read_csv(os.path.join(output_location, data_name))


def get_products_per_customer(df_transactions: pd.DataFrame()) -> pd.DataFrame():
    """Groups products by customers and calculates them. 
    """
    
    tmp = df_transactions.groupby('customer_id').agg({'products': sum}).reset_index()
    tmp['product_cnt'] = tmp['products'].apply(lambda x: Counter(x))
    tmp['product_id'] = tmp['product_cnt'].apply(lambda x: [k for k in x])
    tmp['purchaise_count'] = tmp['product_cnt'].apply(lambda x: [v for v in x.values()])

    df = (tmp.drop(['products', 'product_cnt'], axis=1)
               .explode(['product_id', 'purchaise_count']).reset_index(drop=True))
    return df



if __name__ == "__main__":
    df_customers = load_data('customers.csv')
    df_products = load_data('products.csv')
    df_transactions = read_json_folder(os.path.join(output_location, 'transactions',''))

    df_transactions['basket'] = df_transactions['basket'].apply(str).apply(literal_eval)
    df_transactions['products'] = df_transactions['basket'].apply(lambda x: 
                                                                [elm['product_id'] for elm in x])

    df = get_products_per_customer(df_transactions)
    df = pd.merge(df, df_products.drop('product_description', axis=1), on='product_id', how='left')
    df = pd.merge(df, df_customers, on='customer_id', how='left')

    cols = ['customer_id', 'loyalty_score', 'product_id', 'product_category', 'purchaise_count']
    df = df[cols].copy()

    output_data = 'output_data'
    os.makedirs(output_data, exist_ok=True)

    df.to_csv(os.path.join(output_data, 'customer_products_purchase.csv'), index=False)
