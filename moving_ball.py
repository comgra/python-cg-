import pygame
pygame.init()
win = pygame.display.set_mode((400, 400))
x,y = 50,150 # ball start position
running = True
while running:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
   win.fill((255, 255, 255))      
   pygame.draw.circle(win, (255, 0, 0), (x, y), 20)  
   x += 2                            
   if x > 400:                        
       x = 0
   pygame.display.update()            
   pygame.time.delay(20)              
pygame.quit()
