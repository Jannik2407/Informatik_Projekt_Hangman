'''
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
Projektname:        Hangman Spiel
Authoren:           Jannik Ast und Tobias Brechtenbreiter
Datum:              18. März 2026

Kurzbeschreibung:   Ein Textbasiertes Hangman-Spiel in Python.
                    Der Spieler kann zwischen drei  Schwierigkeitsgraden wählen und muss ein zufällig ausgewähltes Wort
                    Buchstabe für Buchstabe erraten.
                    Der Spieler hat 6 Möglichkeiten das Wort zu erraten, bevor das Spiel beendet wird.
                    Das Spiel zeigt den Galgen als ASCII-Art, informiert über richtig und flasch geratene Buchstaben
                    und führt eine Liste der geratenen Buchstaben.
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
'''


from game_logic import play_game                                                                                            ## Importiert die Spiellogik-Funktion

def main_menu():                                                                                                            ## Endlosschleife für das Hauptmenü
    while True:
        print("\n-----------------Hangman------------------")
        print("Geben Sie '1' ein, um das Spiel zu starten")
        print("Geben Sie '2' ein, um das Spiel zu beenden")

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