"""Tests for the game logic, focused on the high/low hint fix."""
from app import check_guess


def test_guess_too_high():
    # Guess above the secret should report "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # Guess below the secret should report "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


def test_guess_correct():
    # Exact match should report a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"
