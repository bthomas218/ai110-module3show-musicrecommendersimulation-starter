import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load song records from a CSV file."""
    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        return list(csv.DictReader(csv_file))

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score a song against user preferences and return matching reasons."""
    score = 0.0
    reasons = []

    genre = user_prefs.get("genre", user_prefs.get("favorite_genre"))
    if genre is not None:
        if song.get("genre") == genre:
            score += 25.0
            reasons.append("genre match (+25.0)")
        else:
            reasons.append("genre mismatch (+0.0)")

    mood = user_prefs.get("mood", user_prefs.get("favorite_mood"))
    if mood is not None:
        if song.get("mood") == mood:
            score += 30.0
            reasons.append("mood match (+30.0)")
        else:
            reasons.append("mood mismatch (+0.0)")

    def similarity(song_value: float, target: float, maximum_difference: float = 1.0) -> float:
        difference = abs(song_value - target)
        return max(0.0, 1.0 - (difference / maximum_difference))

    energy = user_prefs.get("energy", user_prefs.get("target_energy"))
    if energy is not None:
        points = similarity(float(song["energy"]), float(energy)) * 20.0
        score += points
        reasons.append(f"energy similarity (+{points:.1f})")

    valence = user_prefs.get("valence", user_prefs.get("target_valence"))
    if valence is not None:
        points = similarity(float(song["valence"]), float(valence)) * 10.0
        score += points
        reasons.append(f"valence similarity (+{points:.1f})")

    tempo = user_prefs.get("tempo_bpm", user_prefs.get("target_tempo_bpm"))
    if tempo is not None:
        points = similarity(float(song["tempo_bpm"]), float(tempo), 60.0) * 5.0
        score += points
        reasons.append(f"tempo similarity (+{points:.1f})")

    danceability = user_prefs.get("danceability", user_prefs.get("target_danceability"))
    if danceability is not None:
        points = similarity(float(song["danceability"]), float(danceability)) * 3.0
        score += points
        reasons.append(f"danceability similarity (+{points:.1f})")

    if "likes_acoustic" in user_prefs:
        acoustic_match = float(song["acousticness"])
        if not user_prefs["likes_acoustic"]:
            acoustic_match = 1.0 - acoustic_match
        points = acoustic_match * 7.0
        score += points
        reasons.append(f"acousticness preference (+{points:.1f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Return the top-k songs ranked by preference score."""
    scored_songs = [
        (song, *score_song(user_prefs, song))
        for song in songs
    ]
    ranked_songs = sorted(scored_songs, key=lambda result: result[1], reverse=True)
    return [
        (song, score, "; ".join(reasons))
        for song, score, reasons in ranked_songs[:k]
    ]
