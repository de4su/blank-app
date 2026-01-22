"""
Game recommendation matching algorithm based on user tags.
"""
from typing import List, Dict, Tuple


def calculate_match_score(user_tags: List[str], game_tags: List[str]) -> float:
    """
    Calculate the match percentage between user preferences and a game's tags.
    
    Uses the formula: (matching_tags / user_tags) * 100
    This ensures games are ranked by how well they match user preferences.
    
    Args:
        user_tags: List of tags selected by the user
        game_tags: List of tags associated with a game
        
    Returns:
        Match percentage (0-100). Returns 0 if user has no tags.
    """
    if not user_tags:
        return 0.0
    
    matching_tags = len(set(user_tags) & set(game_tags))
    match_percentage = (matching_tags / len(user_tags)) * 100
    return match_percentage


def get_recommendations(
    user_tags: List[str],
    games: List[Dict],
    top_n: int = 3
) -> List[Tuple[Dict, float]]:
    """
    Get top N game recommendations based on user tags.
    
    Args:
        user_tags: List of tags from user quiz answers
        games: List of game dictionaries with 'name', 'id', 'tags', etc.
        top_n: Number of recommendations to return (default 3)
        
    Returns:
        List of tuples containing (game_dict, match_score) sorted by score
    """
    # Calculate scores for all games
    game_scores = []
    for game in games:
        score = calculate_match_score(user_tags, game.get("tags", []))
        game_scores.append((game, score))
    
    # Sort by score descending and return top N
    game_scores.sort(key=lambda x: x[1], reverse=True)
    return game_scores[:top_n]
