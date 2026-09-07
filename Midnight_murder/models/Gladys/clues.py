CLUES = {
    "Lance": {
        "Lobby": "Camera footage shows Lance leaving the kitchen shortly before 11:47 PM.",
        "Kitchen": "A small poison bottle is missing from the kitchen cabinet.",
        "Office": "A cup containing traces of poison was found beside Hassan's desk.",
        "Garden": "A torn piece of white chef's jacket was found near the garden door."
    },

    "Chris": {
        "Lobby": "Camera footage shows Chris walking toward the office at 11:42 PM.",
        "Kitchen": "A poisoned drink ingredient was found near the serving area.",
        "Office": "A letter shows Chris owed Hassan a large amount of money.",
        "Garden": "A piece of silver tie fabric was found near the garden path."
    },

    "Melody": {
        "Lobby": "Camera footage shows Melody entering the office corridor shortly before 11:47 PM.",
        "Kitchen": "A poisoned cup was prepared using a drink served at the gala.",
        "Office": "A threatening note warns Hassan to stop investigating a family secret.",
        "Garden": "A torn piece of black blazer fabric was found near the garden door."
    },

    "Michael": {
        "Lobby": "Security records show Michael used his hotel access key near the office.",
        "Kitchen": "A poison container was found hidden inside a hotel supply box.",
        "Office": "A financial ledger shows missing hotel money.",
        "Garden": "A torn piece of hotel uniform was found near the garden."
    }
}


def get_case_clues(killer):
    return CLUES[killer]