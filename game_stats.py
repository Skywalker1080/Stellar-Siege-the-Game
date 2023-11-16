class Gamestats:
    """Track statistics for alien invasion."""

    def __init__(self, ai_game):
        """Initialize stats"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start game in an inactive state.
        self.active_game_flag = False

        # High score should never be rest
        self.highscore = 0

    def reset_stats(self):
        """Initialize stats that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

