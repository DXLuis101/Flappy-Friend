import pygame
import random

# Initialize Pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 400, 600
BIRD_X, BIRD_Y = 50, HEIGHT // 2
GRAVITY = 0.5
JUMP_STRENGTH = -10
PIPE_WIDTH = 70
PIPE_GAP = 150
PIPE_SPEED = 3

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 100, 255)

# Create Game Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird Clone")

# Load Bird Image
bird = pygame.Rect(BIRD_X, BIRD_Y, 30, 30)

# Pipe List
pipes = []
for i in range(2):
    pipe_x = WIDTH + i * 200
    pipe_height = random.randint(100, 400)
    pipes.append(pygame.Rect(pipe_x, 0, PIPE_WIDTH, pipe_height))  # Top Pipe
    pipes.append(pygame.Rect(pipe_x, pipe_height + PIPE_GAP, PIPE_WIDTH, HEIGHT - pipe_height - PIPE_GAP))  # Bottom Pipe

# Game Variables
velocity = 0
running = True
score = 0

# Game Loop
while running:
    screen.fill(BLUE)  # Background color
    pygame.time.delay(30)  # Control FPS

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            velocity = JUMP_STRENGTH

    # Bird Gravity Effect
    velocity += GRAVITY
    bird.y += velocity

    # Move Pipes
    for pipe in pipes:
        pipe.x -= PIPE_SPEED

    # Generate New Pipes
    if pipes[0].x < -PIPE_WIDTH:
        pipes.pop(0)
        pipes.pop(0)
        new_pipe_x = WIDTH
        new_pipe_height = random.randint(100, 400)
        pipes.append(pygame.Rect(new_pipe_x, 0, PIPE_WIDTH, new_pipe_height))
        pipes.append(pygame.Rect(new_pipe_x, new_pipe_height + PIPE_GAP, PIPE_WIDTH, HEIGHT - new_pipe_height - PIPE_GAP))
        score += 1  # Increase score

    # Check for Collision
    if bird.y < 0 or bird.y > HEIGHT:
        running = False  # Bird hits top or bottom
    for pipe in pipes:
        if bird.colliderect(pipe):
            running = False  # Bird hits a pipe

    # Draw Bird
    pygame.draw.rect(screen, WHITE, bird)

    # Draw Pipes
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, pipe)

    # Display Score
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.update()  # Refresh Screen

pygame.quit()
