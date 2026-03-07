import pygame
pygame.init()
win = pygame.display.set_mode((400, 400))
x1, y1 = 50, 100
x2, y2 = 20, 200
x3, y3 = 80, 300
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    win.fill((255, 255, 255))   
    pygame.draw.circle(win, (255, 0, 0), (x1, y1), 20)   
    pygame.draw.circle(win, (0, 0, 255), (x2, y2), 20)   
    pygame.draw.circle(win, (0, 200, 0), (x3, y3), 20)   

    x1 += 2        
    y2 -= 1        
    x3 += 1        
    if x1 > 400:
        x1 = 0
    if y2 < 0:
        y2 = 400
    if x3 > 400:
        x3 = 0
    pygame.display.update()     
    pygame.time.delay(20)       
pygame.quit()
