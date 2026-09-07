import random

from pages.Faith.suspects import SUSPECTS
from pages.Gladys.clues import get_case_clues
from pages.Iman.investigation import Investigation


RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"


class Game:
    def _init_(self, investigation=None):
        self.case = investigation or self.new_case()

    def new_case(self):
        killer = random.choice(SUSPECTS).name
        return Investigation(killer, get_case_clues(killer))

    def intro(self):
        print(RED + """
╔══════════════════════════════════════════════╗
║                                              ║
║             THE MIDNIGHT MURDER             ║
║                 CASE #1147                  ║
║                                              ║
╚══════════════════════════════════════════════╝
""" + RESET)

        print("""
              ☠️  THE CASE BEGINS  ☠️

                    █████████
                  ███       ███
                ██     X X     ██
               ██      _      ██
               ██     /   \\     ██
                ██    \\_/    ██
                  ███       ███
                    █████████
                        ||
                   __||__
                  /     ||     \\
                 /      ||      \\
                /       ||       \\
               ☠️        ||        ☠️

Hassan, owner of the Midnight Hotel, has been
found dead inside his private office.

TIME OF DEATH : 11:47 PM
CAUSE OF DEATH : POISON
LOCATION       : HOTEL OFFICE

The murder happened during the hotel's
annual Gala Night.

Four people had a reason to want Hassan gone.

And every one of them is hiding something...
""")

        print(CYAN + "THE SUSPECTS" + RESET)

        for suspect in SUSPECTS:
            print(f"  • {suspect.name:<8} — {suspect.occupation}")

        print(YELLOW + """
──────────────────────────────────────────────
The murderer is different in every investigation.
Trust nobody. Follow the clues.
──────────────────────────────────────────────
""" + RESET)

    def menu(self):
        while True:
            print(CYAN + """
╔══════════════════════════════════════════════╗
║              INVESTIGATION MENU              ║
╚══════════════════════════════════════════════╝
""" + RESET)

            print("  [1] Interview a suspect")
            print("  [2] Search a location")
            print("  [3] View discovered clues")
            print("  [4] Make an accusation")
            print("  [5] Save investigation")
            print("  [6] Exit")

            choice = input(YELLOW + "\nChoose: " + RESET).strip()

            if choice == "1":
                self.interview()

            elif choice == "2":
                self.search()

            elif choice == "3":
                self.case.show_clues()

            elif choice == "4":
                if self.accuse():
                    break

            elif choice == "5":
                self.case.save()

            elif choice == "6":
                print(GREEN + "\nInvestigation closed. Goodbye." + RESET)
                break

            else:
                print(RED + "\nInvalid choice. Please choose 1-6." + RESET)

    def interview(self):
        print(CYAN + "\n--- SUSPECTS ---" + RESET)

        for i, suspect in enumerate(SUSPECTS, 1):
            print(f"{i}. {suspect.name}")

        choice = input(YELLOW + "Choose suspect: " + RESET).strip()

        if choice in ["1", "2", "3", "4"]:
            self.case.interview(SUSPECTS[int(choice) - 1])
        else:
            print(RED + "Invalid suspect." + RESET)

    def search(self):
        locations = ["Lobby", "Kitchen", "Office", "Garden"]

        print(CYAN + "\n--- LOCATIONS ---" + RESET)

        for i, location in enumerate(locations, 1):
            print(f"{i}. {location}")

        choice = input(YELLOW + "Choose location: " + RESET).strip()

        if choice in ["1", "2", "3", "4"]:
            self.case.search(locations[int(choice) - 1])
        else:
            print(RED + "Invalid location." + RESET)

    def accuse(self):
        print(RED + "\n--- MAKE YOUR ACCUSATION ---" + RESET)

        for i, suspect in enumerate(SUSPECTS, 1):
            print(f"{i}. {suspect.name}")

        choice = input(YELLOW + "Who is the murderer? " + RESET).strip()

        if choice in ["1", "2", "3", "4"]:
            return self.case.accuse(
                SUSPECTS[int(choice) - 1].name
            )

        print(RED + "Invalid suspect." + RESET)
        return False