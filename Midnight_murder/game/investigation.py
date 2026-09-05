import random

try:
	from Midnight_murder.ui import display
except ModuleNotFoundError:
	from ui import display


def investigate(case):
	remaining = [clue for clue in case["clues"] if clue not in case["found_clues"]]
	if not remaining:
		display.message("You have searched every useful part of the scene.", "yellow")
		return
	clue = random.choice(remaining)
	case["found_clues"].append(clue)
	display.message(f"You investigate {case['location']} and discover {clue}.", "green")
	display.message(f"Clues discovered: {len(case['found_clues'])}/{len(case['clues'])}", "bold green")


def accuse(case):
	display.show_suspects(case["suspects"], case["location"], numbered=True)
	choice = display.console.input("[bold]Who do you accuse? Press Enter to cancel:[/] ").strip()
	if not choice.isdigit() or not 1 <= int(choice) <= len(case["suspects"]):
		display.message("Please enter a valid suspect number.", "yellow")
		return False
	suspect = case["suspects"][int(choice) - 1]
	if suspect["culprit"]:
		display.message(f"Correct! {suspect['name']} committed the murder.", "bold green")
		display.message("The case is solved.", "bold green")
		return True
	display.message(f"You accused {suspect['name']}, but the evidence does not support it.", "yellow")
	return False
