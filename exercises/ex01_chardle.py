"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730690615"

# Prompting the Inputs
word = input("Enter a 5-character word: ")
char = input("Enter a single character: ")

# Move the length check outside of the main code
if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
# Move the length of character outside of the main code
elif len(char) != 1:
    print("Error: Character must be a single character.")
    exit()
else:
    found = False

    # Create a variable to count matching characters
    count = 0

    if word[0] == char:
        print(f"Searching for {char} in {word}")
        print(f"{char} found at index 0")
        count += 1
        found = True
    if word[1] == char:
        print(f"Searching for {char} in {word}")
        print(f"{char} found at index 1")
        count += 1
        found = True
    if word[2] == char:
        print(f"Searching for {char} in {word}")
        print(f"{char} found at index 2")
        count += 1
        found = True
    if word[3] == char:
        print(f"Searching for {char} in {word}")
        print(f"{char} found at index 3")
        count += 1 
        found = True
    if word[4] == char:
        print(f"Searching for {char} in {word}")
        print(f"{char} found at index 4")
        count += 1
        found = True

    # Check the count to determine the result

    if count == 1:
        print(f"{count} instance of {char} found in {word}")
    else:
        print(f"{count} instances of {char} found in {word}")

    # Check the flag to determine the result
    if not found:
        print(f"No instances of {char} found in {word}")