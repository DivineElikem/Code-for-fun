import string
import random

WORDLIST_FILENAME = "words.txt"

def is_word_guessed(secret_word, letters_guessed):
    if letters_guessed[-1] in secret_word:
        is_guessed = True
    else:
        is_guessed = False
    return is_guessed


def get_guessed_word(secret_word, letters_guessed):
    return ''.join(letter if letter in letters_guessed else '_ ' for letter in secret_word)


def get_available_letters(letters_guessed):
    return ''.join(letter if letter not in letters_guessed else '' for letter in string.ascii_lowercase)


def load_words():
    print("Loading word list from file...")
    with open(WORDLIST_FILENAME, 'r') as inFile:
        wordlist = inFile.read().split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    return random.choice(wordlist)

print("You have 3 warnings")
wordlist = load_words()
secret_word = choose_word(wordlist)
print("Welcome to the game Hangman!\nI am thinking of a word that is", len(secret_word), "letters long")
print("----------------\nYou have", 6, "guesses left.")
print("Available letters:", string.ascii_lowercase)

guesses_remaining = 6
letters_guessed = ''
warnings_remaining = 3
unique_letters = ''

while True:
    letter_guessed = str.lower(input("Please guess a letter: "))
    for x in secret_word:
        if x not in unique_letters:
            unique_letters += x

    if str.isalpha(letter_guessed):
        letters_guessed += letter_guessed
        is_guessed = is_word_guessed(secret_word, letters_guessed)
        word_guessed = get_guessed_word(secret_word, letters_guessed)
        available_letters = get_available_letters(letters_guessed)

        if letter_guessed in letters_guessed[:-1]:
            warnings_remaining -= 1

            if warnings_remaining >= 0:
                print("Oops! you've already guessed that letter. You have", warnings_remaining, "warnings left:", word_guessed)
            else:
                guesses_remaining -= 1
                if guesses_remaining <= 0:
                    print("Sorry you ran out of guesses. The word was", secret_word + ".")
                    break
                print("Oops! you've already guessed that letter. You have no warnings left so you lose one guess:", word_guessed)
                if guesses_remaining >= 0:
                    print("You have", guesses_remaining, "guesses left")
            continue

        elif is_guessed:
            print("Good guess:", word_guessed, "\n------------------")
            if word_guessed == secret_word:
                print("Congratulations, you won!")
                print("Your total score for the game is:", len(unique_letters) * guesses_remaining)
                break
            print("You have", guesses_remaining, "guesses left")
            print("Available letters:", available_letters)

        else:
            print("Oops! That letter is not in my word:", word_guessed, "\n--------------------")
            if letter_guessed in 'aeiou':
                guesses_remaining -= 2
            else:
                guesses_remaining -= 1
            if guesses_remaining <= 0:
                print("Sorry you ran out of guesses. The word was", secret_word + ".")
                break
            if guesses_remaining >= 0:
                print("You have", guesses_remaining, "guesses left")
            print("Available letters:", available_letters)
    else:
        warnings_remaining -= 1
        if warnings_remaining >= 0:
            print("Oops! That is not a valid letter. You have", warnings_remaining, "warnings left:", word_guessed)
        else:
            guesses_remaining -= 1
            if guesses_remaining <= 0:
                print("Sorry, you ran out of guesses. The word was", secret_word + ".")
                break
            print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:", word_guessed)
        continue
