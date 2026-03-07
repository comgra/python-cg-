import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Car with Rising Sun")

clock = pygame.time.Clock()

SKY_BLUE = (135, 206, 235)
ROAD_GRAY = (50, 50, 50)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (34, 139, 34)
BROWN = (101, 67, 33)
YELLOW = (255, 215, 0)

car_x = -150
car_y = 420
car_speed = 1

sun_x = 0
sun_y = 350   

trees = [(10, 370), (120, 380), (250, 375), (400, 370),
         (550, 385), (700, 370), (850, 375), (950, 380)]

def draw_road():
    pygame.draw.rect(screen, ROAD_GRAY, (0, 450, WIDTH, 150))
    for i in range(0, WIDTH, 40):
        pygame.draw.rect(screen, WHITE, (i, 520, 20, 5))

def draw_car(x, y):
    pygame.draw.rect(screen, (200, 0, 0), (x, y, 120, 40))
    pygame.draw.rect(screen, (180, 0, 0), (x + 20, y - 25, 70, 25))
    pygame.draw.circle(screen, BLACK, (x + 25, y + 40), 12)
    pygame.draw.circle(screen, BLACK, (x + 95, y + 40), 12)

def draw_tree(x, y):
    pygame.draw.rect(screen, BROWN, (x + 15, y + 40, 10, 40))
    pygame.draw.circle(screen, GREEN, (x + 20, y + 30), 30)

running = True
while running:
    clock.tick(60)
    screen.fill(SKY_BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    if sun_x < WIDTH//2:
        sun_x += 0.5
        sun_y -= 0.2

    pygame.draw.circle(screen, YELLOW, (int(sun_x), int(sun_y)), 40)

    for t in trees:
        draw_tree(t[0], t[1])

    draw_road()
    draw_car(car_x, car_y)

    car_x += car_speed
    if car_x > WIDTH:
        car_x = -150

    pygame.display.update()

pygame.quit()
sys.exit()
