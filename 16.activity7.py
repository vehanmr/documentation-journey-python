# import random
#
# print("Welcome to Hangman!")
#
# words = ["hacker", "bounty", "random"]
# secret_word = random.choice(words)
# print("You get 5 guesses")
# display_word = []
# for letter in secret_word:
#     display_word += "_"
# print(display_word)
#
# num = 0
# game_over = False
#
# while not game_over:
#     guess = input("Guess a letter ").lower()
#     for position in range(len(secret_word)):
#         letter = secret_word[position]
#         if letter == guess:
#             display_word[position] = letter
#     if guess not in secret_word:
#         num += 1
#         guesses_left = 5 - num
#         print(f"You have {guesses_left} guesses left")
#         if num >= 5:
#             print("You Loser")
#             game_over = True
#     print(display_word)
#
#     if "_" not in display_word:
#         print("You Win")
#         game_over = True


import random

# List of words to choose from
word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]

# Select a random word from the list
secret_word = random.choice(word_list)

# Initialize variables
remaining_guesses = 5
guessed_letters = []
display_word = ["_"] * len(secret_word)

# Main game loop
while remaining_guesses > 0:
    # Display the current state of the word
    print(" ".join(display_word))
    print(f"Remaining guesses: {remaining_guesses}")

    # Ask the player for a guess
    guess = input("Guess a letter: ").lower()

    # Check if the guess is a single letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    # Check if the letter has already been guessed
    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    # Add the guessed letter to the list of guessed letters
    guessed_letters.append(guess)

    # Check if the guessed letter is in the secret word
    if guess in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        print("Incorrect guess.")
        remaining_guesses -= 1

    # Check if the player has guessed the entire word
    if "".join(display_word) == secret_word:
        print("Congratulations! You've guessed the word:", secret_word)
        break

# Game over
if "".join(display_word) != secret_word:
    print("Sorry, you're out of guesses. The word was:", secret_word)

