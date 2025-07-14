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

Font_Size = 50
score = 0
new_score = 1
win_menu = "Start Screen"
font = pygame.font.SysFont("comicsans", Font_Size)
PLACEHOLDER_VALUE = 0

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

    def apply_upgrade(self):
        global new_score
        new_score += self.addition
        self.amount += 1
    
    def can_afford(self):
        global score
        return score >= self.cost

    def purchase(self):
        global score
        if self.can_afford():
            score -= self.cost
            self.apply_upgrade()
            return True
        return False
    
    def draw(self):
        pass

upgrade1 = Upgrade("Upgrade 1", 10, 1, "Increases score gain by 1",PLACEHOLDER_VALUE, PLACEHOLDER_VALUE, PLACEHOLDER_VALUE, PLACEHOLDER_VALUE)
upgrade2 = Upgrade("Upgrade 2", 100, 5, "Increases score gain by 5",PLACEHOLDER_VALUE, PLACEHOLDER_VALUE, PLACEHOLDER_VALUE, PLACEHOLDER_VALUE)
upgrade3 = Upgrade("Upgrade 3", 1000, 50, "Increases score gain by 50",PLACEHOLDER_VALUE, PLACEHOLDER_VALUE, PLACEHOLDER_VALUE, PLACEHOLDER_VALUE)

#---------------------------------------------------------
#clicker
#---------------------------------------------------------

class clicker:
    def __init__(self,x ,y ,width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw_clicker(self, mouse_pos, mouse_pressed, clicked):
        clicker_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(WIN, "white", clicker_rect)
        if clicker_rect.collidepoint(mouse_pos):
            pygame.draw.rect(WIN, "green", clicker_rect)
        
        # Only return True if this is a new click (mouse pressed and wasn't clicked before)
        if clicker_rect.collidepoint(mouse_pos) and mouse_pressed and not clicked:
            pygame.draw.rect(WIN, "black", clicker_rect)
            pygame.draw.rect(WIN, "green", clicker_rect.inflate(-20, -20))
            return True
        return False

#---------------------------------------------------------
#draw modules
#---------------------------------------------------------
def score_display():
    score_text = font.render(f"Score: {score}", True, WHITE)
    WIN.blit(score_text, (0, 0))

def start_screen():
    WIN.fill("black")
    start_text = font.render("Click to Start", True, WHITE)
    WIN.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2 - start_text.get_height() // 2))


#---------------------------------------------------------
#script
#---------------------------------------------------------

def main():
    global score, new_score, win_menu
    RUN = True
    CLOCK = pygame.time.Clock()
    clicked = False

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
                clicked = True  # Mouse button was pressed
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                clicked = False  # Mouse button was released

        WIN.fill("black")

        if win_menu == "Start Screen":
            start_screen()
            if mouse_pressed and not clicked:
                win_menu = "Game"
                clicked = True
        
        elif win_menu == "Game":
            # Check if clicker was clicked and update score
            if my_clicker.draw_clicker(mouse_pos, mouse_pressed, clicked):
                score += new_score
                clicked = True  # Prevent multiple clicks
                print("clicker clicked, score increased to:", score)
            
            # Display score in game mode
            score_display()

        pygame.display.flip()
        
#---------------------------------------------------------
#run
#---------------------------------------------------------

if __name__ == "__main__":
    main()