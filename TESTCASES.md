# Testcases Hangman-Spiel

## TESTCASES.md
Dieses Dokument zeigt Testfälle für das Hangman-Spiel.
Jeder Test enthält: Eingaben (Input), erwartetes Ergebnis (Expected Output) und tatsächliches Ergebnis (Actual Output).

## Testfälle Hauptmenü:

### Testfall 1: Spiel starten (Auswahl '1')

**Input:**
```text
1
```

**Expected Output:**
```text
-----------------Hangman------------------
Geben Sie '1' ein, um das Spiel zu starten
Geben Sie '2' ein, um das Spiel zu beenden
Auswahl: 1
Geben Sie die Schwierigkeit ein (leicht, mittel oder schwer): 
```

**Actual Output:**
```text
-----------------Hangman------------------
Geben Sie '1' ein, um das Spiel zu starten
Geben Sie '2' ein, um das Spiel zu beenden
Auswahl: 1
Geben Sie die Schwierigkeit ein (leicht, mittel oder schwer): 
```

---

### Testfall 2: Programm beenden (Auswahl: '2')

**Input:**
```text
2
```

**Expected Output:**
```text
-----------------Hangman------------------
Geben Sie '1' ein, um das Spiel zu starten
Geben Sie '2' ein, um das Spiel zu beenden
Auswahl: 2
Programm beendet.
```

**Actual Output:**
```text
-----------------Hangman------------------
Geben Sie '1' ein, um das Spiel zu starten
Geben Sie '2' ein, um das Spiel zu beenden
Auswahl: 2
Programm beendet.
```

---

### Testfall 3: Ungültige Eingabe

**Input:**
```text
x
```

**Expected Output:**
```text
-----------------Hangman------------------
Geben Sie '1' ein, um das Spiel zu starten
Geben Sie '2' ein, um das Spiel zu beenden
Auswahl: x
Ungültige Eingabe! Bitte geben Sie '1' um das Spiel zu starten oder '2' um das Spiel zu beenden.

-----------------Hangman------------------
Geben Sie '1' ein, um das Spiel zu starten
Geben Sie '2' ein, um das Spiel zu beenden
Auswahl: 
```

**Actual Output:**
```text
-----------------Hangman------------------
Geben Sie '1' ein, um das Spiel zu starten
Geben Sie '2' ein, um das Spiel zu beenden
Auswahl: x
Ungültige Eingabe! Bitte geben Sie '1' um das Spiel zu starten oder '2' um das Spiel zu beenden.

-----------------Hangman------------------
Geben Sie '1' ein, um das Spiel zu starten
Geben Sie '2' ein, um das Spiel zu beenden
Auswahl: 
```

## Testfälle Spiel:

### Testfall 4: Richtiger Buchstabe 

**Input:**
```text
o
```

**Expected Output:**
```text
Raten Sie einen Buchstaben: o

           -----
           |   |
               |
               |
               |
               |
        =========
        
Bisher geratene Buchstaben: o

Richtig!

Wort: _ o _ _

Raten Sie einen Buchstaben: 
```

**Actual Output:**
```text
Raten Sie einen Buchstaben: o

           -----
           |   |
               |
               |
               |
               |
        =========
        
Bisher geratene Buchstaben: o

Richtig!

Wort: _ o _ _

Raten Sie einen Buchstaben: 
```

---

### Testfall 5: Falscher Buchstabe 

**Input:**
```text
a
```

**Expected Output:**
```text
Raten Sie einen Buchstaben: a

           -----
           |   |
           O   |
               |
               |
               |
        =========
        
Bisher geratene Buchstaben: a
Falsch! 
Dieser Buchstabe (a) ist nicht im Wort.

Wort: _ _ _ _

Raten Sie einen Buchstaben: 
```

**Actual Output:**
```text
Raten Sie einen Buchstaben: a

           -----
           |   |
           O   |
               |
               |
               |
        =========
        
Bisher geratene Buchstaben: a
Falsch! 
Dieser Buchstabe (a) ist nicht im Wort.

Wort: _ _ _ _

Raten Sie einen Buchstaben: 
```
