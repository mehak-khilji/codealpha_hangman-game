import random

def hangman():
    words = ['london', 'america', 'turkey', 'italy', 'canada']
    word = random.choice(words)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = 6
    display_word = ['_' for _ in word]

    print("Welcome to Hangman!")
    print("Guess the word")

    while incorrect_guesses < max_incorrect and '_' in display_word:
        print("\nWord: " + ' '.join(display_word))
        print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            for index, letter in enumerate(word):
                if letter == guess:
                    display_word[index] = guess
            print("Great guess!")
        else:
            incorrect_guesses += 1
            print("Wrong guess!")

    if '_' not in display_word:
        print(f"\nCongratulations! You guessed the word: {word}")
    else:
        print(f"\nGame over! The word was: {word}")

if __name__ == "__main__":
    hangman()
