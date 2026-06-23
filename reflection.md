# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| | | | |
| | | | |
| | | | |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

While playing the game twice on Normal difficulty (range 1-100), I found several glitches:

**Bug 1 - Hints are inverted.**
Expected: guessing below the secret should say "Go HIGHER"; guessing above should say "Go LOWER."
Actual: with the secret at 24, guessing 23 (too low) showed "Go LOWER!" - the high/low logic is reversed, so the hints actively mislead the player.

**Bug 2 - Attempts counter is inconsistent.**
Expected: with 8 attempts allowed, "Attempts left" should start at 8 and decrease by 1 per guess.
Actual: "Attempts left" showed 7 before any guess was made, and the relationship between attempts used, allowed, and remaining doesn't add up.

**Bug 3 - Score goes negative.**
Expected: score should never drop below 0.
Actual: after a few guesses the score showed -10, which shouldn't be possible.

**Bug 4 - Guess history is delayed and not reset.**
Expected: history shows each guess immediately, and "New Game" clears it.
Actual: history updates one guess behind the actual input, and "New Game" keeps the previous game's history.

### Bug Reproduction Logs

| Input Used | Expected Behavior | Actual Behavior | Console Error / Output |
|------------|-------------------|-----------------|------------------------|
| Guess of 23 (secret 24) | "Go HIGHER" hint | "Go LOWER!" hint shown | none |
| Fresh game, no guess yet | "Attempts left: 8" | "Attempts left: 7" | none |
| 2-3 guesses on one game | Score stays >= 0 | Score showed -10 | none |
| Click "New Game" after playing | History clears | History still shows previous guesses | none |
