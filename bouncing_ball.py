import pygame

pygame.init()

win = pygame.display.set_mode((400, 300))

x, y = 100, 100
dx, dy = 3, 2

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    x += dx
    y += dy

    if x <= 20 or x >= 380:
        dx = -dx
    if y <= 20 or y >= 280:
        dy = -dy

    win.fill((255, 255, 255))
    pygame.draw.circle(win, (255, 0, 0), (x, y), 20)
    pygame.display.update()
    pygame.time.delay(20)

pygame.quit()
