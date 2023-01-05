import pygame
import random

pygame.init()
frame_rate = 60
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Stress Test')
gravity = 0.1
balls = []


class Ball:
    def __init__(self):
        self.x = random.uniform(0, screen_width)
        self.y = random.uniform(0, screen_height)
        self.vx = random.uniform(-1, 4)
        self.vy = random.uniform(-1, 4)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.radius = random.randint(5, 10)

    def update(self):
        self.vy += gravity
        self.x += self.vx
        self.y += self.vy
        if self.x - self.radius < 0 or self.x + self.radius > screen_width:
            self.vx = -self.vx
        if self.y - self.radius < 0 or self.y + self.radius > screen_height:
            self.vy = -self.vy

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


def add_ball():
    bouncy_ball = Ball()
    balls.append(bouncy_ball)


def remove_ball():
    if balls:
        balls.pop()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                for i in range(0, 100):
                    add_ball()
            elif event.key == pygame.K_BACKSPACE:
                for i in range(0, 100):
                    remove_ball()
    for ball in balls:
        ball.update()
    screen.fill((0, 0, 0))
    for ball in balls:
        ball.draw()
    fps = clock.get_fps()
    fps_text = font.render(f"FPS: {fps:.2f}", True, (255, 255, 255))
    screen.blit(fps_text, (10, 10))
    balls_text = font.render(f"Balls: {(len(balls)) :}", True, (255, 255, 255))
    screen.blit(balls_text, (10, 40))
    pygame.display.flip()
    clock.tick(frame_rate)
pygame.quit()
