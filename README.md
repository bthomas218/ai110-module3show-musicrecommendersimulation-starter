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

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** _(optional)_: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

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
