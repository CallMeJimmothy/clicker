import pygame
import math
from engine import engine
from Constants import HEIGHT, WIDTH

class Clicker:
    def __init__(self, x, y, width):
        self.x = x
        self.y = y
        self.width = width
        self.is_animating = False
        self.click_animation_duration = 20  # Duration of the click animation in frames
        self.click_animation_time = 0
        # Add hover animation properties
        self.current_scale = 1.0
        self.target_scale = 1.0
        self.hover_animation_speed = 0.1

    def draw_clicker(self, mouse_pos, mouse_pressed, clicked):
        # colours
        default_color = "white"
        hover_color = (46, 139, 87) # Dark Sea Green
        click_colour = (46, 139, 87) # Dark Sea Green
        
        # scale factors
        hover_scale_factor = 1.2
        min_scale_factor = 0.8  # How small it gets when shrinking
        max_scale_factor = 1.3  # How large it gets when expanding
        
        # Check for collision
        clicker_circle = pygame.Rect(self.x - self.width, self.y - self.width, self.width * 2, self.width * 2)
        
        # Update hover target scale based on mouse position
        self.target_scale = hover_scale_factor if clicker_circle.collidepoint(mouse_pos) else 1.0
        
        # Smoothly interpolate current scale towards target scale
        self.current_scale += (self.target_scale - self.current_scale) * self.hover_animation_speed
        
        # Handle click
        if mouse_pressed and clicker_circle.collidepoint(mouse_pos) and not clicked:
            self.is_animating = True
            self.click_animation_time = self.click_animation_duration
            return True
        
        # Handle click animation
        if self.is_animating:
            # Calculate the animation progress (0 to 1)
            progress = self.click_animation_time / self.click_animation_duration
            
            # Create a bouncing effect using sine wave
            bounce_factor = min_scale_factor + (1 + math.sin(progress * math.pi * 2)) * (max_scale_factor - min_scale_factor) / 2
            
            # Draw the bouncing circle
            current_width = int(self.width * bounce_factor)
            pygame.draw.circle(engine.win, click_colour, (self.x, self.y), current_width)
            
            # Decrement animation timer
            self.click_animation_time -= 1
            
            # End animation when timer reaches 0
            if self.click_animation_time <= 0:
                self.is_animating = False
                self.click_animation_time = 0
        
        # Handle hover effect (when not animating)
        elif not self.is_animating:
            current_width = int(self.width * self.current_scale)
            color = hover_color if clicker_circle.collidepoint(mouse_pos) else default_color
            pygame.draw.circle(engine.win, color, (self.x, self.y), current_width)
        
        return False

