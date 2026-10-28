# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**VibeMatch 1.0**

---

## 2. Goal / Task

VibeMatch suggests songs for a user. It compares user preferences with song
features. It returns the five highest-scoring songs.

### Intended Use

This system is for classroom learning. It shows how simple recommendation rules
work. It can suggest songs for a small music collection.

### Non-Intended Use

This system is not a production music service. It should not make important
decisions about people. It should not be treated as a complete measure of a
person's taste.

---

## 3. Algorithm Summary

The recommender compares each song with the user's preferences. A mood match is
worth 30 points. A genre match is worth 12.5 points. Energy can add up to 40
points. Valence can add up to 10 points. Tempo can add up to 5 points.
Danceability can add up to 3 points. Acoustic preference can add up to 7 points.

Closer numeric values receive more points. Exact genre and mood matches receive
their full bonus. The model sorts songs by total score. It also explains why a
song received its score. It does not learn from listening history.

---

## 4. Data

The catalog has 18 songs. Each song has an ID, title, artist, genre, mood,
energy, tempo, valence, danceability, and acousticness. Most genres appear only
once. Lofi has three songs, and pop has two songs. This is a small sample.
It does not include lyrics, listening history, skips, or user ratings.

---

## 5. Strengths

The system is easy to understand. The score gives clear reasons for each song.
It works well when a user gives realistic energy and mood values. It also makes
clear changes when the user changes from low energy to high energy.

---

## 6. Limitations and Bias

Energy can dominate the results because it is worth up to 40 points. A song can
have the right energy but the wrong mood. Genre and mood use exact text
matches. For example, `pop` and `indie pop` are different labels. The small
catalog can also favor the genres and moods that have more songs.

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

I would validate all user values before scoring them. I would group related
genres and moods. I would add a diversity rule so one artist or style does not
fill the whole list.

---

## 9. Personal Reflection

I learned that small weight changes can change recommendation scores quickly.
I was surprised that `Gym Hero` appeared for many different profiles. Its high
energy and danceability made it strong even when its mood did not match. This
showed me that recommendation results depend heavily on the rules chosen by the
designer.
