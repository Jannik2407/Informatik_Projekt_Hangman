from wordlist import get_word_by_difficulty                                                         ## Importiert Funktion zum Laden eines Wortes basierend auf dem Schwierigkeitsgrad
from gallows import display_hangman                                                                 ## Importiert Funktion zum Anzeigen des Galgens

def display_word(word, guessed_letters):
    display = ""                                                                                    ## Speichert die sichtbar dargestellten Buchstaben und Unterstriche
    for letter in word:
        if letter in guessed_letters:                                                               ## Wenn der Buchstabe schon geraten wurde:
            display += letter + " "                                                                     ## Buchstaben anzeigen
        else:
            display += "_ "                                                                             ## Sonst Unterstrich anzeigen
    return display.strip()                                                                          ## Entfernt das letzte Vorzeichen

def play_game():
    difficulty =input("Wählen Sie einen Schwierigkeitsgrad aus (leicht/mittel/schwer):").lower()
    word = get_word_by_difficulty(difficulty)                                                       ## Holt das passende Wort basierend auf dem Schwierigkeitsgrad

    guessed_letters = []                                                                            ## Liste aller geratenen Buchstaben
    wrong_guesses = 0                                                                               ## Anzahl fehlerhafter Versuche
    max_wrong_guesses = 6                                                                           ## Maximal erlaubte Fehlversuche
    
    while wrong_guesses < max_wrong_guesses:                                                        ## Spiel läuft, solange nicht verloren
        print("Wort:", display_word(word, guessed_letters))

        guess = input("Rate einen Buchstaben: ").lower()

        if len(guess) != 1 or not guess.isalpha():                                                  ## Prüft, ob Eingabe gültig ist
            print("Bitte einen Buchstaben eingeben!")
            continue

        guessed_letters.append(guess)                                                               ## Buchstabe wird gespeichert

        if guess in word:                                                                           ## Richtiger Buchstabe
            print("Richtig!")

        else:
            wrong_guesses += 1                                                                      ## Falscher Buchstabe
            display_hangman(wrong_guesses)                                                          ## Galgen anzeigen

        if all(letter in guessed_letters for letter in word):                                       ## Prüft, ob alle Buchstaben erraten wurden
            print("Gewonnen! Das Wort war:", word)
            return                                                                                  ## Spiel beenden, wenn gewonnen


    print("Verloren! Das Word war:", word)                                                          ## Spiel verloren; Wort anzeigen