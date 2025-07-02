import pandas as pd

def load_users():
    return pd.DataFrame({
        'user_id': [1, 2, 3],
        'location_lat': [28.6139, 28.7041, 28.5355],
        'location_lng': [77.2090, 77.1025, 77.3910],
        'avg_order_value': [25, 30, 20]
    })


def load_restaurants():
    return pd.DataFrame({
        'restaurant_id': [101, 102, 103],
        'name': ['Restaurant A', 'Restaurant B', 'Restaurant C'],
        'cuisine_type': ['Italian', 'Chinese', 'Indian'],
        'rating': [4.5, 4.2, 4.0],
        'delivery_time': [30, 25, 20],
        'location_lat': [28.6140, 28.7045, 28.5358],
        'location_lng': [77.2100, 77.1030, 77.3905]
    })


def load_orders():
    return pd.DataFrame({
        'order_id': [1001, 1002, 1003, 1004],
        'user_id': [1, 1, 2, 3],
        'restaurant_id': [101, 102, 102, 103],
        'order_value': [24, 26, 30, 20],
        'rating_given': [5, 4, 5, 4]
    })

