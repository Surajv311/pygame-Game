import pygame , sys , os
from pygame.locals import *

red = [250,0,0] # a list of values for rgb values
#initialize pygame
pygame.init()

# set up the size of the window
display_window = pygame.display.set_mode((1000,600))
pygame.display.set_caption('SNAKE GAME')
# setting up the drawing surface
screen = pygame.display.get_surface()
screen.fill(red) # so we have filled the screen with rgb-250,0,0
pygame.display.set_caption("game")
pygame.display.flip()

while True:

    # print("Snake game")
 
