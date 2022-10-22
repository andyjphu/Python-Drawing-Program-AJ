import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 480))

running = 1
mouse_pressed = False
screen.fill((255,255,255))
while running:
  for event in pygame.event.get():
    if event.type == QUIT:
      running = 0
    else:
      if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pressed = True
      elif event.type == pygame.MOUSEBUTTONUP:
        mouse_pressed = False
        
      if event.type == pygame.MOUSEMOTION and mouse_pressed:
        #print("UREUHUFEFU")
        pygame.draw.rect(screen, (0,0,0), (pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],5,5))

  #screen.fill((120, 120, 120))
  pygame.display.flip()

pygame.quit()