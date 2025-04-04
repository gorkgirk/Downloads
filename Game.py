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

  
