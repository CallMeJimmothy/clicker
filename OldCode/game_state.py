from Constants import SAVES_FOLDER, DEFAULT_SAVE, VERSION

class GameState:
    def __init__(self):
        self.score = 0
        self.new_score = 1
        self.automatic_score_gain = 0
        self.win_menu = "Start Screen"
        self.upgradesmenu = "Manual upgrades"

game_state = GameState()