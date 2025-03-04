"""A One-Shot to Success!"""

__author__ = "730690615"

# Named constants of the emojis
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# Secret word
secret_word = "python"

# Length of the secret word
secret_word_length = len(secret_word)

while True:
    try:
        # Ask the user for a guess
        user_guess = input(f"What is your {len(secret_word)}-letter guess? ")

    # Check if the guess has the correct length
        if len(user_guess) != secret_word_length:
            print(f"That was not {len(secret_word)} letters! Try again: ")
        else:
            # Define variables
            index = 0
            result_emoji = ""

        # Iterate through each character in the guess
        while index < secret_word_length:
            # Test if the current index of the guessed word matches the secret word
            if user_guess[index] == secret_word[index]:
                # If they match concatenate a GREEN_BOX emoji
                result_emoji += GREEN_BOX
            elif secret_word.count(user_guess[index]) > 0:
                # If the letter is in the word but at the wrong position concatenate a YELLOW_BOX emoji
                result_emoji += YELLOW_BOX
            else:
                # If they don't match concatenate a WHITE_BOX emoji
                result_emoji += WHITE_BOX

            # Move to the next index
            index += 1

        # Print the resulting emoji string
        print(result_emoji)

        # Check if the guess is correct
        if user_guess == secret_word:
            print("Woo! You got it!")
            break

        else:
            print("Not quite. Play again soon!")

    except EOFError:
        # Hopful to fix this error
        print("EOFError: Found.")
        break