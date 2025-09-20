import pygame
from engine import engine
from gamestate import game_state
import math

class upgrademenu_switcher_btn:
      
    ANIMATION_DURATION = 20
    HOVER_ANIMATION_SPEED = 0.1

    def __init__(self, x, y, sizeX, sizeY):
        self.x = x
        self.y = y
        self.font = pygame.font.SysFont("Arial", 20)
        self.rect = pygame.Rect(x, y, sizeX, sizeY)

        self.is_animating = False
        self.animation_time = 0
        self.current_scale = 1.0
        self.target_scale = 1.0

    def draw_button(self, mouse_pos, mouse_pressed, clicked):
        default_color = "white"
        hover_color = (46, 139, 87) # Dark Sea Green
        click_colour = (46, 139, 87) # Dark Sea Green
        text_color = "Black"

        hover_scale_factor = 1.1
        min_scale_factor = 0.9 
        max_scale_factor = 1.15



        if game_state.upgradesmenu == "Manual upgrades":
            upgrademenu_text = "Manual"
            upgradebutton_text = self.font.render(f"{upgrademenu_text} ", True, text_color)

            # Update hover target scale based on mouse position
            self.target_scale = hover_scale_factor if self.rect.collidepoint(mouse_pos) else 1.0

            # Smoothly interpolate current scale towards target scale
            self.current_scale += (self.target_scale - self.current_scale) * self.HOVER_ANIMATION_SPEED

            # Handle click
            if mouse_pressed and self.rect.collidepoint(mouse_pos) and not clicked:
                pygame.draw.rect(engine.win, click_colour, self.rect)
                self.is_animating = True
                self.animation_time = self.ANIMATION_DURATION
                return True
            
            # Handle animation
            if self.is_animating:
                # Calculate the animation progress (0 to 1)
                progress = self.animation_time / self.ANIMATION_DURATION

                # Create a bouncing effect using sine wave
                bounce_factor = min_scale_factor + (1 + math.sin(progress * math.pi * 2)) * (max_scale_factor - min_scale_factor) / 2

                # Draw the bouncing rectangle
                current_width = int(self.rect.width * bounce_factor)
                current_height = int(self.rect.height * bounce_factor)
                current_x = self.rect.centerx - current_width // 2
                current_y = self.rect.centery - current_height // 2
                animated_rect = pygame.Rect(current_x, current_y, current_width, current_height)
                pygame.draw.rect(engine.win, click_colour, animated_rect)

                # Decrement animation timer
                self.animation_time -= 1

                # End animation when timer reaches 0
                if self.animation_time <= 0:
                    self.is_animating = False
                    self.animation_time = 0
            # Handle hover effect (when not animating)
            elif not self.is_animating:
                current_width = int(self.rect.width * self.current_scale)
                current_height = int(self.rect.height * self.current_scale)
                current_x = self.rect.centerx - current_width // 2
                current_y = self.rect.centery - current_height // 2
                hover_rect = pygame.Rect(current_x, current_y, current_width, current_height)
                color = hover_color if self.rect.collidepoint(mouse_pos) else default_color
                pygame.draw.rect(engine.win, color, hover_rect)
                engine.win.blit(upgradebutton_text, (hover_rect.x, hover_rect.y))
            
            return False

        if game_state.upgradesmenu == "Automatic upgrades":
            upgrademenu_text = "Automatic"
            
            upgradebutton_text = self.font.render(f"{upgrademenu_text} ", True, text_color)

            # Update hover target scale based on mouse position
            self.target_scale = hover_scale_factor if self.rect.collidepoint(mouse_pos) else 1.0

            # Smoothly interpolate current scale towards target scale
            self.current_scale += (self.target_scale - self.current_scale) * self.HOVER_ANIMATION_SPEED

            # Handle click
            if mouse_pressed and self.rect.collidepoint(mouse_pos) and not clicked:
                pygame.draw.rect(engine.win, click_colour, self.rect)
                self.is_animating = True
                self.animation_time = self.ANIMATION_DURATION
                return True
            
            # Handle animation
            if self.is_animating:
                # Calculate the animation progress (0 to 1)
                progress = self.animation_time / self.ANIMATION_DURATION

                # Create a bouncing effect using sine wave
                bounce_factor = min_scale_factor + (1 + math.sin(progress * math.pi * 2)) * (max_scale_factor - min_scale_factor) / 2

                # Draw the bouncing rectangle
                current_width = int(self.rect.width * bounce_factor)
                current_height = int(self.rect.height * bounce_factor)
                current_x = self.rect.centerx - current_width // 2
                current_y = self.rect.centery - current_height // 2
                animated_rect = pygame.Rect(current_x, current_y, current_width, current_height)
                pygame.draw.rect(engine.win, click_colour, animated_rect)

                # Decrement animation timer
                self.animation_time -= 1

                # End animation when timer reaches 0
                if self.animation_time <= 0:
                    self.is_animating = False
                    self.animation_time = 0
            # Handle hover effect (when not animating)
            elif not self.is_animating:
                current_width = int(self.rect.width * self.current_scale)
                current_height = int(self.rect.height * self.current_scale)
                current_x = self.rect.centerx - current_width // 2
                current_y = self.rect.centery - current_height // 2
                hover_rect = pygame.Rect(current_x, current_y, current_width, current_height)
                color = hover_color if self.rect.collidepoint(mouse_pos) else default_color
                pygame.draw.rect(engine.win, color, hover_rect)
                engine.win.blit(upgradebutton_text, (hover_rect.x, hover_rect.y))
            
            return False            


upgrademenu_switcher_button = upgrademenu_switcher_btn(20,100, 100, 100)