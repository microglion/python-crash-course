from pathlib import Path
import json

class GameStats:
    """Track statistics for Alien Invasion."""
    def __init__(self, ai_game):
        """Initialise statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        #High score should never be reset
        self.high_score = self.load_high_score()

    def reset_stats(self):
        """Initialise statistics that can changed during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def save_high_score(self):
        """Store high score to a json"""
        path = Path('high_score.json')
        contents = json.dumps(self.high_score)
        path.write_text(contents)

    def load_high_score(self):
        """retrieve store when game starts up"""
        path = Path('high_score.json')
        try:
            contents = path.read_text()
            return json.loads(contents)
        except FileNotFoundError:
             return 0
        