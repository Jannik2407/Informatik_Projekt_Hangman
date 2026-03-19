from wordlist import get_random_word_by_difficulty                                                  ## Importiert Funktion zum Laden eines Wortes basierend auf dem Schwierigkeitsgrad
from gallows import display_hangman                                                                 ## Importiert Funktion zum Anzeigen des Galgens


RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
PURPLE = "\033[95m"
RESET = "\033[0m"


def display_word(word, guessed_letters):
    display = ""                                                                                    ## Speichert die sichtbar dargestellten Buchstaben und Unterstriche
    for letter in word:
        if letter in guessed_letters:                                                               ## Wenn der Buchstabe schon geraten wurde:
            display += letter + " "                                                                     ## Buchstaben anzeigen
        else:
            display += "_ "                                                                             ## Sonst Unterstrich anzeigen
    return display.strip()                                                                          ## Entfernt das letzte Vorzeichen

def play_game():
    # Schleife für Schwierigkeitseingabe
    while True:
        difficulty = input("Geben Sie die Schwierigkeit ein (leicht, mittel oder schwer): ").lower()
        word = get_random_word_by_difficulty(difficulty)                                            ## Holt das passende Wort basierend auf dem Schwierigkeitsgrad
        if word is None:
            print("Ungültige Eingabe, geben Sie eine gültige Schwierigkeit ein.")
        else:
           break
                                                         
    guessed_letters = []                                                                            ## Liste aller geratenen Buchstaben
    wrong_guesses = 0                                                                               ## Anzahl fehlerhafter Versuche
    max_wrong_guesses = 6                                                                           ## Maximal erlaubte Fehlversuche
    
    while wrong_guesses < max_wrong_guesses:                                                        ## Spiel läuft, solange nicht verloren
        print("\nWort:", display_word(word, guessed_letters))

        guess = input("\nRaten Sie einen Buchstaben: ").lower()

        if len(guess) != 1 or not guess.isalpha():                                                  ## Prüft, ob Eingabe gültig ist
            print("Bisher geratene Buchstaben:", " ".join(sorted(guessed_letters)))                 # Liste der bisher geratenen Buchstaben anzeigen 
            print(YELLOW + "\nBitte geben Sie einen Buchstaben ein!" + RESET)
            continue

        if guess in guessed_letters:                                                                ## Doppelte Eingabe verhindern
            display_hangman(wrong_guesses)                                                          ## Galgen anzeigen
            print("Bisher geratene Buchstaben:", " ".join(sorted(guessed_letters)))                 # Liste der bisher geratenen Buchstaben anzeigen 
            print(YELLOW + f"\nDiesen Buchstaben ({guess}) haben Sie bereits geraten! Versuchen Sie einen anderen." + RESET)
            continue

        guessed_letters.append(guess)                                                               ## Buchstabe wird gespeichert

        if guess in word:                                                                           ## Richtiger Buchstabe
            display_hangman(wrong_guesses)                                                          ## Galgen anzeigen
            print("Bisher geratene Buchstaben:", " ".join(sorted(guessed_letters)))                 # Liste der bisher geratenen Buchstaben anzeigen 
            print(GREEN + "\nRichtig!" + RESET)

        else:
            wrong_guesses += 1                                                                      ## Falscher Buchstabe
            display_hangman(wrong_guesses)                                                          ## Galgen anzeigen
            print("Bisher geratene Buchstaben:", " ".join(sorted(guessed_letters)))                 # Liste der bisher geratenen Buchstaben anzeigen                                    
            print(RED + f"Falsch! \nDieser Buchstabe ({guess}) ist nicht im Wort." + RESET)

        if all(letter in guessed_letters for letter in word):                                       ## Prüft, ob alle Buchstaben erraten wurden
            print(PURPLE + "\nGewonnen! 🥳" + RESET)
            print("\nDas Wort war:", word)
            return                                                                                  ## Spiel beenden, wenn gewonnen


    print(RED + "\nVerloren! 😒" + RESET)
    print("\nDas Wort war:", word)                                                          ## Spiel verloren; Wort anzeigen