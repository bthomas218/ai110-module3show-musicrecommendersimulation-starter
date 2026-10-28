# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**

---

## 2. Intended Use

Describe what your recommender is designed to do and who it is for.

Prompts:

- What kind of recommendations does it generate
- What assumptions does it make about the user
- Is this for real users or classroom exploration

---

## 3. How the Model Works

The recommender compares each song with the user's preferred genre, mood, and
audio targets. A song receives 25 points for matching the preferred genre and
30 points for matching the preferred mood. It also receives points when its
energy, valence, tempo, or danceability is close to the user's target values.
If the user has an acoustic preference, the model includes that as well.

Songs that match more of the user's preferences receive higher scores. The
model sorts all songs from highest to lowest score and returns the top results,
along with short reasons explaining the matches. This is a simple,
rule-based approach: it does not learn from listening history or try to
understand a song beyond the features recorded in the catalog.

---

## 4. Data

Describe the dataset the model uses.

Prompts:

- How many songs are in the catalog
- What genres or moods are represented
- Did you add or remove data
- Are there parts of musical taste missing in the dataset

---

## 5. Strengths

Where does your system seem to work well

Prompts:

- User types for which it gives reasonable results
- Any patterns you think your scoring captures correctly
- Cases where the recommendations matched your intuition

---

## 6. Limitations and Bias

One weakness discovered during the adversarial-profile experiment is that the
energy score can dominate the recommendations because it is worth up to 40
points (after doubling), more than any other single feature. This can cause high-energy users to
receive songs with the right intensity but the wrong genre or mood. The system
also treats genre and mood as exact text matches, so related labels such as
`pop` and `indie pop` are considered completely different. As a result, the
recommender may create a narrow filter bubble instead of offering diverse
musical alternatives.

---

## 7. Evaluation

I tested six profiles: High-Energy Pop, Conflicting High-Energy Sad, Extreme
Values, No Matching Categories, Minimal Profile, and Contradictory Acoustic.
For each profile, I ran the recommender and examined the five highest-scoring
songs and the explanation attached to each score. I looked for songs that
matched the main preferences and for cases where unusual values or missing
preferences caused unexpected results.

The most surprising result was that `Gym Hero` appeared near the top for
several very different users. This happens because it has very high energy
(`0.93`), high danceability, and low acousticness. Since energy is worth up to
40 points, those features can outweigh a mismatch in mood or genre. The song
is not being understood as a universally good match; it is repeatedly winning
the mathematical comparison because several of its numbers are strong.

### Profile comparisons

- **High-Energy Pop vs. Conflicting High-Energy Sad:** Both profiles ask for
  high energy, so both favor `Gym Hero` and other energetic songs. High-Energy
  Pop ranks `Sunrise City` first because it matches both pop and happy, while
  the sad profile has no sad song that also matches its other strong features.
- **High-Energy Pop vs. Extreme Values:** High-Energy Pop uses realistic values,
  so `Sunrise City` earns points across many features. The extreme profile asks
  for values such as energy `2.0` and tempo `1000`, which are outside the
  catalog's ranges, so most similarity scores become zero and `Glass Cathedral`
  only leads because it matches classical.
- **High-Energy Pop vs. No Matching Categories:** The first profile receives
  genre, mood, and audio-feature points, so `Sunrise City` is clearly first.
  The second profile has unknown genre and mood values, so only its medium
  energy target matters and lower-energy songs rise to the top.
- **High-Energy Pop vs. Minimal Profile:** High-Energy Pop selects `Sunrise
  City` using several matching features. The Minimal Profile only asks for pop,
  so `Sunrise City` and `Gym Hero` tie on the genre points; the catalog order
  decides which one appears first.
- **High-Energy Pop vs. Contradictory Acoustic:** The first profile prefers
  happy pop, while the second prefers intense rock with acoustic music. `Storm
  Runner` wins for the second profile because it matches rock and intense,
  while `Gym Hero` remains nearby because it also has intense mood and high
  energy.
- **Conflicting High-Energy Sad vs. Extreme Values:** The sad profile still
  has a valid high-energy target, so `Gym Hero` can score strongly despite its
  sad mismatch. The extreme profile gets almost no numerical similarity points,
  so its results are driven mostly by the one exact genre match.
- **Conflicting High-Energy Sad vs. No Matching Categories:** The sad profile
  has a usable energy target of `0.9`, which favors `Gym Hero` and other energetic
  songs. The no-match profile has an energy target near the middle and no valid
  genre or mood match, so it favors songs near energy `0.5` instead.
- **Conflicting High-Energy Sad vs. Minimal Profile:** The sad profile adds
  many preferences and makes `Gym Hero` first because of its energy. The
  Minimal Profile ignores energy and mood, so it only sees the tie between the
  two pop songs.
- **Conflicting High-Energy Sad vs. Contradictory Acoustic:** Both profiles
  prefer high energy, but the sad profile has pop as its genre and the acoustic
  profile has rock and intense mood. That moves `Gym Hero` to first for the sad
  profile and `Storm Runner` to first for the acoustic profile.
- **Extreme Values vs. No Matching Categories:** Extreme Values produce almost
  no useful similarity points, so `Glass Cathedral` leads with its classical
  genre match. No Matching Categories still has a valid energy target, allowing
  songs such as `After the Rain` and `Backroad Letters` to compete on energy.
- **Extreme Values vs. Minimal Profile:** The extreme profile favors `Glass
  Cathedral` because of its classical label. The Minimal Profile favors the two
  pop songs because genre is its only preference.
- **Extreme Values vs. Contradictory Acoustic:** The extreme profile has
  invalid numerical targets and therefore produces low scores. The acoustic
  profile has valid rock, intense, and high-energy preferences, so `Storm
  Runner` receives strong points and ranks first.
- **No Matching Categories vs. Minimal Profile:** The no-match profile ranks
  songs near energy `0.5`, regardless of genre. The Minimal Profile ignores
  energy and selects pop songs, so the two profiles produce noticeably
  different top results.
- **No Matching Categories vs. Contradictory Acoustic:** The no-match profile
  has no valid genre or mood match and only rewards medium energy. The acoustic
  profile rewards rock, intense mood, high energy, and acousticness, making
  `Storm Runner` the clear leader.
- **Minimal Profile vs. Contradictory Acoustic:** The Minimal Profile favors
  `Sunrise City` and `Gym Hero` because both are pop. The acoustic profile favors
  `Storm Runner` because it matches rock and intense, although `Gym Hero` still
  appears because its energy and intense mood fit well.

---

## 8. Future Work

Ideas for how you would improve the model next.

Prompts:

- Additional features or preferences
- Better ways to explain recommendations
- Improving diversity among the top results
- Handling more complex user tastes

---

## 9. Personal Reflection

A few sentences about your experience.

Prompts:

- What you learned about recommender systems
- Something unexpected or interesting you discovered
- How this changed the way you think about music recommendation apps
