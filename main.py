from game_logic import play_game                                                                                            ## Importiert die Spiellogik-Funktion

def main_menu():                                                                                                            ## Endlosschleife für das Hauptmenü
    while True:
        print("\n---Hangman---")
        print("1 - Spiel starten")
        print("2 - Beenden")

        choice = input("Auswahl: ")                                                                                         ## Nutzer trifft eine Menüauswahl

        if choice == "1":
            play_game()                                                                                                     ## Startet das Spiel
        elif choice == "2":
            print("Programm beendet.")                                                                                      ## Verlässt die Schleife; Programmende
            break
        else:
            print("Ungültige Eingabe! Bitte geben Sie '1' um das Spiel zu starten oder '2' um das Spiel zu beenden.")       ## Fehlermeldung bei falscher Eingabe

def main():
    main_menu()                                                                                                             ## Einstiegspunkt: startet das Hauptmenü

if __name__ == "__main__":
    main()                                                                                                                  ## Führt main() nur aus, wenn Datei direkt gestartet wird