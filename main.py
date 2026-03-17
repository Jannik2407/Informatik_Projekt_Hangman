from game_logic import play_game

def main_menu():
    while true:
        print("---Hangman---")
        print("1 - Spiel starten")
        print("2 - Beenden")

        choice = input("Auswahl: ")

        if choice == "1":
            play_game()
        elif choice == "2":
            print("Programm beendet.")
            break
        else:
            print("Ungültige Eingabe! Bitte geben Sie "1" um das Spiel zu starten "
            "       oder "2" um das Spiel zu beenden")

def main():
    main_menu()

if __name__ == "__main__":
    main()