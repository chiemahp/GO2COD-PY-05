import random

def choose_word():
    words = ['python', 'Artificial Intelligence', 'programming', 'developer', 'algorithm','Machine learning']
    return random.choice(words)

def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        --------
        """
    ]
    return stages[tries]

def play_hangman():
    word = choose_word()
    word_letters = set(word)
    guessed_letters = set()
    tries = 6

    print("Welcome to Hangman!")
    print(display_hangman(tries))
    print("Word: " + " ".join("_" for _ in word))

    while tries > 0 and word_letters:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word_letters:
            word_letters.remove(guess)
            guessed_letters.add(guess)
            print("Good guess!")
        else:
            tries -= 1
            guessed_letters.add(guess)
            print("Wrong guess. You have {} tries left.".format(tries))

        print(display_hangman(tries))
        word_display = [letter if letter in guessed_letters else "_" for letter in word]
        print("Word: " + " ".join(word_display))

    if not word_letters:
        print("Congratulations! You guessed the word: " + word)
    else:
        print("Sorry, you ran out of tries. The word was: " + word)

if __name__ == "__main__":
    play_hangman()
