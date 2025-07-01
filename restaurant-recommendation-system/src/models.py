import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

class RecommendationModel:
    def __init__(self):
        self.model = None
        self.scaler = StandardScaler()
        self.features = ['distance', 'user_avg_order_value', 'restaurant_rating']

    def prepare_training_data(self, orders_df, user_features, restaurant_features, calculate_distance):
        merged = orders_df.merge(user_features, on='user_id').merge(restaurant_features, on='restaurant_id')
        merged['distance'] = merged.apply(lambda row: calculate_distance(
            row['location_lat_x'], row['location_lng_x'],
            row['location_lat_y'], row['location_lng_y']), axis=1)
        merged['user_avg_order_value'] = merged['avg_order_value']
        merged['restaurant_rating'] = merged['avg_rating']
        merged['target'] = merged['rating_given'] / 5.0
        return merged

    def train(self, training_data):
        X = training_data[self.features]
        y = training_data['target']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        X_train_scaled = self.scaler.fit_transform(X_train)
        self.model = xgb.XGBRegressor()
        self.model.fit(X_train_scaled, y_train)

    def predict(self, user_id, user_features, restaurant_features, calculate_distance, top_n=5):
        user = user_features[user_features['user_id'] == user_id].iloc[0]
        predictions = []
        for _, restaurant in restaurant_features.iterrows():
            distance = calculate_distance(user['location_lat'], user['location_lng'], restaurant['location_lat'], restaurant['location_lng'])
            X = pd.DataFrame([{ 'distance': distance, 'user_avg_order_value': user['avg_order_value'], 'restaurant_rating': restaurant['avg_rating'] }])
            X_scaled = self.scaler.transform(X)
            score = self.model.predict(X_scaled)[0]
            predictions.append((restaurant['restaurant_id'], restaurant['name'], restaurant['cuisine_type'], restaurant['rating'], restaurant['delivery_time'], score))
        predictions.sort(key=lambda x: x[5], reverse=True)
        return predictions[:top_n]
