from wordlist import get_word_by_difficulty
from gallows import display_hangman

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def play_game():
    difficulty =input("Wählen Sie einen Schwierigkeitsgrad aus (leicht/mittel/schwer):").lower()
    word = get_word_by_difficulty(difficulty)

    guessed_letters = []
    wrong_guesses = 0
    max_wrong_guesses = 6
    
    while wrong_guesses < max_wrong_guesses:
        print("Wort:", display_word(word, guessed_letters))

        guess = input("Rate einen Buchstaben: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Bitte einen Buchstaben eingeben!")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Richtig!")

        else:
            wrong_guesses += 1
            display_hangman(wrong_guesses)

        if all(letter in guessed_letters fpr letter in word):
            print("Gewonnen! Das Wort war:", word)

            
    print("Verloren! Das Word war:", word)
                