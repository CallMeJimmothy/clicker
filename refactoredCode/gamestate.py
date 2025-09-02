import pygame

class GameState:
    def __init__(self):
        self.score = 0
        self.new_score = 1
        self.automatic_score_gain = 0
        self.win_menu = "Start Screen"
        self.upgradesmenu = "Manual upgrades"
        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse_pressed = pygame.mouse.get_pressed()[0]
        self.clicked = False

game_state = GameState()