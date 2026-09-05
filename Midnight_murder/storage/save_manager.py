import json
from pathlib import Path


SAVE_FILE = Path(__file__).parents[1] / "data" / "saves" / "player_save.json"
REQUIRED_KEYS = {
    "title", "location", "victim", "victim_description", "method",
    "suspects", "clues", "found_clues", "player_name",
}


def save_game(case):
    SAVE_FILE.parent.mkdir(parents=True, exist_ok=True)
    with SAVE_FILE.open("w") as file:
        json.dump(case, file, indent=4)


def load_game():
    if not SAVE_FILE.exists():
        return None
    try:
        with SAVE_FILE.open() as file:
            case = json.load(file)
    except (json.JSONDecodeError, OSError):
        return None
    if not isinstance(case, dict) or not REQUIRED_KEYS.issubset(case):
        return None
    if not isinstance(case["suspects"], list) or not isinstance(case["clues"], list):
        return None
    return case
