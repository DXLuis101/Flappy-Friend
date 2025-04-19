import pygame
import random

# Some values
WIDTH, HEIGHT = 400, 600
BIRD_X, BIRD_Y = 50, HEIGHT // 2
GRAVITY = 0.5
JUMP_STRENGTH = -10
PIPE_WIDTH = 70
PIPE_GAP = 150
PIPE_SPEED = 3

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 100, 255)


def init_game():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Flappy Friends")
    return screen


def create_pipes():
    pipes = []
    for i in range(2):
        pipe_x = WIDTH + i * 200
        pipe_height = random.randint(100, 400)
        pipes.append(pygame.Rect(pipe_x, 0, PIPE_WIDTH, pipe_height))  # This is the Top Pipe
        pipes.append(pygame.Rect(pipe_x, pipe_height + PIPE_GAP, PIPE_WIDTH, HEIGHT - pipe_height - PIPE_GAP))  # This is the Bottom Pipe
    return pipes


def draw_game(screen, bird, pipes, score):
    screen.fill(BLUE)
    pygame.draw.rect(screen, WHITE, bird)
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, pipe)
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))
    pygame.display.update()


def main():
    screen = init_game()
    bird = pygame.Rect(BIRD_X, BIRD_Y, 30, 30)
    pipes = create_pipes()
    velocity = 0
    running = True
    score = 0
    clock = pygame.time.Clock()  # Control FPS

    while running:
        screen.fill(BLUE)
        clock.tick(60)  # Limit 60 FPS

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                velocity = JUMP_STRENGTH

        velocity += GRAVITY
        bird.y += velocity

        for pipe in pipes:
            pipe.x -= PIPE_SPEED

        if pipes[0].x < -PIPE_WIDTH:
            pipes.pop(0)
            pipes.pop(0)
            new_pipe_x = WIDTH
            new_pipe_height = random.randint(100, 400)
            pipes.append(pygame.Rect(new_pipe_x, 0, PIPE_WIDTH, new_pipe_height))
            pipes.append(pygame.Rect(new_pipe_x, new_pipe_height + PIPE_GAP, PIPE_WIDTH, HEIGHT - new_pipe_height - PIPE_GAP))
            score += 1

        if bird.y < 0 or bird.y > HEIGHT:
            running = False
        for pipe in pipes:
            if bird.colliderect(pipe):
                running = False

        draw_game(screen, bird, pipes, score)

    pygame.quit()


if __name__ == "__main__":
    main()
