import random

try:
	from Midnight_murder.stories.story_loader import load_story_sources
except ModuleNotFoundError:
	from stories.story_loader import load_story_sources


LOCATIONS = ["the abandoned theatre", "the candlelit manor", "the winter train",
			 "the seaside hotel", "the garden party", "the city museum"]
VICTIMS = [("Lord Edmund Vale", "wealthy owner of the estate"),
		   ("Dr. Miriam Bell", "famous forensic researcher"),
		   ("Clara Nightingale", "celebrated stage performer")]
METHODS = ["a rare poison hidden in a glass of wine", "a concealed blade near the scene",
		   "a tampered medication bottle", "a loosened balcony rail"]
SUSPECTS = [("the jealous business partner", "wanted control of the victim's fortune"),
			("the estranged sibling", "had been cut out of the victim's will"),
			("the loyal housekeeper", "was protecting a dangerous secret"),
			("the mysterious guest", "had arrived with a false identity")]
CLUES = ["a torn piece of a black glove", "muddy footprints leading away from the scene",
		 "a threatening letter with no signature", "a stopped pocket watch showing the time of death",
		 "a silver button caught on the victim's coat"]


def generate_case():
	sources = load_story_sources()
	source = random.choice(sources) if sources else None
	story = source["story"] if source else {}
	locations = source["locations"] if source else LOCATIONS
	suspects = source["suspects"] if source else SUSPECTS
	clues = source["clues"] if source else CLUES
	location = random.choice(locations)
	victim_name, victim_description = random.choice(VICTIMS)
	victim = story.get("victim", victim_name)
	if isinstance(victim, dict):
		victim_description = victim.get("description", victim_description)
		victim = victim.get("name", victim_name)
	selected_suspects = random.sample(suspects, 4)
	culprit = random.randrange(4)
	return {
		"title": story.get("title", f"The Mystery at {location.title()}"),
		"location": location,
		"victim": victim,
		"victim_description": story.get("victim_description", victim_description),
		"method": story.get("method", random.choice(METHODS)),
		"suspects": [{"name": name, "motive": motive, "culprit": index == culprit}
					 for index, (name, motive) in enumerate(selected_suspects)],
		"clues": random.sample(clues, 5),
		"found_clues": [],
		"player_name": "",
		"story_source": source["folder"] if source else "built-in fallback",
	}
