# import the necessary libraries
import pygame
import time

# initialize the pygame module
pygame.init()

# set the dimensions of the window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
BLOCK_SIZE = 60
ERASER_SIZE = 30

# create the window & Title
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Canvas Eraser")

# Create grid of blocks (rectangles)
grid = []
for row in range(0, WINDOW_HEIGHT, BLOCK_SIZE):
    for col in range(0, WINDOW_WIDTH, BLOCK_SIZE):
        rect = pygame.Rect(col, row, BLOCK_SIZE, BLOCK_SIZE)
        grid.append(rect)

eraser = pygame.Rect(300, 300, ERASER_SIZE, ERASER_SIZE)

running = True
while running:
    screen.fill((255, 255, 255))  # Fill background with white

    # Get mouse position and move eraser
    mouse_x, mouse_y = pygame.mouse.get_pos()
    eraser.topleft = (mouse_x, mouse_y)

    # Draw and update the grid
    new_grid = []
    for rect in grid:
        if not eraser.colliderect(rect):
            pygame.draw.rect(screen, (46, 139, 87), rect)
            new_grid.append(rect)
    grid = new_grid

    # Draw eraser
    pygame.draw.rect(screen, (255, 0, 0), eraser)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    time.sleep(0.01)

pygame.quit()
