# sports-reco

A simple sports recommendation system that helps users discover sports activities based on their preferences.

## Features

- Personalized sport recommendations
- Filter by intensity level, team sport preference, and equipment needs
- Easy-to-use Python API

## Quick Start

```python
from sports_reco import SportsRecommender

recommender = SportsRecommender()
recommendations = recommender.get_recommendations({
    "intensity": "medium",
    "team_sport": False
})
print(recommendations)  # ['tennis', 'swimming']
```
