# 🎵 Music Recommender Simulation

## Project Summary

This project is a small, explainable music recommender. It compares user
preferences with 18 songs in a CSV catalog. It scores each song and prints the
top five recommendations with short explanations.

---

## How The System Works

Real-world recommendation systems learn from many signals, including what users listen to, skip, save, or add to playlists, as well as the attributes of each song. They often combine collaborative filtering, which finds patterns across users, with content-based filtering, which compares song features. Our simulation will focus on a simple, explainable content-based approach: it will prioritize matching a user's favorite genre and mood, then use numerical audio features such as energy, tempo, valence, danceability, and acousticness to rank songs by how closely they fit the user's preferences.

The `Song` object will use these features:

- `id`
- `title`
- `artist`
- `genre`
- `mood`
- `energy`
- `tempo_bpm`
- `valence`
- `danceability`
- `acousticness`

The updated `UserProfile` will store the user's main categorical preferences and numeric targets:

- `favorite_genre`
- `favorite_mood`
- `target_energy`
- `target_valence`
- `target_tempo_bpm`
- `target_danceability`
- `likes_acoustic`

This remains a deliberately small, explainable profile. Energy is currently
the strongest numeric preference. Genre and mood still add important exact
match bonuses.

### Algorithm Recipe

For every song in `data/songs.csv`:

1. Award 30 points for an exact mood match.
2. Award 12.5 points for an exact genre match.
3. Add up to 40 points for how closely the song's energy matches `target_energy`.
4. Add up to 10 points for valence similarity.
5. Add up to 7 points for matching the user's acoustic preference.
6. Add up to 5 points for tempo similarity.
7. Add up to 3 points for danceability similarity.
8. Save the song, total score, and a short explanation of the matching features.

The numerical feature scores will be normalized so that closer values receive more points. After every song has been scored, the system will sort the results from highest to lowest and return the top `k` recommendations.

Potential bias: the energy weight can push energetic songs above better mood or
genre matches. The small catalog and fixed labels can also hide useful songs
from underrepresented genres. The boolean `likes_acoustic` preference is a
simple approximation of a more gradual taste.

---

## Getting Started

### Setup

1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/) if it
   is not already installed.

   ```bash
   uv sync
   ```

2. Run the recommender:

```bash
uv run python src/main.py
```

### Running Tests

Run the starter tests with:

```bash
uv run pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

```text
Loaded songs: 18

High-Energy Pop - Top recommendations:

