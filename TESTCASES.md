# Testcases Hangman-Spiel

## TESTCASES.md
Dieses Dokument zeigt Testfälle für das Hangman-Spiel.
Jeder Test enthält: Eingaben (Input), erwartetes Ergebnis (Expected Output) und tatsächliches Ergebnis (Actual Output).

## Testfälle Hauptmenü:

### Testfall 1: Spiel starten (Auswahl '1')

**Input:**
1

**Expected Output:**
-----------------Hangman------------------
Geben Sie '1' ein, um das Spiel zu starten
Geben Sie '2' ein, um das Spiel zu beenden
Auswahl: 1
Geben Sie die Schwierigkeit ein (leicht, mittel oder schwer): 

**Actual Output:**
-----------------Hangman------------------
Geben Sie '1' ein, um das Spiel zu starten
Geben Sie '2' ein, um das Spiel zu beenden
Auswahl: 1
Geben Sie die Schwierigkeit ein (leicht, mittel oder schwer): 

---

### Testfall 2: Programm beenden (Auswahl: '2')

**Input:**
2

**Expected Output:**
-----------------Hangman------------------
Geben Sie '1' ein, um das Spiel zu starten
Geben Sie '2' ein, um das Spiel zu beenden
Auswahl: 2
Programm beendet.

**Actual Output:**
-----------------Hangman------------------
Geben Sie '1' ein, um das Spiel zu starten
Geben Sie '2' ein, um das Spiel zu beenden
Auswahl: 2
Programm beendet.

---

### Testfall 3: Ungültige Eingabe

**Input:**
x

**Expected Output:**
-----------------Hangman------------------
Geben Sie '1' ein, um das Spiel zu starten
Geben Sie '2' ein, um das Spiel zu beenden
Auswahl: x
Ungültige Eingabe! Bitte geben Sie '1' um das Spiel zu starten oder '2' um das Spiel zu beenden.

-----------------Hangman------------------
Geben Sie '1' ein, um das Spiel zu starten
Geben Sie '2' ein, um das Spiel zu beenden
Auswahl: 

**Actual Output:**
-----------------Hangman------------------
Geben Sie '1' ein, um das Spiel zu starten
Geben Sie '2' ein, um das Spiel zu beenden
Auswahl: x
Ungültige Eingabe! Bitte geben Sie '1' um das Spiel zu starten oder '2' um das Spiel zu beenden.

-----------------Hangman------------------
Geben Sie '1' ein, um das Spiel zu starten
Geben Sie '2' ein, um das Spiel zu beenden
Auswahl: 


