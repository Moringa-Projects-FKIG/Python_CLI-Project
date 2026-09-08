import json

from models.Kennedy.game import Game
from models.Iman.investigation import Investigation


RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"


print(RED + r"""
    ███╗   ███╗██╗██████╗ ███╗   ██╗██╗ ██████╗ ██╗  ██╗████████╗
    ████╗ ████║██║██╔══██╗████╗  ██║██║██╔════╝ ██║  ██║╚══██╔══╝
    ██╔████╔██║██║██║  ██║██╔██╗ ██║██║██║  ███╗███████║   ██║
    ██║╚██╔╝██║██║██║  ██║██║╚██╗██║██║██║   ██║██╔══██║   ██║
    ██║ ╚═╝ ██║██║██████╔╝██║ ╚████║██║╚██████╔╝██║  ██║   ██║
    ╚═╝     ╚═╝╚═╝╚═════╝ ╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝

                       M U R D E R
""" + RESET)

print(CYAN + """
╔══════════════════════════════════════════════╗
║              A HOTEL. A MURDER.             ║
║                FOUR SUSPECTS.               ║
╚══════════════════════════════════════════════╝
""" + RESET)

print("  [1] New Investigation")
print("  [2] Load Saved Investigation")
print("  [3] Exit")

choice = input(YELLOW + "\nChoose: " + RESET).strip()

if choice == "1":
    game = Game()
    game.intro()
    game.menu()

elif choice == "2":
    try:
        game = Game(Investigation.load())
        print(GREEN + "\nSaved investigation loaded." + RESET)
        game.menu()
    except (FileNotFoundError, json.JSONDecodeError, KeyError, TypeError):
        print(RED + "\nNo saved investigation found." + RESET)

elif choice == "3":
    print(GREEN + "\nGoodbye, Detective." + RESET)

else:
    print(RED + "\nInvalid choice. Please restart the game." + RESET)