# Hangman-Spiel


## Kurzbeschreibung 
Dieses Programm ist ein textbasiertes Hangman-Spiel, das in Python implementiert wurde.
Der Spieler versucht, ein zufällig ausgewähltes Wort, Buchstabe für Buchstabe zu erraten.

Das Spiel bietet verschiedene Schwierigkeitsgrade und zeigt den Fortschritt visuell durch 
eine ASCII-Galgen-Darstellung.
Ziel ist es, das Wort zu erraten, bevor die maximale Anzahl an Fehlversuchen erreicht und 
die ASCII-Galgen-Darstellung vervollständigt ist.


## Teammitglieder 
- Tobias Brechtenbreiter
- Jannik Ast


## Verwendete Technologien 
- Programmiersprache: Python 3.11
- Entwicklungsumgebung: Visual Studio Code


## Hinweise 
- Das Spiel läuft vollständig über die Konsole.
- Es sind keine externen Bibliotheken erforderlich.
- Alle Eingaben werden validiert, um Fehler zu vermeiden.


## Verwendete Module 
- random 
  → Wird verwendet, um ein zufälliges Wort aus der Wortliste auszuwählen.
- ANSI-Farbcodes  
  → Werden verwendet, um Buchstaben-Eingaben und Spielergebnisse farblich hervorzuheben.


## Projektstruktur 
```
project/ 
│ 
├── main.py             # Einstiegspunkt und Hauptmenü 
├── game_logic.py       # Spiellogik 
├── gallows.py          # ASCII-Galgen 
├── wordlist.py         # Wortlisten & Zufallsauswahl 
├── README.md           # Projektdokumentation 
├── TESTCASES.md        # Testfälle 
├── flowchart.pdf       # Programmablaufdiagramm
```

## Programmstart 
Das Programm wird über die Datei `main.py` gestartet:

```bash
python main.py
```

## Beispielhafte Nutzung 
```text
-----------------Hangman------------------ 
Geben Sie '1' ein, um das Spiel zu starten 
Geben Sie '2' ein, um das Spiel zu beenden

Auswahl: 1

Geben Sie die Schwierigkeit ein (leicht, mittel oder schwer): leicht

Wort: _ _ _ _

Raten Sie einen Buchstaben: i

           -----
           |   |
               |
               |
               |
               |
        =========
        
Bisher geratene Buchstaben: i

Richtig!

Wort: _ i _ _

Raten Sie einen Buchstaben: o

           -----
           |   |
           O   |
               |
               |
               |
        =========
        
Bisher geratene Buchstaben: i o
Falsch! 
Dieser Buchstabe (o) ist nicht im Wort.

Wort: _ i _ _

Raten Sie einen Buchstaben: f

           -----
           |   |
           O   |
               |
               |
               |
        =========
        
Bisher geratene Buchstaben: f i o

Richtig!

Wort: f i _ _

Raten Sie einen Buchstaben: l

           -----
           |   |
           O   |
               |
               |
               |
        =========
        
Bisher geratene Buchstaben: f i l o

Richtig!

Wort: f i l _

Raten Sie einen Buchstaben: e

           -----
           |   |
           O   |
               |
               |
               |
        =========
        
Bisher geratene Buchstaben: e f i l o

Richtig!

Gewonnen! 🥳

Das Wort war: file
```