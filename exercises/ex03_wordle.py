# My Approach to a Structured Wordle!

__author__ = "730690615"


def contains_char(word, char):
    """Check if char is contained in the word."""
    assert len(char) == 1  # Ensure char is a single character
    i = 0
    while i < len(word):
        if word[i] == char:
            return True
        i += 1
    return False


def emojified(guess, secret):
    """Generate emoji-based feedback for the guess."""
    assert len(guess) == len(secret)  # Ensure guess and secret have the same length
    feedback = ""
    i = 0
    while i < len(secret):
        if guess[i] == secret[i]:
            feedback += "🟩"  # Green for correct character and position
        elif contains_char(secret, guess[i]):
            feedback += "🟨"  # Yellow for correct character but wrong position
        else:
            feedback += "⬜"  # White for incorrect character
        i += 1
    return feedback


def input_guess(expected_length):
    """Prompt the user for a guess of the expected length."""
    guess = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        print(f"That wasn't {expected_length} chars! Try again:")
        guess = input(f"Enter a {expected_length} character word: ")
    return guess


def main() -> None:
    """The entry point of the Wordle game."""
    secret = "codes"  # You can change the secret word here
    max_turns = 6
    turns = 0
    won = False

    print("Welcome to Wordle!")

    while turns < max_turns and not won:
        turns += 1
        print(f"=== Turn {turns}/{max_turns} ===")
        guess = input_guess(len(secret))
        feedback = emojified(guess, secret)
        print(feedback)

        if guess == secret:
            won = True

    if won:
        print(f"You won in {turns}/{max_turns} turns!")
    else:
        print(f"X/{max_turns} - Sorry, try again tomorrow!")

    if __name__ == "__main__":
        main()
