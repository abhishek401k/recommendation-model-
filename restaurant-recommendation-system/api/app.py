
from flask import Flask, request, jsonify
import pandas as pd
from src.data_preprocessing import load_users, load_restaurants, load_orders
from src.feature_engineering import create_user_features, create_restaurant_features, calculate_distance
from src.models import RecommendationModel

app = Flask(__name__)

users_df = load_users()
restaurants_df = load_restaurants()
orders_df = load_orders()

user_features = create_user_features(users_df, orders_df, restaurants_df)
restaurant_features = create_restaurant_features(restaurants_df, orders_df)

model = RecommendationModel()
training_data = model.prepare_training_data(orders_df, user_features, restaurant_features, calculate_distance)
model.train(training_data)

@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        data = request.json
        user_id = data['user_id']
        num_recommendations = data.get('num_recommendations', 5)

        recommendations = model.predict(user_id, user_features, restaurant_features, calculate_distance, top_n=num_recommendations)

        response = [
            {'restaurant_id': r[0], 'name': r[1], 'cuisine': r[2], 'rating': r[3], 'delivery_time': r[4], 'recommendation_score': r[5]} 
            for r in recommendations
        ]

        return jsonify({'recommendations': response})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
