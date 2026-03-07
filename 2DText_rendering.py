import pygame
pygame.init()
screen = pygame.display.set_mode((600, 200))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Magneto", 48)
text = font.render("Hello Python..!", True, (255, 0, 255))
x = 0
y = 80
speed = 3
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    x += speed
    if x > 600:
        x = -text.get_width()
    screen.fill((255, 255, 255))
    screen.blit(text, (x, y))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
