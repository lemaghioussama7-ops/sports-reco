"""Main recommendation engine for sports activities."""

from typing import List, Dict, Any


class SportsRecommender:
    """A simple sports recommendation system."""

    def __init__(self):
        """Initialize the recommender with default sports data."""
        self.sports_data = {
            "football": {"intensity": "high", "team_sport": True, "equipment": "ball"},
            "tennis": {
                "intensity": "medium",
                "team_sport": False,
                "equipment": "racket",
            },
            "swimming": {
                "intensity": "medium",
                "team_sport": False,
                "equipment": "none",
            },
            "basketball": {
                "intensity": "high",
                "team_sport": True,
                "equipment": "ball",
            },
            "yoga": {"intensity": "low", "team_sport": False, "equipment": "mat"},
        }

    def get_recommendations(self, user_preferences: Dict[str, Any]) -> List[str]:
        """Get sport recommendations based on user preferences.

        Args:
            user_preferences: Dictionary containing user preferences like
                            intensity level, team sport preference, etc.

        Returns:
            List of recommended sports.
        """
        recommendations = []

        for sport, attributes in self.sports_data.items():
            if self._matches_preferences(attributes, user_preferences):
                recommendations.append(sport)

        return recommendations

    def _matches_preferences(
        self, sport_attributes: Dict[str, Any], user_preferences: Dict[str, Any]
    ) -> bool:
        """Check if sport attributes match user preferences."""
        if "intensity" in user_preferences:
            if sport_attributes["intensity"] != user_preferences["intensity"]:
                return False

        if "team_sport" in user_preferences:
            if sport_attributes["team_sport"] != user_preferences["team_sport"]:
                return False

        return True
