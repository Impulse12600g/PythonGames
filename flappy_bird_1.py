import pygame
from pygame.locals import *


def flappy():
    pygame.init()

    screen_width = 864
    scree_height = 936
    # initial screen params
    screen = pygame.display.set_mode((screen_width, scree_height))

    # window title
    pygame.display.set_caption('Flappy Bird')

    run = True

    # initial game loop
    while run:

        for event in pygame.event.get():  # get all events that happening
            if event.type == pygame.QUIT:  # looking for specific one
                run = False  # breaks loop

    pygame.quit()
