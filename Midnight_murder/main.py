import json
from pathlib import Path
import random

SAVE_FILE = Path(__file__).parent / "data" / "saves" / "player_save.json"
STORY_ROOT = Path(__file__).parent / "stories"

LOCATION_POOL = [
    "the abandoned theatre", "the candlelit manor", "the winter train",
    "the seaside hotel", "the garden party", "the city museum",
]
VICTIM_POOL = [
    ("Lord Edmund Vale", "wealthy owner of the estate"),
    ("Dr. Miriam Bell", "famous forensic researcher"),
    ("Arthur Finch", "retired detective"),
    ("Clara Nightingale", "celebrated stage performer"),
    ("Victor Hart", "collector of rare antiques"),
    ("Evelyn March", "powerful newspaper publisher"),
]
SUSPECT_POOL = [
    ("the jealous business partner", "wanted control of the victim's fortune"),
    ("the estranged sibling", "had been cut out of the victim's will"),
    ("the loyal housekeeper", "was protecting a dangerous secret"),
    ("the ambitious assistant", "feared the victim would expose their fraud"),
    ("the mysterious guest", "had arrived with a false identity"),
    ("the old family friend", "was seeking revenge for a past betrayal"),
]
METHOD_POOL = [
    "a rare poison hidden in a glass of wine", "a concealed blade found near the scene",
    "a tampered medication bottle", "a fall caused by a loosened balcony rail",
    "a smothering pillow from the guest room",
]
CLUE_POOL = [
    "a torn piece of a black glove", "muddy footprints leading away from the scene",
    "a threatening letter with no signature", "a stopped pocket watch showing the time of death",
    "a silver button caught on the victim's coat", "a half-burned photograph",
    "a hidden key marked with the letter M", "a glass with an unfamiliar lipstick mark",
]


def read_json_file(file_path):
    if not file_path.exists() or file_path.stat().st_size == 0:
        return None
    try:
        with file_path.open() as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return None


def first_value(data, keys, default=""):
    if isinstance(data, dict):
        for key in keys:
            value = data.get(key)
            if value:
                return value
    return default


def text_values(data, keys):
    if isinstance(data, dict):
        data = first_value(data, keys, [])
    if not isinstance(data, list):
        return []

    values = []
    for item in data:
        if isinstance(item, str) and item.strip():
            values.append(item.strip())
        elif isinstance(item, dict):
            value = first_value(item, keys)
            if value:
                values.append(value)
    return values


def load_story_sources():
    sources = []
    for story_folder in STORY_ROOT.iterdir():
        if not story_folder.is_dir() or story_folder.name == "generated_stories":
            continue

        story_data = read_json_file(story_folder / "story.json")
        if story_data is None:
            story_data = read_json_file(story_folder / "stroy.json")
        locations_data = read_json_file(story_folder / "locations.json")
        suspects_data = read_json_file(story_folder / "suspects.json")
        clues_data = read_json_file(story_folder / "clues.json")

        locations = text_values(locations_data, ["name", "location", "title", "text"])
        clues = text_values(clues_data, ["clue", "description", "text", "name"])
        suspects = []
        suspect_items = suspects_data if isinstance(suspects_data, list) else []
        for item in suspect_items:
            if isinstance(item, str):
                suspects.append((item, "has a possible motive"))
            elif isinstance(item, dict):
                suspect_name = first_value(item, ["name", "suspect", "person"])
                motive = first_value(item, ["motive", "description", "reason"], "has a possible motive")
                if suspect_name:
                    suspects.append((suspect_name, motive))

        if story_data or locations or suspects or clues:
            sources.append({
                "folder": story_folder.name,
                "story": story_data or {},
                "locations": locations,
                "suspects": suspects,
                "clues": clues,
            })
    return sources


def generate_case():
    story_sources = load_story_sources()
    source = random.choice(story_sources) if story_sources else None
    story = source["story"] if source else {}
    locations = source["locations"] if source and source["locations"] else LOCATION_POOL
    suspect_pool = source["suspects"] if source and len(source["suspects"]) >= 4 else SUSPECT_POOL
    clues = source["clues"] if source and len(source["clues"]) >= 5 else CLUE_POOL

    location = random.choice(locations)
    fallback_victim, fallback_description = random.choice(VICTIM_POOL)
    victim_name = first_value(
        story,
        ["victim", "victim_name", "murder_victim"],
        fallback_victim,
    )
    victim_description = first_value(
        story,
        ["victim_description", "description"],
        fallback_description,
    )
    if isinstance(victim_name, dict):
        victim_description = first_value(victim_name, ["description", "role"], victim_description)
        victim_name = first_value(victim_name, ["name", "victim"], fallback_victim)
    suspects = random.sample(suspect_pool, 4)
    culprit_index = random.randrange(4)
    return {
        "title": first_value(story, ["title", "name"], f"The Mystery at {location.title()}"),
        "location": location,
        "victim": victim_name,
        "victim_description": victim_description,
        "method": first_value(story, ["method", "murder_method", "weapon"], random.choice(METHOD_POOL)),
        "suspects": [
            {"name": name, "motive": motive, "culprit": index == culprit_index}
            for index, (name, motive) in enumerate(suspects)
        ],
        "clues": random.sample(clues, 5),
        "found_clues": [],
        "player_name": "",
        "story_source": source["folder"] if source else "built-in fallback",
    }


