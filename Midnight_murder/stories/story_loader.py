import json
from pathlib import Path


STORY_ROOT = Path(__file__).parents[1] / "data" / "stories"


def _read_json(path):
	try:
		with path.open() as file:
			return json.load(file)
	except (FileNotFoundError, json.JSONDecodeError, OSError):
		return None


def _values(data, keys):
	if isinstance(data, dict):
		for key in keys:
			if isinstance(data.get(key), list):
				data = data[key]
				break
	if not isinstance(data, list):
		return []
	values = []
	for item in data:
		if isinstance(item, str) and item.strip():
			values.append(item.strip())
		elif isinstance(item, dict):
			for key in keys:
				value = item.get(key)
				if value:
					values.append(value)
					break
	return values


def load_story_sources():
	sources = []
	if not STORY_ROOT.exists():
		return sources
	for folder in STORY_ROOT.iterdir():
		if not folder.is_dir():
			continue
		story = _read_json(folder / "story.json") or {}
		locations = _values(_read_json(folder / "locations.json"), ["name", "location"])
		clues = _values(_read_json(folder / "clues.json"), ["clue", "description", "text"])
		suspects = []
		for item in _read_json(folder / "suspects.json") or []:
			if isinstance(item, str):
				suspects.append((item, "has a possible motive"))
			elif isinstance(item, dict) and item.get("name"):
				suspects.append((item["name"], item.get("motive", "has a possible motive")))
		if story and locations and len(suspects) >= 4 and len(clues) >= 5:
			sources.append({"folder": folder.name, "story": story, "locations": locations,
							"suspects": suspects, "clues": clues})
	return sources
