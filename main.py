version = "0.1.3"
#---------------------------------------------------------
# setup
#---------------------------------------------------------
import pygame
pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 1500, 1000
FPS = 120
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CLICKIE")
Font_Size = 35
font = pygame.font.SysFont("comicsans", Font_Size)
PLACEHOLDER_VALUE = 0

#---------------------------------------------------------
# game state
#---------------------------------------------------------

class GameState:
    def __init__(self):
        self.score = 0
        self.new_score = 1
        self.win_menu = "Start Screen"
        self.upgradesmenu = "Manual upgrades"

game_state = GameState()


#---------------------------------------------------------
#upgrades
#---------------------------------------------------------

class Upgrade:
    def __init__(self, name, cost, addition, effect, x, y, size_x, size_y):
        self.name = name
        self.cost = cost
        self.addition = addition
        self.effect = effect
        self.amount = 0
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y
        # Animation properties
        self.click_animation_time = 0
        self.click_animation_duration = 10  # frames
        self.is_animating = False
        self.was_purchased = False  # Track successful purchases

    def apply_upgrade(self, game_state):
        game_state.new_score += self.addition
        self.amount += 1
    
    def can_afford(self, game_state):
        return game_state.score >= self.cost

    def purchase(self, game_state):
        if self.can_afford(game_state):
            game_state.score -= self.cost
            self.apply_upgrade(game_state)
            self.was_purchased = True  # Mark as purchased
            return True
        return False
    
    def draw(self, mouse_pos, mouse_pressed, clicked, game_state):
        upgrade_rect = pygame.Rect(self.x - self.size_x // 2, self.y - self.size_y // 2, self.size_x, self.size_y)
        
        # Animation logic
        if self.is_animating:
            # Draw animation based on purchase success
            if self.was_purchased:
                pygame.draw.rect(WIN, "pink", upgrade_rect)
                shrink_factor = (self.click_animation_time / self.click_animation_duration)
                shrink_amount = int(20 * (1 - shrink_factor))
                pygame.draw.rect(WIN, "green", upgrade_rect.inflate(-shrink_amount, -shrink_amount))
            else:
                pygame.draw.rect(WIN, "pink", upgrade_rect)
                shrink_factor = (self.click_animation_time / self.click_animation_duration)
                shrink_amount = int(20 * (1 - shrink_factor))
                pygame.draw.rect(WIN, "red", upgrade_rect.inflate(-shrink_amount, -shrink_amount))
            
            self.click_animation_time -= 1
            if self.click_animation_time <= 0:
                self.is_animating = False
                self.was_purchased = False
        else:
            # Normal drawing
            base_color = "blue"
            if upgrade_rect.collidepoint(mouse_pos):
                base_color = "green"
            pygame.draw.rect(WIN, base_color, upgrade_rect)

        # Text rendering (always on top)
        upgrade_text_name = font.render(f"{self.name}", True, "white")
        upgrade_text_cost = font.render(f"Cost: {self.cost:,}", True, "white")
        upgrade_text_effect = font.render(f"Gain: {self.addition:,}", True, "white")

        WIN.blit(upgrade_text_name, (self.x - 50, self.y + 15))
        WIN.blit(upgrade_text_cost, (self.x - 50, self.y + 45))
        WIN.blit(upgrade_text_effect, (self.x - 50, self.y + 75))

        # Handle clicks
        if upgrade_rect.collidepoint(mouse_pos) and mouse_pressed and not clicked:
            self.is_animating = True
            self.click_animation_time = self.click_animation_duration
            return self.purchase(game_state)
        return False
   
# upgrade - upgrade("name", cost, addition, effect, x, y, size_x, size_y)
upgrade1 = Upgrade("Upgrade 1", 10, 1, "Increases score gain by 1",100, 150, 100, 50)
upgrade2 = Upgrade("Upgrade 2", 100, 5, "Increases score gain by 5",100, 300, 100, 50)
upgrade3 = Upgrade("Upgrade 3", 1_000, 50, "Increases score gain by 50",100, 450, 100, 50)
upgrade4 = Upgrade("Upgrade 4", 10_000, 500, "Increases score gain by 500",100, 600, 100, 50)
upgrade5 = Upgrade("Upgrade 5", 1_000_000, 10000, "Increases score gain by 10,000",100, 750, 100, 50)
upgrade6 = Upgrade("Upgrade 6", 10_000_000, 100000, "Increases score gain by 100,000",100, 900, 100, 50)


upgradelist = [upgrade1, upgrade2, upgrade3, upgrade4, upgrade5, upgrade6]

#----------------------------------------------------------
#automatic upgrades
#---------------------------------------------------------

class AutomaticUpgrade:
    def __init__(self, name, cost, addition, effect, x, y, size_x, size_y):
        self.name = name
        self.cost = cost
        self.addition = addition
        self.effect = effect
        self.amount = 0
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y

    def apply_upgrade(self, game_state):
        game_state.new_score += self.addition
        self.amount += 1
    
    def can_afford(self, game_state):
        return game_state.score >= self.cost

    def purchase(self, game_state):
        if self.can_afford(game_state):
            game_state.score -= self.cost
            self.apply_upgrade(game_state)
            return True
        return False
    
    def draw(self, mouse_pos, mouse_pressed, clicked, game_state):
        # Similar to Upgrade class but for automatic upgrades
        pass  # Implement as needed for automatic upgrades

#---------------------------------------------------------
#clicker
#---------------------------------------------------------

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
            pygame.draw.rect(WIN, click_color, clicker_rect)
            # Calculate the shrinking size based on animation progress
            shrink_factor = (self.click_animation_time / self.click_animation_duration)
            shrink_amount = int(20 * (1 - shrink_factor))
            pygame.draw.rect(WIN, inner_click_color, clicker_rect.inflate(-shrink_amount, -shrink_amount))
            
            # Update animation timer
            self.click_animation_time -= 1
            if self.click_animation_time <= 0:
                self.is_animating = False
        else:
            # Normal drawing
            if clicker_rect.collidepoint(mouse_pos):
                pygame.draw.rect(WIN, hover_color, clicker_rect)
            else:
                pygame.draw.rect(WIN, base_color, clicker_rect)
        
        # Check for new clicks
        if clicker_rect.collidepoint(mouse_pos) and mouse_pressed and not clicked:
            self.is_animating = True
            self.click_animation_time = self.click_animation_duration
            return True
        return False

#---------------------------------------------------------
#draw modules
#---------------------------------------------------------

def score_display(game_state):
    score_text = font.render(f"Score: {game_state.score:,}", True, "white")
    WIN.blit(score_text, (0, 0))

def start_screen():
    WIN.fill("black")
    start_text = font.render("Click to Start", True, "white")
    WIN.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2 - start_text.get_height() // 2))

#---------------------------------------------------------
#script
#---------------------------------------------------------

def main():
    RUN = True
    CLOCK = pygame.time.Clock()
    clicked = False
    timer = 0
    ten_second_timer = 0

    # Create a clicker instance (centered)
    my_clicker = clicker(WIDTH // 2 - 100, HEIGHT // 2 - 100, 200, 200)

    while RUN:
        CLOCK.tick(FPS)
        mouse_pressed = pygame.mouse.get_pressed()[0]
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                RUN = False

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if not clicked:
                    clicked = True  # Mouse button was pressed

            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                clicked = False  # Mouse button was released
            
            # move upgrades up or down with mouse wheel
            elif event.type == pygame.MOUSEWHEEL and game_state.upgradesmenu == "Manual upgrades":
                for upgrade in upgradelist:
                    upgrade.y += event.y * 20

        WIN.fill("black")

        if game_state.win_menu == "Start Screen":
            start_screen()
            if mouse_pressed and not clicked:
                game_state.win_menu = "Game"
                clicked = True
        
        elif game_state.win_menu == "Game":
            # Check if clicker was clicked and update score
            if my_clicker.draw_clicker(mouse_pos, mouse_pressed, clicked):
                game_state.score += game_state.new_score
                clicked = True  # Prevent multiple clicks
                print(f"clicker clicked, score increased to: {game_state.score:,}")

            if game_state.upgradesmenu == "Manual upgrades":
                pygame.draw.rect(WIN, "pink", (25, 100, 300, 850))
                for upgrade in upgradelist:
                    if upgrade.y > 100 and upgrade.y < 850:
                        if upgrade.draw(mouse_pos, mouse_pressed, clicked, game_state):
                            clicked = True
                            print(f"Upgrade {upgrade.name} applied. New score gain: {game_state.new_score:,}")
            


            # Display score in game mode
            score_display(game_state)
        
        timer += 1 # Increment timer every frame
        ten_second_timer += 1 # increment ten second timer every frame

        # 1 second timer
        if timer >= FPS: # Reset timer every second
            timer = 0

        # 10 second timer
        if ten_second_timer >= FPS * 10: # Reset timer every second
            ten_second_timer = 0
            print(f"Current score: {game_state.score:,}, Score gain per click: {game_state.new_score:,}")
            for upgrade in upgradelist:
                print(f"{upgrade.name} - amount bought: {upgrade.amount:,}")
        pygame.display.flip()
        
#---------------------------------------------------------
#run
#---------------------------------------------------------

if __name__ == "__main__":
    main()


#---------------------------------------------------------
#redo for updates
#---------------------------------------------------------