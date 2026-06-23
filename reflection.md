# 💭 Reflection: Game Glitch Investigator

## 1. What was broken when you started?

When I first ran the game it loaded fine and looked complete, but several things were off. While playing twice on Normal difficulty (range 1-100), I found multiple glitches: the hints were backwards, the attempts counter didn't add up, the score went negative, and the guess history lagged and never reset.

**Bug 1 - Hints are inverted.** Guessing below the secret should say "Go HIGHER"; guessing above should say "Go LOWER." Instead, with the secret at 24, guessing 23 (too low) showed "Go LOWER!" - the high/low logic is reversed, so the hints actively mislead the player.

**Bug 2 - Attempts counter is inconsistent.** With 8 attempts allowed, "Attempts left" should start at 8 and decrease by 1 per guess. Instead it showed 7 before any guess was made, and started at 1 internally.

**Bug 3 - Score goes negative.** Score should never drop below 0, but after a few guesses it showed -10.

**Bug 4 - Guess history is delayed and not reset.** History should show each guess immediately and clear on "New Game." Instead it updated one guess behind and kept the previous game's history.

**Bug Reproduction Log**

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess of 23 (secret 24) | "Go HIGHER" hint | "Go LOWER!" hint shown | none |
| Fresh game, no guess yet | "Attempts left: 8" | "Attempts left: 7" | none |
| 2-3 guesses on one game | Score stays >= 0 | Score showed -10 | none |
| Click "New Game" after playing | History clears | History still showed previous guesses; later crashed | StreamlitAPIException |

---

## 2. How did you use AI as a teammate?

I used the AI coding assistant built into VS Code, starting a fresh chat per bug and reviewing every diff before accepting it.

**A correct suggestion:** For the inverted hint bug, the AI correctly identified that check_guess() returned the opposite direction message and that the comparison branches were paired with the wrong messages. It flipped them. I verified in the live game: with the secret at 71, guessing 2 (too low) now correctly showed "Go HIGHER!" The fix was right on the first try.

**An incorrect / misleading suggestion:** For the history bug, the AI's first fix sounded confident but was wrong. It tried to clear the input with st.session_state[f"guess_input_{difficulty}"] = "", which crashed with a StreamlitAPIException because you can't modify a widget's state after the widget is instantiated. I caught this by re-running the live game instead of trusting the explanation, sent the error back, and its second attempt used a reset_guess_input flag to clear the input safely on the next rerun, fixing the crash.

---

## 3. Debugging and testing your fixes

I verified fixes two ways: manually in the running app, and with automated pytest. For the hint fix I wrote tests/test_game_logic.py with three cases - a guess above the secret returns "Too High", a guess below returns "Too Low", and an exact match returns "Win". All three passed (3 passed in 0.42s), confirming the logic at the code level, not just visually. The AI helped me design these tests by suggesting the input/secret pairs to cover each branch. For the New Game fix, I confirmed in the browser that history, score, and status reset cleanly with no crash.

**Known remaining issues:** I fixed two bugs cleanly rather than rushing all four. The history still displays one guess behind due to Streamlit's rerun timing, and the attempts counter is off by one. These would be the next targets.

---

## 4. What did you learn about Streamlit and state?

Streamlit re-runs the entire script top to bottom every time you interact with anything - click a button, type in a box. Because of that, normal variables reset each run, so anything that needs to persist (the secret number, score, history) has to live in st.session_state, which survives between reruns. The trickiest part I learned: you can't change a widget's value in session_state after that widget has already been created in the same run, which is exactly what caused the New Game crash.

---

## 5. Looking ahead: your developer habits

One habit I want to reuse is writing a quick automated test to confirm a fix instead of only checking by hand - it caught that my logic was right at the source, and it's reusable. With Git, committing in small steps (bugs logged, fixes applied, tests added) kept my progress organized.

One thing I'd do differently: I'd test the AI's fixes in the live app immediately before accepting them, rather than trusting a confident-sounding explanation - that's how the New Game crash slipped through at first.

This project changed how I think about AI-generated code: it can be confidently wrong, so my job is to verify and stay in control, not just accept what looks right.
