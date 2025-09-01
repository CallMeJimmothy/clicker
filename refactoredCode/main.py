#--------------------------------------
#import to main.py
#--------------------------------------

import pygame
import json
from clicker import Clicker
from upgrades import *
from Constants import WIDTH, HEIGHT, FPS
from engine import engine
from gamestate import game_state

#--------------------------------------

#--------------------------------------
#main loop
#--------------------------------------

def main():
    running = True
    clock = pygame.time.Clock()      
    clicked = False
    clicker = Clicker(WIDTH // 2, HEIGHT // 2, 100)

    while running:
        delta_time = clock.tick(FPS) / 1000
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[0]
        
        # Reset clicked state if mouse button is released
        if not mouse_pressed:
            clicked = False
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

        # Clear the screen
        engine.win.fill((0, 0, 0))
        
        # Draw the clicker and check for clicks
        
        if clicker.draw_clicker(mouse_pos, mouse_pressed, clicked):
            clicked = True
        
        for upgrade in Upgrades.upgrades_instances:
            upgrade.draw_upgrade(mouse_pos, mouse_pressed, clicked)

        pygame.display.flip()
#--------------------------------------

if __name__ == "__main__":
    main()