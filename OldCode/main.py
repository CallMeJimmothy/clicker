#--------------------------------------
#file to main.py
#--------------------------------------

import pygame
import json
from OldCode.engine import engine
from game_state import GameState
from upgrades import *
from clicker import *
from ui import score_display, start_screen
from Constants import WIDTH, HEIGHT, FPS


#--------------------------------------
#def main loop
#--------------------------------------

def main():

    # Initialize game state and objects
    game_state = GameState()
    my_clicker = clicker(WIDTH // 2 - 100, HEIGHT // 2 - 100, 200, 200)
    clock = pygame.time.Clock()
    try:
        with open("Clickerscore.txt", "r") as score_file:
            data = json.load(score_file)
            game_state.score = data.get("score")
            game_state.new_score = data.get("new_score")
            game_state.automatic_score_gain = data.get("automatic_score_gain")
    except:
        print("No save file found, starting a new game.")
    
    # Game loop variables
    running = True
    clicked = False
    timer = 0
    ten_second_timer = 0

    while running:
        delta_time = clock.tick(FPS) / 1000
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                with open("Clickerscore.txt", "w") as score_file:
                    json.dump(data, score_file)
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if not clicked:
                    clicked = True

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                clicked = False
            
            # Mouse wheel scrolling
            if event.type == pygame.MOUSEWHEEL:
                upgrade_list = Upgrade.instances if game_state.upgradesmenu == "Manual upgrades" else AutomaticUpgrade.instances
                for upgrade in upgrade_list:
                    upgrade.y += event.y * 20
        
        #data holding
        data = {
            "score": game_state.score,
            "new_score": game_state.new_score,
            "automatic_score_gain": game_state.automatic_score_gain,
        }

        # Clear screen
        engine.win.fill("black")

        # Game state rendering
        if game_state.win_menu == "Start Screen":
            start_screen(engine.win)
            if mouse_pressed and not clicked:
                game_state.win_menu = "Game"
                clicked = True
                
        elif game_state.win_menu == "Game":
            # Clicker interaction
            if my_clicker.draw_clicker(mouse_pos, mouse_pressed, clicked):
                game_state.score += game_state.new_score
                clicked = True

            # Upgrades panel
            panel_color = "pink" if game_state.upgradesmenu == "Manual upgrades" else "light pink"
            pygame.draw.rect(engine.win, panel_color, (25, 100, 300, 850))
            
            # Draw active upgrades
            upgrade_list = Upgrade.instances if game_state.upgradesmenu == "Manual upgrades" else AutomaticUpgrade.instances
            for upgrade in upgrade_list:
                if 100 < upgrade.y < 850:
                    if upgrade.draw(mouse_pos, mouse_pressed, clicked, game_state):
                        clicked = True

            # Upgrade type switches
            manual_btn = pygame.draw.rect(engine.win, "purple", (25, 50, 150, 50))
            auto_btn = pygame.draw.rect(engine.win, "green", (175, 50, 150, 50))
            
            if manual_btn.collidepoint(mouse_pos) and mouse_pressed and not clicked:
                game_state.upgradesmenu = "Manual upgrades"
                clicked = True
            elif auto_btn.collidepoint(mouse_pos) and mouse_pressed and not clicked:
                game_state.upgradesmenu = "Automatic upgrades"
                clicked = True

            # Display score
            score_display(game_state)
        

        # Timers
        timer += delta_time
        ten_second_timer += delta_time

        if timer >= 1:  # 1-second timer
            if game_state.automatic_score_gain > 0:
                game_state.score += game_state.automatic_score_gain
            timer = 0

        if ten_second_timer >= 10:  # 10-second debug output
            ten_second_timer = 0
            print(f"Score: {game_state.score:,} | Click Power: {game_state.new_score:,} | Auto: {game_state.automatic_score_gain:,}/s")
            for upgrade in Upgrade.instances + AutomaticUpgrade.instances:
                print(f"{upgrade.name} | purchased: {upgrade.amount}")
            
            with open("Clickerscore.txt", "w") as score_file:
                json.dump(data, score_file)

        pygame.display.flip()

#--------------------------------------
#run main
#--------------------------------------

if __name__ == "__main__":
    main()