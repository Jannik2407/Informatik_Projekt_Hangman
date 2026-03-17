import random       # für zufällige Auswahl von Wörtern

words = [
    "hangman",
    "python",
    "informatik",
    "programmieren",
    "code"
]


def get_random_word_by_difficulty(difficulty):
    # Wörter nach Schwierigkeit sortieren: schwer (0-4), mittel (5-6), leicht (7-)
    if difficulty == "leicht":
       word_list = [word for word in words if len(word) <= 4]  # Einfache Wörter
    elif difficulty == "mittel":
        word_list = [word for word in words if 5 <= len(word) <= 6]  # Mittelschwere Wörter
    elif difficulty == "schwer":
        word_list = [word for word in words if len(word) >= 7]  # Schwere Wörter
    else:
        return None # Ungültige Eingabe 
    
    if not word_list:
        return None # Keine Wörter für diese Schwierigkeit gefunden
    
    return random.choice(word_list)