import pygame
from engine import engine
from gamestate import game_state

class upgrademenu_switcher_btn:
      
    ANIMATION_DURATION = 20
    HOVER_ANIMATION_SPEED = 0.1

    def __init__(self, x, y, sizeX, sizeY):
        self.x = x
        self.y = y
        self.sizeX = sizeX
        self.sizeY = sizeY

    def draw_button(self, mouse_pos, mouse_pressed, clicked):
        default_colour = "white"
        text_colour = "black"

        if game_state.upgradesmenu == "Manual upgrades":
            upgrademenu_text = "Manual"
        if game_state.upgradesmenu == "Automatic upgrades":
            upgrademenu_text = "Automatic"
              


upgrademenu_switcher_button = upgrademenu_switcher_btn(20,100, 50, 100)