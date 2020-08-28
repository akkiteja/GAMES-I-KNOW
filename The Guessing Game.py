import pygame
import sys
import random
import subprocess
pygame.init()
win = pygame.display.set_mode((500,500))
pygame.display.set_caption("The incredible guessing game")

x = 40
y = 30
width = 10
height =  20
vel=0.1
run = True
while run:
 for event in pygame.event.get():
   if event.type == pygame.QUIT:
     run =False
 keys=pygame.key.get_pressed()
 if keys[pygame.K_LEFT]:
      x-=vel
 if keys[pygame.K_RIGHT]:
      x+=vel
 if keys[pygame.K_UP]:
      y-=vel
 if keys[pygame.K_DOWN]:
      y+=vel
 win.fill((0,0,0))         
 pygame.draw.rect(win, (255,0,0), (x,y,width,height))
 pygame.display.update()

pygame.quit()