"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


# Example user preference profiles for different listening styles.
HIGH_ENERGY_POP = {
    "genre": "pop",
    "mood": "happy",
    "energy": 0.8,
    "valence": 0.9,
    "tempo_bpm": 120,
    "danceability": 0.8,
    "likes_acoustic": False,
}

CHILL_LOFI = {
    "genre": "lofi",
    "mood": "chill",
    "energy": 0.4,
    "valence": 0.6,
    "tempo_bpm": 80,
    "danceability": 0.5,
    "likes_acoustic": True,
}

DEEP_INTENSE_ROCK = {
    "genre": "rock",
    "mood": "intense",
    "energy": 0.9,
    "valence": 0.3,
    "tempo_bpm": 140,
    "danceability": 0.4,
    "likes_acoustic": False,
}

CONFLICTING_HIGH_ENERGY_SAD = {
    "genre": "pop",
    "mood": "sad",
    "energy": 0.9,
    "valence": 0.9,
    "tempo_bpm": 180,
    "danceability": 1.0,
    "likes_acoustic": False,
}

EXTREME_VALUES = {
    "genre": "classical",
    "mood": "calm",
    "energy": 2.0,
    "valence": -1.0,
    "tempo_bpm": 1000,
    "danceability": -0.5,
    "likes_acoustic": True,
}

NO_MATCHING_CATEGORIES = {
    "genre": "unknown-genre",
    "mood": "unknown-mood",
    "energy": 0.5,
}

MINIMAL_PROFILE = {
    "genre": "pop",
}

CONTRADICTORY_ACOUSTIC_PROFILE = {
    "genre": "rock",
    "mood": "intense",
    "energy": 0.9,
    "likes_acoustic": True,
}

ADVERSARIAL_PROFILES = {
    "Conflicting High-Energy Sad": CONFLICTING_HIGH_ENERGY_SAD,
    "Extreme Values": EXTREME_VALUES,
    "No Matching Categories": NO_MATCHING_CATEGORIES,
    "Minimal Profile": MINIMAL_PROFILE,
    "Contradictory Acoustic": CONTRADICTORY_ACOUSTIC_PROFILE,
}


def main() -> None:
    songs = load_songs("data/songs.csv") 
    print(f"Loaded songs: {len(songs)}")

    profiles = {"High-Energy Pop": HIGH_ENERGY_POP, **ADVERSARIAL_PROFILES}
    for profile_name, user_prefs in profiles.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print(f"\n{profile_name} - Top recommendations:\n")
        for song, score, explanation in recommendations:
            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print()


if __name__ == "__main__":
    main()
