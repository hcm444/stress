#balls
import pygame
import random
import math
pygame.init()
frame_rate = 60
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()
screen_width = 800
screen_height = 600
window_size = (screen_width, screen_height)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Stress Test')
gravity = 0.05
balls = []
num_frames_for_fps = 60
max_fps = 60
graph_size = (100, 50)
graph_pos = (10, 80)
graph_color = (255, 0, 255)

fps_values = []
running = True


class Ball:
    def __init__(self):
        self.x = random.uniform(0, screen_width)
        self.y = random.uniform(0, screen_height)
        self.vx = random.uniform(-4, 4)
        self.vy = random.uniform(-4, 4)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.radius = random.randint(2, 4)

    def update(self):
        self.vy += gravity
        self.x += self.vx
        self.y += self.vy
        if self.x - self.radius <= 0 or self.x + self.radius >= screen_width:
            self.vx = -self.vx
        if self.y - self.radius <= 0 or self.y + self.radius >= screen_height:
            self.vy = -self.vy

    def check_collision(self, other_ball):
            dx = self.x - other_ball.x
            dy = self.y - other_ball.y
            distance = math.sqrt(dx ** 2 + dy ** 2)

            if distance < self.radius + other_ball.radius:
                new_self_vx = (self.vx * (self.radius - other_ball.radius) +
                               2 * other_ball.radius * other_ball.vx) / (self.radius + other_ball.radius)
                new_other_vx = (other_ball.vx * (other_ball.radius - self.radius) +
                                2 * self.radius * self.vx) / (self.radius + other_ball.radius)
                self.vx = new_self_vx
                other_ball.vx = new_other_vx

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
                for i in range(0, 10):
                    add_ball()
            elif event.key == pygame.K_BACKSPACE:
                for i in range(0, 10):
                    remove_ball()
    for ball in balls:
        ball.update()
    screen.fill((0, 0, 0))
    for ball in balls:
        ball.draw()
    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            balls[i].check_collision(balls[j])
    fps = clock.get_fps()
    if pygame.time.get_ticks() / 1000 > num_frames_for_fps:
        fps_counter = 0
    fps_values.append(fps)
    if len(fps_values) > graph_size[0]:
        fps_values = fps_values[-graph_size[0]:]
    for i, fps in enumerate(fps_values):
        bar_height = fps / max_fps * graph_size[1]
        x = graph_pos[0] + i
        y = graph_pos[1] + graph_size[1] - bar_height
        bar_pos = (x, y)
        pygame.draw.rect(screen, graph_color, (bar_pos, (1, bar_height)))
    fps_text = font.render(f"FPS: {fps:.2f}", True, (255, 0, 255))
    screen.blit(fps_text, (10, 40))
    balls_text = font.render(f"Balls: {(len(balls)) :}", True, (255, 255, 255))
    screen.blit(balls_text, (10, 10))
    pygame.display.flip()
    clock.tick(frame_rate)
pygame.quit()
