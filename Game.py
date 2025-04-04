import pygame
import random
from pygame.locals import *

# Set up Pygame and initialize its modules to prepare for game development.
pygame.init()

# Define the main game settings like screen dimensions, frame rate, gravity, jump force, and obstacle speed.
WIDTH, HEIGHT = 800, 600  
FPS = 60  
GRAVITY = 0.8  
JUMP_FORCE = -18  
OBSTACLE_SPEED = 5  
# Define color values using RGB format for various elements in the game.
WHITE = (255, 255, 255)  
GREEN = (0, 255, 0)  
VIOLET = (125, 0, 255)  
BLUE = (0, 0, 255)  
RED = (255, 0, 0)  

# Create the game window with specified dimensions and set its title to "THIS IS NOT AI".
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("THIS IS NOT AI")
clock = pygame.time.Clock()  # Create a clock object to manage frame rate.

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Create a circular player character using a transparent surface and draw a red circle on it.
        self.image = pygame.Surface((60, 60), pygame.SRCALPHA)
        pygame.draw.circle(self.image, RED, (30, 30), 30)  
        self.rect = self.image.get_rect(center=(100, HEIGHT - 100))  
        self.velocity = 0  # Initialize vertical velocity to zero.
        self.on_ground = True  # Boolean flag to check if the player is on the ground.

def update(self):
        # Apply gravity to simulate falling and update the player's vertical position.
        self.velocity += GRAVITY
        self.rect.y += self.velocity

# Check if the player has hit the ground; if so, stop falling and reset velocity.
        if self.rect.bottom >= HEIGHT - 50:
            self.rect.bottom = HEIGHT - 50
            self.on_ground = True
            self.velocity = 0

def jump(self):
        # Allow jumping only when the player is on the ground; apply upward force to start jump.
        if self.on_ground:
            self.velocity = JUMP_FORCE
            self.on_ground = False

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Generate random dimensions for obstacles to add variety to gameplay.
        self.width = random.randint(30, 70)
        self.height = random.randint(20, 60)

# Create a rectangular obstacle with a green fill color.
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(GREEN)

 # Position obstacles at the right edge of the screen and align them with the ground level.
        self.rect = self.image.get_rect(
            midleft=(WIDTH, HEIGHT - self.height - 50)
        )

 def update(self):
        # Move obstacles leftward across the screen at a constant speed; remove them when off-screen.
        self.rect.x -= OBSTACLE_SPEED
        if self.rect.right < 0:
            self.kill()

# Initialize player and obstacle groups for managing sprites in the game.
player = Player()
obstacle_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Track game states like whether gameplay is active or paused and initialize score variables.
game_active = False
start_time = 0
score = 0

# Set up a timer event to spawn obstacles periodically during gameplay.
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

def display_score():
    # Calculate and display the current score based on elapsed time since gameplay started.
    current_time = (pygame.time.get_ticks() - start_time) // 1000
    score_surf = pygame.font.Font(None, 50).render(f"Score: {current_time}", True, WHITE)
    score_rect = score_surf.get_rect(center=(WIDTH//2, 50))
    screen.blit(score_surf, score_rect)
    return current_time

# Main game loop that handles events, updates game states, and draws elements on screen.
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle())
                all_sprites.add(obstacle_group)
        else:
            if event.type == KEYDOWN and event.key == K_SPACE:
                game_active = True
                start_time = pygame.time.get_ticks()

  
