# UberEats Restaurant Recommendation System

This project builds a personalized restaurant recommendation system for UberEats users using a hybrid machine learning approach.

## Project Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the API
```bash
python api/app.py
```

### 3. API Endpoint
POST /recommend

Request Body:
```json
{
  "user_id": 123,
  "location": {"lat": 28.61, "lng": 77.20},
  "num_recommendations": 5
}
```

Response:
```json
{
  "recommendations": [
    {"restaurant_id": 1, "name": "Restaurant A", "cuisine": "Italian", "rating": 4.5, "delivery_time": 30, "recommendation_score": 0.85},
    {"restaurant_id": 2, "name": "Restaurant B", "cuisine": "Chinese", "rating": 4.3, "delivery_time": 25, "recommendation_score": 0.82}
  ]
}
```
