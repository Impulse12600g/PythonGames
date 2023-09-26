import pygame
from pygame.locals import *


def flappy():
    pygame.init()

    clock = pygame.time.Clock
    fps = 60

    screen_width = 864
    scree_height = 936
    # initial screen params
    screen = pygame.display.set_mode((screen_width, scree_height))

    # window title
    pygame.display.set_caption('Flappy Bird')

    # define game variables
    ground_scroll = 0
    scroll_speed = 4

    # load in image
    bg = pygame.image.load('img/bg.png')
    ground_img = pygame.image.load('img/ground.png')
    run = True

    # initial game loop
    while run:

        clock.tick(fps)  # scrolls a lot slower

        # draw background
        screen.blit(bg, (0, 0))

        # drae and scroll ground
        screen.blit(ground_img, (ground_scroll, 768))
        ground_scroll -= scroll_speed

        for event in pygame.event.get():  # get all events that happening
            if event.type == pygame.QUIT:  # looking for specific one
                run = False  # breaks loop

        pygame.display.update()

    pygame.quit()
