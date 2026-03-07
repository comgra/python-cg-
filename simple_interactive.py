import pygame
pygame.init()
win = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
x, y = 200, 200
width, height = 60, 40
speed = 5
running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x < 400 - width:
        x += speed
    if keys[pygame.K_UP] and y > 0:
        y -= speed
    if keys[pygame.K_DOWN] and y < 400 - height:
        y += speed
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()
    clock.tick(30)
pygame.quit()
