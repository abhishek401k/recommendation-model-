import pandas as pd
import numpy as np
from geopy.distance import geodesic

def calculate_distance(lat1, lng1, lat2, lng2):
    return geodesic((lat1, lng1), (lat2, lng2)).km

def create_user_features(users_df, orders_df, restaurants_df):
    user_features = users_df.copy()

    order_stats = orders_df.groupby('user_id').agg({
        'order_id': 'count',
        'order_value': 'mean',
        'rating_given': 'mean'
    }).reset_index().rename(columns={
        'order_id': 'total_orders',
        'order_value': 'computed_avg_order_value',
        'rating_given': 'avg_rating_given'
    })

    user_features = user_features.merge(order_stats, on='user_id', how='left')

    # Safely handle avg_order_value
    user_features['final_avg_order_value'] = user_features['computed_avg_order_value'].combine_first(user_features['avg_order_value'])

    # Clean up and rename
    user_features = user_features.drop(['avg_order_value', 'computed_avg_order_value'], axis=1)
    user_features = user_features.rename(columns={'final_avg_order_value': 'avg_order_value'})

    return user_features

