# Midnight Murder

Midnight Murder is a terminal detective game built with Python and Rich.

## Run the game

From the repository root:

```bash
source .venv-1/bin/activate
python Midnight_murder/main.py
```

Choose **New Game** to generate a case or **Load Game** to continue the saved case.

## Project layout

- `main.py` starts the application.
- `game/` runs the case session and investigation actions.
- `stories/` loads story data and generates randomized cases.
- `storage/` saves and loads player progress.
- `ui/` renders the Rich terminal interface.
- `models/` contains the domain model package.
- `data/stories/` contains reusable story templates.
- `data/saves/` contains runtime save files.
- `tests/` contains automated tests.

## Install dependencies

```bash
python -m pip install -r Midnight_murder/requirements.txt
```
