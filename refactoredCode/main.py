#--------------------------------------
#import to main.py
#--------------------------------------

import pygame
import json
from clicker import Clicker
from upgrades import *
from Constants import *
from engine import engine
from gamestate import game_state
from StartScreen import start_screen
from numbernotations import Convert_Number_to_Short_Scale_Notation, Convert_Short_Scale_Notation_to_Number

#--------------------------------------

#--------------------------------------
#main loop
#--------------------------------------

def main():
    running = True
    clock = pygame.time.Clock()      
    clicker = Clicker(WIDTH // 2, HEIGHT // 2, 100)
    game_state.win_menu = "start screen"

    while running:
        delta_time = clock.tick(FPS) / 1000

        game_state.mouse_pos = pygame.mouse.get_pos()
        game_state.mouse_pressed = pygame.mouse.get_pressed()[0]
        
        # Reset clicked state if mouse button is released
        if not game_state.mouse_pressed:
            game_state.clicked = False
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
        if game_state.win_menu == "clicker":
            # Clear the screen
            engine.win.fill((0, 0, 0))
        
            # Draw the clicker and check for clicks
        
            if clicker.draw_clicker(game_state.mouse_pos, game_state.mouse_pressed, game_state.clicked):
                game_state.clicked = True
                game_state.score += game_state.new_score

            for upgrade in Upgrades.upgrades_instances:
                if upgrade.upgrade_type == "click":
                    if upgrade.draw_upgrade(game_state.mouse_pos, game_state.mouse_pressed, game_state.clicked):
                        game_state.clicked = True
                        upgrade.purchase_upgrade()

        # if statement inside for start screen
        start_screen()

        if game_state.win_menu == "clicker":
            # Draw the score
            score_text = engine.font.render(f"Score: {Convert_Number_to_Short_Scale_Notation(game_state.score)}", True, "white")
            engine.win.blit(score_text, (10, 10))

        pygame.display.flip()
#--------------------------------------

if __name__ == "__main__":
    main()