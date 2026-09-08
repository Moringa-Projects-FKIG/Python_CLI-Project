import json
from pathlib import Path


SAVE_FILE = Path(__file__).resolve().parents[2] / "data" / "saved_game.json"


class Investigation:
    def __init__(self, killer, clues):
        self.killer = killer
        self.clues = clues
        self.found = []
        self.interviewed = []

    def interview(self, suspect):
        if suspect.name not in self.interviewed:
            self.interviewed.append(suspect.name)

        print()
        print(f"--- {suspect.name} ---")
        print(f"Occupation: {suspect.occupation}")
        print(f"Motive: {suspect.motive}")
        print(f"Clothing: {suspect.clothing}")
        print(f"Alibi: {suspect.alibi}")
        print(f"Secret: {suspect.secret}")

    def search(self, location):
        print()
        print(f"--- Searching the {location} ---")

        clue = self.clues[location]
        print(f"- {clue}")

        if clue not in self.found:
            self.found.append(clue)

    def show_clues(self):
        print()
        print("--- CLUES FOUND ---")

        if not self.found:
            print("You have not found any clues yet.")
        else:
            for clue in self.found:
                print(f"- {clue}")

    def accuse(self, suspect):
        print()

        if suspect == self.killer:
            print(f"Correct. {suspect} is the murderer.")
            return True

        print(f"Wrong accusation. {suspect} is innocent.")
        print(f"The murderer was {self.killer}.")
        return False

    def save(self):
        data = {
            "killer": self.killer,
            "clues": self.clues,
            "found": self.found,
            "interviewed": self.interviewed
        }

        with SAVE_FILE.open("w") as file:
            json.dump(data, file, indent=4)

        print()
        print("Investigation saved successfully.")

    @classmethod
    def load(cls):
        with SAVE_FILE.open("r") as file:
            data = json.load(file)

        game = cls(data["killer"], data["clues"])
        game.found = data["found"]
        game.interviewed = data["interviewed"]

        return game