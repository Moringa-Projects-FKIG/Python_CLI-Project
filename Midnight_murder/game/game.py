try:
	from Midnight_murder.game.investigation import accuse, investigate
	from Midnight_murder.stories.generator import generate_case
	from Midnight_murder.storage.save_manager import load_game, save_game
	from Midnight_murder.ui import display
except ModuleNotFoundError:
	from game.investigation import accuse, investigate
	from stories.generator import generate_case
	from storage.save_manager import load_game, save_game
	from ui import display


def play_case(case):
	old_name = case.get("player_name", "").strip()
	entered_name = display.ask_name(old_name)
	case["player_name"] = entered_name or old_name or "Detective"
	display.message(f"Welcome, Detective {case['player_name']}.", "bold white")
	display.show_case(case)
	options = ("Investigate location", "Review clues", "Review suspects",
			   "Accuse a suspect", "Save game", "Return to main menu")
	while True:
		choice = display.choose("Case Menu", options, case["location"])
		if choice == "1":
			investigate(case)
		elif choice == "2":
			display.show_clues(case["found_clues"], case["location"]) if case["found_clues"] else display.message("You have not discovered any clues yet.", "yellow")
		elif choice == "3":
			display.show_suspects(case["suspects"], case["location"])
		elif choice == "4" and accuse(case):
			save_game(case)
			return
		elif choice == "5":
			save_game(case)
			display.message("Game saved.", "bold green")
		elif choice == "6":
			return
		else:
			display.message("Please choose a number from the menu.", "yellow")


def run_game():
	while True:
		choice = display.choose("Welcome to Midnight Murder", ("New Game", "Load Game", "Game Rules", "Exit Game"))
		if choice == "1":
			play_case(generate_case())
		elif choice == "2":
			case = load_game()
			if case:
				play_case(case)
			else:
				display.message("No valid saved game found.", "yellow")
		elif choice == "3":
			display.show_rules()
		elif choice == "4":
			display.message("Goodbye, Detective.", "bold white")
			return
		else:
			display.message("Please choose a number from the menu.", "yellow")
