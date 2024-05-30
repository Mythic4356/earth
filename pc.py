# Add your code here
import pygame
import serial
ser = serial.Serial("COM8", 9600)
ser.open()
pygame.init()
screen = pygame.display.set_mode((360, 360))
clock = pygame.time.Clock()
running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

      # fill the screen with a color to wipe away anything from last frame
  print(ser.readline().decode)
  screen.fill("white")
  one = pygame.image.load("earth.jpeg").convert()
  screen.blit(one, (0,0))
      # RENDER YOUR GAME HERE

      # flip() the display to put your work on screen
  pygame.display.flip()

  clock.tick(60)  # limits FPS to 60

pygame.quit()
ser.close()