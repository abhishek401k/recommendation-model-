import pandas as pd

def load_users():
    return pd.read_csv('data/raw/users.csv')

def load_restaurants():
    return pd.read_csv('data/raw/restaurants.csv')

def load_orders():
    return pd.read_csv('data/raw/orders.csv')
