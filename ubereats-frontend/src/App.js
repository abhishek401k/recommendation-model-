import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [userId, setUserId] = useState('');
  const [recommendations, setRecommendations] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const response = await axios.post('https://recommendation-model-3.onrender.com/recommend', {
        user_id: parseInt(userId),
        num_recommendations: 5
      });
      setRecommendations(response.data.recommendations);
    } catch (error) {
      console.error('Error fetching recommendations', error);
    }
    setLoading(false);
  };

  return (
    <div className="App" style={{ padding: '20px' }}>
      <h1>UberEats Restaurant Recommendations</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="number"
          placeholder="Enter User ID"
          value={userId}
          onChange={(e) => setUserId(e.target.value)}
          required
          style={{ padding: '8px', marginRight: '10px' }}
        />
        <button type="submit" style={{ padding: '8px 16px' }}>Get Recommendations</button>
      </form>

      {loading && <p>Loading...</p>}

      {recommendations.length > 0 && (
        <div style={{ marginTop: '20px' }}>
          <h2>Recommended Restaurants:</h2>
          <ul>
            {recommendations.map((rec) => (
              <li key={rec.restaurant_id}>
                {rec.name} ({rec.cuisine}) - Rating: {rec.rating} - Delivery: {rec.delivery_time} mins
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
