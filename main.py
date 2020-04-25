import pygame
import time

def main():
    (width, height) = (600, 600)
    screen = pygame.display.set_mode((width, height))
    pygame.display.flip()
    pygame.display.set_caption("Hello World")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()

    pygame.quit()

main()
