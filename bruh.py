import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Call this function so the Pygame library can initialize itself
pygame.init()

# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])

# This sets the name of the window
pygame.display.set_caption('Space Block')

clock = pygame.time.Clock()

# Set positions of graphics
background_position = [0, 0]
block_position = [400, 300]

# Load and set up graphics.
background_image = pygame.transform.scale(pygame.image.load("imgs/pipe.png").convert(), (1000, 600))
block_image = pygame.image.load("imgs/base.png").convert()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Copy image to screen:
    screen.blit(background_image, background_position)
    screen.blit(block_image, block_position)

    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    mouse_position = pygame.mouse.get_pos()
    x = mouse_position[0]
    y = mouse_position[1]

    # Move the block according to the mouse position.
    block_position[0] = x
    block_position[1] = y

    pygame.display.update()

    clock.tick(60)

pygame.quit()