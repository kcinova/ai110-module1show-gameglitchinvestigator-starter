
# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.

It wrote the code, ran away, and now the game is unplayable.

- You can't win.

- The hints lie to you.

- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`

2. Run the app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.

2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*

3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.

4. **Refactor & Test.**

   - Move the logic into `logic_utils.py`.

   - Run `pytest` in your terminal.

   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- **Game's purpose:** A number guessing game built in Streamlit. The player guesses a number between 1 and 100, gets "higher/lower" hints, and tries to find the secret number within the allowed attempts.

- **Bugs found:** (1) the high/low hints were inverted, (2) the attempts counter was off by one, (3) the score could go negative, and (4) the guess history lagged one guess behind and never reset on "New Game."

- **Fixes applied:** (1) corrected the inverted hint logic in `check_guess()` so a guess above the secret says "Go LOWER" and below says "Go HIGHER"; (2) fixed "New Game" so it safely resets the secret, attempts, score, status, history, and input without crashing. The history-lag and attempts-counter issues are documented as known remaining issues in `reflection.md`.

## 📸 Demo Walkthrough

A sample game with the fixes applied:

1. The app starts and picks a secret number (e.g. 71). "Developer Debug Info" can be expanded to view it.

2. User enters a guess of 2 → game returns "Go HIGHER!" (correct, since 2 is below 71).

3. User enters a guess of 90 → game returns "Go LOWER!" (correct, since 90 is above 71).

4. User enters 71 → game returns "🎉 Correct!" and the guess is recorded.

5. User clicks "New Game" → the secret, score, attempts, and history all reset cleanly with no error, ready for a fresh round.

## 🧪 Test Results

```
$ python3 -m pytest tests/test_game_logic.py -v
tests/test_game_logic.py::test_guess_too_high PASSED       [ 33%]
tests/test_game_logic.py::test_guess_too_low PASSED        [ 66%]
tests/test_game_logic.py::test_guess_correct PASSED        [100%]
========================= 3 passed in 0.42s =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]