def save_game(case):
    SAVE_FILE.parent.mkdir(parents=True, exist_ok=True)
    with SAVE_FILE.open("w") as file:
        json.dump(case, file, indent=4)
    print("Game saved.")


def load_game():
    if not SAVE_FILE.exists():
        print("No saved game found.")
        return None

    try:
        with SAVE_FILE.open() as file:
            case = json.load(file)
    except (json.JSONDecodeError, OSError):
        print("The save file could not be read.")
        return None

    required_keys = {
        "title", "location", "victim", "victim_description", "method",
        "suspects", "clues", "found_clues", "player_name",
    }
    if not isinstance(case, dict) or not required_keys.issubset(case):
        print("This save file is from an older or invalid game version.")
        return None
    if not isinstance(case["suspects"], list) or not isinstance(case["clues"], list):
        print("This save file is invalid.")
        return None
    return case


def show_case(case):
    print(f"\n{case['title']}")
    print(f"{case['victim']} ({case['victim_description']}) was found dead at {case['location']}.")
    print(f"The apparent method was {case['method']}.")


def investigate(case):
    remaining_clues = [clue for clue in case["clues"] if clue not in case["found_clues"]]
    if not remaining_clues:
        print("You have searched every useful part of the scene.")
        return

    clue = random.choice(remaining_clues)
    case["found_clues"].append(clue)
    print(f"You investigate {case['location']} and discover {clue}.")
    print(f"Clues discovered: {len(case['found_clues'])}/{len(case['clues'])}")


def accuse(case):
    print("\nSuspects:")
    for number, suspect in enumerate(case["suspects"], start=1):
        print(f"{number}. {suspect['name']}")

    choice = input("Who do you accuse? Enter a number, or press Enter to cancel: ").strip()
    if not choice:
        return False
    if not choice.isdigit() or not 1 <= int(choice) <= len(case["suspects"]):
        print("That is not a valid suspect.")
        return False

    suspect = case["suspects"][int(choice) - 1]
    if suspect["culprit"]:
        print(f"Correct! {suspect['name']} committed the murder.")
        print("The case is solved.")
    else:
        print(f"You accused {suspect['name']}, but the evidence does not support it.")
        print("The case remains unsolved. Keep investigating or try again.")
    return suspect["culprit"]


def play_case(case):
    if not case["player_name"]:
        case["player_name"] = input("Detective, what is your name? ").strip() or "Detective"

    print(f"\nWelcome, Detective {case['player_name']}.")
    show_case(case)

    while True:
        print("1. Investigate location")
        print("2. Review clues")
        print("3. Review suspects")
        print("4. Accuse a suspect")
        print("5. Save game")
        print("6. Return to main menu")
        choice = input("Choose an option and press Enter: ").strip()

        if choice == "1":
            investigate(case)
        elif choice == "2":
            if case["found_clues"]:
                print("\nClues found:")
                for clue in case["found_clues"]:
                    print(f"- {clue}")
            else:
                print("You have not discovered any clues yet.")
        elif choice == "3":
            print("\nSuspects:")
            for suspect in case["suspects"]:
                print(f"- {suspect['name']}: {suspect['motive']}")
        elif choice == "4":
            if accuse(case):
                save_game(case)
                return
        elif choice == "5":
            save_game(case)
        elif choice == "6":
            return
        else:
            print("Please choose a number from the menu.")


def print_rules():
    print("\nGame rules:")
    print("Investigate locations to discover clues.")
    print("Review the clues and suspects before making an accusation.")
    print("Every new game creates a different victim, location, method, suspects, and clues.")
    input("Press Enter to continue...")


def main():
    while True:
        print("\nWelcome to Midnight Murder!")
        print("1. New Game")
        print("2. Load Game")
        print("3. Game Rules")
        print("4. Exit Game")
        choice = input("What would you like to do? ").strip()

        if choice == "1":
            play_case(generate_case())
        elif choice == "2":
            case = load_game()
            if case is not None:
                play_case(case)
        elif choice == "3":
            print_rules()
        elif choice == "4":
            print("Goodbye, Detective.")
            break
        else:
            print("Please choose a number from the menu.")


if __name__ == "__main__":
    main()
            