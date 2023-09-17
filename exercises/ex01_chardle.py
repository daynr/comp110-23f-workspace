"""EX01 - Chardle - An Eager Approach to learning how to code a Wordle"""


__author__ = 730690615

# Get an input for a 5-character word and a single character in str() format.
word_input = str(input("Enter a 5-character word: "))
char_input = str(input("Enter a single character: "))

# Check if the word input is not exactly 5 characters long.
if len(word_input) != 5:
    print("Error: Word must contain 5 characters")
else:
    # Check if the character input is not a single character.
    if len(char_input) != 1:
        print("Error: Character must be a single character.")
    else:
        # Make the diagnostic message.
        diagnostic_message = "searching for " + char_input + "in " + word_input

        # Print the diagnostic message.
        print(diagnostic_message)

        # Check to see if the character was found.
        found = False

        # Look through the characters in the word string.
        for index in range(len(word_input)):
            # Check if the character at the current index matches the input character.
            if word_input[index] == char_input:
                # If a match is found, print a message indicating the character and its index.
                print(char_input + "found at index " + str(index))
                found = True

        # If the character was not found, print an appropriate message.
        if not found:
            print("no instances of " + char_input + "found in " + word_input)
