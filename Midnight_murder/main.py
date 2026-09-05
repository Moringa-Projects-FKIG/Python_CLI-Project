try:
    from Midnight_murder.game.game import run_game
except ModuleNotFoundError:
    from game.game import run_game


def main():
    """Start the Midnight Murder application."""
    run_game()


if __name__ == "__main__":
    main()
