import pygame
pygame.init()

window = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Single Click Circle Move")

x, y = 250, 200
running = True
while running:
    window.fill((255, 255, 255))  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos  
    pygame.draw.circle(window, (255, 0, 0), (x, y), 30)
    pygame.display.update()
pygame.quit()
