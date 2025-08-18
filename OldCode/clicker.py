
import pygame
from engine import engine

class clicker:
    def __init__(self,x ,y ,width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.is_animating = False
        self.click_animation_duration = 10  # Duration of the click animation in frames
    
    def draw_clicker(self, mouse_pos, mouse_pressed, clicked):
        clicker_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        
        # Default state (white)
        base_color = "white"
        hover_color = "green"
        click_color = "black"
        inner_click_color = "green"
        
        # Check if we're animating
        if self.is_animating:
            # Draw the click animation
            pygame.draw.rect(engine.win, click_color, clicker_rect)
            # Calculate the shrinking size based on animation progress
            shrink_factor = (self.click_animation_time / self.click_animation_duration)
            shrink_amount = int(20 * (1 - shrink_factor))
            pygame.draw.rect(engine.win, inner_click_color, clicker_rect.inflate(-shrink_amount, -shrink_amount))
            
            # Update animation timer
            self.click_animation_time -= 1
            if self.click_animation_time <= 0:
                self.is_animating = False
        else:
            # Normal draengine.wing
            if clicker_rect.collidepoint(mouse_pos):
                pygame.draw.rect(engine.win, hover_color, clicker_rect)
            else:
                pygame.draw.rect(engine.win, base_color, clicker_rect)
        
        # Check for new clicks
        if clicker_rect.collidepoint(mouse_pos) and mouse_pressed and not clicked:
            self.is_animating = True
            self.click_animation_time = self.click_animation_duration
            return True
        return False
