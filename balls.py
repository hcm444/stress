import sys
import pygame
import random
pygame.init()
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Stress Test")
frame_rate = 60
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
gravity = (0, 0.05)
num_balls = 1000
balls = []
for i in range(num_balls):
    x = random.uniform(0, window_size[0])
    y = random.uniform(0, window_size[1])
    vx = random.uniform(-1, 1)
    vy = random.uniform(-1, 1)
    radius = random.uniform(5, 10)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    ball = {'pos': (x, y), 'vel': (vx, vy), 'radius': radius, 'color': color}
    balls.append(ball)
while True:
    for event in pygame.event.get():
        if event.type != pygame.QUIT:
            continue
        pygame.quit()
        sys.exit()
    screen.fill((0, 0, 0))
    for ball in balls:
        ball['vel'] = (ball['vel'][0] + gravity[0], ball['vel'][1] + gravity[1])
        ball['pos'] = (ball['pos'][0] + ball['vel'][0], ball['pos'][1] + ball['vel'][1])
        if ball['pos'][0] - ball['radius'] < 0 or ball['pos'][0] + ball['radius'] > window_size[0]:
            ball['vel'] = (-ball['vel'][0], ball['vel'][1])
        if ball['pos'][1] - ball['radius'] < 0 or ball['pos'][1] + ball['radius'] > window_size[1]:
            ball['vel'] = (ball['vel'][0], -ball['vel'][1])
        pygame.draw.circle(screen, ball['color'], ball['pos'], ball['radius'])
    fps = clock.get_fps()
    fps_text = font.render(f"FPS: {fps:.2f}", True, (255, 255, 255))
    screen.blit(fps_text, (10, 10))
    pygame.display.flip()
    clock.tick(frame_rate)
