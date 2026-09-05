from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text


console = Console()

SCENE_STYLES = {
	"hotel": ("#d6b36a", "midnight blue"),
	"garden": ("#9bc27a", "dark_green"),
	"train": ("#9aa7b8", "grey15"),
	"museum": ("#c58b65", "grey11"),
	"theatre": ("#d49ab6", "grey13"),
}


def scene_style(location=""):
	location = location.lower()
	for word, style in SCENE_STYLES.items():
		if word in location:
			return style
	return "#b9a7d0", "grey15"


def heading(title, location=""):
	accent, background = scene_style(location)
	console.print(Panel(
		Text(title, justify="center", style=f"bold {accent}"),
		border_style=accent,
		style=f"on {background}",
		padding=(0, 2),
	))


def choose(title, options, location=""):
	heading(title, location)
	table = Table(show_header=False, box=None, padding=(0, 1))
	table.add_column(style="bold white", width=4)
	table.add_column(style="white")
	for number, option in enumerate(options, 1):
		table.add_row(f"{number}.", option)
	console.print(table)
	return console.input("[bold]Choose an option:[/] ").strip()


def message(text, style="white"):
	console.print(text, style=style)


def show_case(case):
	accent, background = scene_style(case["location"])
	details = Text()
	details.append(f"{case['victim']}\n", style="bold white")
	details.append(f"{case['victim_description']}\n\n", style="italic white")
	details.append(f"Scene: {case['location']}\n", style=accent)
	details.append(f"Apparent method: {case['method']}", style="white")
	console.print(Panel(
		details,
		title=case["title"],
		title_align="left",
		border_style=accent,
		style=f"on {background}",
		padding=(1, 2),
	))


def show_clues(clues, location=""):
	heading("Clues Found", location)
	for clue in clues:
		console.print(f"[bold green]•[/] {clue}")


def show_suspects(suspects, location="", numbered=False):
	heading("Suspects", location)
	for number, suspect in enumerate(suspects, 1):
		prefix = f"{number}." if numbered else "•"
		console.print(f"[bold yellow]{prefix}[/] {suspect['name']}", end="")
		if not numbered:
			console.print(f": {suspect['motive']}")
		else:
			console.print()


def ask_name(old_name=""):
	prompt = "Detective, what is your name?"
	if old_name:
		prompt += f" (Enter keeps {old_name})"
	return console.input(f"[bold]{prompt}[/] ").strip()


def show_rules():
	heading("Game Rules")
	console.print("Investigate locations to discover clues.")
	console.print("Review the clues and suspects before making an accusation.")
	console.print("Every new game creates a different case.")
	console.input("\nPress Enter to continue...")