Sunrise City - Score: 104.64
Rooftop Lights - Score: 89.66
Gym Hero - Score: 69.41
Velvet Calle - Score: 59.03
Neon Gravity - Score: 57.31
```

The full profile output is recorded in the Experiments section below. The
adversarial logs there were captured before the later energy-weight change.

---

## Experiments You Tried

The recommender was tested with adversarial profiles designed to expose
unexpected scoring behavior. The scores in these logs document that earlier
experiment; I also tried doubling the energy and halving the genreweight, but it did not result in any significant differenes. Run `uv run python src/main.py` for current scores.

### Conflicting High-Energy Sad

```text
Gym Hero - Score: 63.39
Because: genre match (+25.0); mood mismatch (+0.0); energy similarity (+19.4); valence similarity (+8.7); tempo similarity (+1.0); danceability similarity (+2.6); acousticness preference (+6.6)
Sunrise City - Score: 60.91
Because: genre match (+25.0); mood mismatch (+0.0); energy similarity (+18.4); valence similarity (+9.4); tempo similarity (+0.0); danceability similarity (+2.4); acousticness preference (+5.7)
Neon Gravity - Score: 38.77
Because: genre mismatch (+0.0); mood mismatch (+0.0); energy similarity (+19.0); valence similarity (+9.9); tempo similarity (+0.7); danceability similarity (+2.8); acousticness preference (+6.4)
Storm Runner - Score: 36.55
Because: genre mismatch (+0.0); mood mismatch (+0.0); energy similarity (+19.8); valence similarity (+5.8); tempo similarity (+2.7); danceability similarity (+2.0); acousticness preference (+6.3)
Iron Horizon - Score: 35.17
Because: genre mismatch (+0.0); mood mismatch (+0.0); energy similarity (+18.6); valence similarity (+4.2); tempo similarity (+4.0); danceability similarity (+1.7); acousticness preference (+6.7)
```

### Extreme Values

```text
Glass Cathedral - Score: 32.61
Because: genre match (+25.0); mood mismatch (+0.0); energy similarity (+0.0); valence similarity (+0.0); tempo similarity (+0.0); danceability similarity (+1.0); acousticness preference (+6.6)
Spacewalk Thoughts - Score: 6.71
Because: genre mismatch (+0.0); mood mismatch (+0.0); energy similarity (+0.0); valence similarity (+0.0); tempo similarity (+0.0); danceability similarity (+0.3); acousticness preference (+6.4)
Coffee Shop Stories - Score: 6.23
Because: genre mismatch (+0.0); mood mismatch (+0.0); energy similarity (+0.0); valence similarity (+0.0); tempo similarity (+0.0); danceability similarity (+0.0); acousticness preference (+6.2)
Library Rain - Score: 6.02
Because: genre mismatch (+0.0); mood mismatch (+0.0); energy similarity (+0.0); valence similarity (+0.0); tempo similarity (+0.0); danceability similarity (+0.0); acousticness preference (+6.0)
Focus Flow - Score: 5.46
Because: genre mismatch (+0.0); mood mismatch (+0.0); energy similarity (+0.0); valence similarity (+0.0); tempo similarity (+0.0); danceability similarity (+0.0); acousticness preference (+5.5)
```

### No Matching Categories

```text
After the Rain - Score: 19.20
Because: genre mismatch (+0.0); mood mismatch (+0.0); energy similarity (+19.2)
Backroad Letters - Score: 18.40
Because: genre mismatch (+0.0); mood mismatch (+0.0); energy similarity (+18.4)
Midnight Coding - Score: 18.40
Because: genre mismatch (+0.0); mood mismatch (+0.0); energy similarity (+18.4)
Focus Flow - Score: 18.00
Because: genre mismatch (+0.0); mood mismatch (+0.0); energy similarity (+18.0)
Wildflower Road - Score: 17.80
Because: genre mismatch (+0.0); mood mismatch (+0.0); energy similarity (+17.8)
```

### Minimal Profile

```text
Sunrise City - Score: 25.00
Because: genre match (+25.0)
Gym Hero - Score: 25.00
Because: genre match (+25.0)
Midnight Coding - Score: 0.00
Because: genre mismatch (+0.0)
Storm Runner - Score: 0.00
Because: genre mismatch (+0.0)
Library Rain - Score: 0.00
Because: genre mismatch (+0.0)
```

### Contradictory Acoustic

```text
Storm Runner - Score: 75.50
Because: genre match (+25.0); mood match (+30.0); energy similarity (+19.8); acousticness preference (+0.7)
Gym Hero - Score: 49.75
Because: genre mismatch (+0.0); mood match (+30.0); energy similarity (+19.4); acousticness preference (+0.4)
Sunrise City - Score: 19.66
Because: genre mismatch (+0.0); mood mismatch (+0.0); energy similarity (+18.4); acousticness preference (+1.3)
Rooftop Lights - Score: 19.65
Because: genre mismatch (+0.0); mood mismatch (+0.0); energy similarity (+17.2); acousticness preference (+2.4)
Neon Gravity - Score: 19.56
Because: genre mismatch (+0.0); mood mismatch (+0.0); energy similarity (+19.0); acousticness preference (+0.6)
```

These results show that the scorer treats each preference independently. It
does not detect contradictions, validate feature ranges, or prevent a sparse
profile from producing ties.

---

## Limitations and Risks

The recommender only works with this small catalog. It does not understand
lyrics, language, or listening history. Exact labels can miss related songs.
Invalid profile values can make similarity scores drop to zero. High-energy
songs can also appear for users who wanted a specific mood instead.

---

## Reflection

My biggest learning moment was how weights turn preferences into scores. Small weight
changes can change the results without changing the songs. The experiments
also showed that a simple recommender can repeat the same songs for different
users and create a narrow filter bubble. AI tools helped me explore more complex ranking methods than the
Initial implementation, but I had to be careful to avoid overfitting to the small catalog. I also learned that a simple, explainable system can still be useful for understanding how recommendations are made. If I extened this project the first thing I would do is make reccomandations based off listening history; There is a concept of "revealed preference" where a user may not know what they like until they hear it. I would also add more songs to the catalog and include more features, such as lyrics, language, and user ratings.

See the completed [model card](model_card.md) for the profile comparisons and
future improvement ideas.
