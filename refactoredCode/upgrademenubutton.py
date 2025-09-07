import pygame
from engine import engine
from gamestate import game_state

""" def upgmenu_switcher_btn(game_state):
        upgrademenu_selection = ("manual", "auto")
        upgrademenuselectionpointer = upgrademenu_selection[1]

        if game_state.upgradesmenu == "manual":
            upgrademenuselectionpointer = upgrademenu_selection[1]
        
        if game_state.upgradesmenu == "auto":
              upgrademenuselectionpointer = upgrademenu_selection[0]

        upgrademenuswitcher_text = engine.font.render(f"change menu to {upgrademenuselectionpointer}", True, "White") """


class upgrademenu_switcher_btn:
      
      ANIMATION_DURATION = 20
      HOVER_ANIMATION_SPEED = 0.1

      def __init__(self, x, y, sizeX, sizeY):
        self.x = x
        self.y = y
        self.sizeX = sizeX
        self.sizeY = sizeY


upgrademenu_switcher_button = upgrademenu_switcher_btn()