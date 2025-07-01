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
        'order_value': 'avg_order_value',
        'rating_given': 'avg_rating_given'
    })
    user_features = user_features.merge(order_stats, on='user_id', how='left')
    user_features['avg_order_value'] = user_features['avg_order_value'].fillna(user_features['avg_order_value'].mean())
    return user_features

def create_restaurant_features(restaurants_df, orders_df):
    restaurant_features = restaurants_df.copy()
    order_stats = orders_df.groupby('restaurant_id').agg({
        'order_id': 'count',
        'rating_given': 'mean'
    }).reset_index().rename(columns={
        'order_id': 'total_orders',
        'rating_given': 'avg_rating'
    })
    restaurant_features = restaurant_features.merge(order_stats, on='restaurant_id', how='left')
    restaurant_features['avg_rating'] = restaurant_features['avg_rating'].fillna(restaurant_features['rating'])
    return restaurant_features
