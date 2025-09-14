
import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Runner 🦖")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()

# Fonts
font = pygame.font.SysFont(None, 40)

# Dino
dino = pygame.Rect(50, 300, 50, 50)
dino_y_change = 0
gravity = 1
is_jumping = False

# Obstacles
obstacles = []
speed = 7

# Score
score = 0

def draw_text(text, x, y):
    screen.blit(font.render(text, True, BLACK), (x, y))

def game_loop():
    global dino_y_change, is_jumping, obstacles, score, speed

    running = True
    while running:
        screen.fill(WHITE)

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not is_jumping:
                    dino_y_change = -15
                    is_jumping = True

        # Dino movement
        dino_y_change += gravity
        dino.y += dino_y_change
        if dino.y >= 300:
            dino.y = 300
            is_jumping = False

        # Spawn obstacles
        if len(obstacles) == 0 or obstacles[-1].x < 600:
            obstacles.append(pygame.Rect(800, 320, 30, 50))

        # Move obstacles
        for obs in obstacles:
            obs.x -= speed
        obstacles = [obs for obs in obstacles if obs.x > -50]

        # Collision detection
        for obs in obstacles:
            if dino.colliderect(obs):
                draw_text("Game Over! Press R to Restart", 200, 200)
                pygame.display.flip()
                waiting = True
                while waiting:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            waiting = False
                            running = False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:
                                obstacles = []
                                score = 0
                                speed = 7
                                dino.y = 300
                                waiting = False
                break

        # Increase score
        score += 1
        if score % 500 == 0:
            speed += 1

        # Draw dino
        pygame.draw.rect(screen, BLACK, dino)

        # Draw obstacles
        for obs in obstacles:
            pygame.draw.rect(screen, (200, 0, 0), obs)

        # Draw score
        draw_text("Score: " + str(score), 10, 10)

        # Update
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

# Run game
game_loop()
