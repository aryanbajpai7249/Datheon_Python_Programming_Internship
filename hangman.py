import random

# Hangman stages
HANGMAN_STAGES = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]


def load_words(filename):
    """Load words from the text file."""
    try:
        with open(filename, "r") as file:
            words = [
                word.strip().lower()
                for word in file
                if word.strip().isalpha()
            ]

        if not words:
            print("No valid words found in the word list.")
            return []

        return words

    except FileNotFoundError:
        print("Error: english_words.txt not found.")
        return []


def display_word(secret_word, guessed_letters):
    """Display guessed letters and underscores."""
    result = []

    for letter in secret_word:
        if letter in guessed_letters:
            result.append(letter)
        else:
            result.append("_")

    return " ".join(result)


def play_game(words):
    """Run one Hangman game."""
    secret_word = random.choice(words)

    guessed_letters = set()
    wrong_guesses = 0
    max_attempts = 6

    print("\n" + "=" * 40)
    print("       HANGMAN WORD GUESSING GAME")
    print("=" * 40)

    while wrong_guesses < max_attempts:

        print(HANGMAN_STAGES[wrong_guesses])

        print("Word:", display_word(secret_word, guessed_letters))
        print("Guessed letters:",
              " ".join(sorted(guessed_letters)) if guessed_letters else "None")

        print("Wrong attempts:", wrong_guesses, "/", max_attempts)

        guess = input("\nEnter a letter: ").strip().lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabet letter.")
            continue

        # Duplicate guess
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        # Correct guess
        if guess in secret_word:
            print("Correct guess!")

        # Wrong guess
        else:
            wrong_guesses += 1
            print("Wrong guess!")

        # Check win
        if all(letter in guessed_letters for letter in secret_word):
            print("\n" + "=" * 40)
            print("           🎉 YOU WON! 🎉")
            print("=" * 40)
            print("The word was:", secret_word)
            print(HANGMAN_STAGES[wrong_guesses])
            return

    # Game over
    print(HANGMAN_STAGES[wrong_guesses])

    print("\n" + "=" * 40)
    print("           GAME OVER!")
    print("=" * 40)
    print("The word was:", secret_word)


def main():
    words = load_words("english_words.txt")

    if not words:
        return

    while True:
        play_game(words)

        again = input("\nPlay again? (y/n): ").strip().lower()

        if again != "y":
            print("\nThanks for playing Hangman!")
            break


if __name__ == "__main__":
    main()