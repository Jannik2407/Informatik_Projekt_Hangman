import random       # für zufällige Auswahl von Wörtern

words = {
    "leicht": [ # 4 Buchstaben oder weniger
        "code", "byte", "bits", "node", "link", "file", "data", "loop"
    ],
    "mittel": [ # 5-6 Buchstaben
        "array", "cache", "login", "query", "proxy", "debug", "python", "server", "script", "binary", "thread", "object"
    ],
    "schwer": [ # 7 oder mehr Buchstaben
        "hangman", "compiler", "algorithm", "informatik", "programmieren"
    ]
}

def get_random_word_by_difficulty(difficulty):
    # Gibt ein zufälliges Wort basierend auf der gewählten Schwierigkeit zurück
    if difficulty not in words:
        return None # Ungültige Eingabe
    
    return random.choice(words[difficulty])