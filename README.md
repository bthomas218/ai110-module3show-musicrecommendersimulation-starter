# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

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

This remains a deliberately small, explainable profile. Mood is weighted slightly more than genre because it better represents what the user wants right now, while genre still prevents recommendations from feeling musically unrelated.

### Algorithm Recipe

For every song in `data/songs.csv`:

1. Award 30 points for an exact mood match.
2. Award 25 points for an exact genre match.
3. Add up to 20 points for how closely the song's energy matches `target_energy`.
4. Add up to 10 points for valence similarity.
5. Add up to 7 points for matching the user's acoustic preference.
6. Add up to 5 points for tempo similarity.
7. Add up to 3 points for danceability similarity.
8. Save the song, total score, and a short explanation of the matching features.

The numerical feature scores will be normalized so that closer values receive more points. After every song has been scored, the system will sort the results from highest to lowest and return the top `k` recommendations.

Potential bias: this system may over-prioritize the user's declared genre and mood, causing it to miss excellent songs from other genres or songs that match the user's current mood but not their favorite genre. The small catalog, fixed labels, and limited profile also bias results toward songs whose features happen to be represented in the dataset. A boolean `likes_acoustic` preference may further oversimplify a preference that is usually gradual rather than all-or-nothing.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

   ```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

```text
Loaded songs: 18

Top recommendations:

Sunrise City - Score: 74.60
Because: genre match (+25.0); mood match (+30.0); energy similarity (+19.6)

Rooftop Lights - Score: 49.20
Because: genre mismatch (+0.0); mood match (+30.0); energy similarity (+19.2)

Gym Hero - Score: 42.40
Because: genre match (+25.0); mood mismatch (+0.0); energy similarity (+17.4)

Night Drive Loop - Score: 19.00
Because: genre mismatch (+0.0); mood mismatch (+0.0); energy similarity (+19.0)

Velvet Calle - Score: 18.60
Because: genre mismatch (+0.0); mood mismatch (+0.0); energy similarity (+18.6)
```

**Screenshot or video** _(optional)_: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

The recommender was tested with adversarial profiles designed to expose
unexpected scoring behavior.

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

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this
