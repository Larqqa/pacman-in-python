"""
Ya yeet!
"""

import sys
import math
import time
import pygame
from pygame.locals import *

# pygame inits
pygame.font.init()

SIZE = 600

# Make the screen size be a square
(WIDTH, HEIGHT) = (SIZE, SIZE)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.flip()
pygame.display.set_caption("Pacman")


# Pygame vars
BG = Color(0, 0, 0)
RED = Color(255, 0, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)

FONT = pygame.font.SysFont('sans', 12)

KEYMAP = [
    {"name": pygame.K_a, "action": "a"},
    {"name": pygame.K_d, "action": "d"},
    {"name": pygame.K_w, "action": "w"},
    {"name": pygame.K_s, "action": "s"},
    {"name": pygame.K_f, "action": "f"},
    {"name": pygame.K_g, "action": "g"},
    {"name": pygame.K_LEFT,  "action": "left"},
    {"name": pygame.K_RIGHT, "action": "right"},
    {"name": pygame.K_UP,    "action": "up"},
    {"name": pygame.K_DOWN,  "action": "down"},
]

def draw(keys):
    SCREEN.fill(BG)

    TRESHOLD = SIZE / 10

    for i in range(math.floor(TRESHOLD)):
        pygame.draw.line(SCREEN, BLUE, (i * TRESHOLD, 0), (i * TRESHOLD, SIZE), 1)
        pygame.draw.line(SCREEN, BLUE, (0, i * TRESHOLD), (SIZE, i * TRESHOLD), 1)

    text = FONT.render(keys, True, GREEN, BG)
    SCREEN.blit(text, (0, 0))

def main():
    """Main function."""

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        pressed_keys = []
        keys = pygame.key.get_pressed()

        # check if keys in keymap are pressed
        for key in KEYMAP:
            if keys[key["name"]]:

                # Check if pressed key is already pressed
                is_present = False
                for p_key in pressed_keys:
                    if p_key == key["action"]:
                        is_present = True

                # Toggle action in list
                if is_present:
                    pressed_keys.pop(pressed_keys.index(key["action"]))
                else:
                    pressed_keys.append(key["action"])

        all_the_keys = ""
        for key in pressed_keys:
            all_the_keys = all_the_keys + " " + key            

        draw(all_the_keys)
        pygame.display.update()


# if name main error in emacs
# if __name__ == "__main__":
main()

# After main, exit and cleanup
del FONT
pygame.quit()
#sys.exit(0)
