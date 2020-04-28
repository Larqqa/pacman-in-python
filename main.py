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
TRESHOLD = SIZE / 21

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
YELLOW = Color(255, 255, 0)

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

UPDATECAP = 1/60
pressed_keys = []
all_the_keys = ""

class Pacman:
    """The Pacman class"""

    color = YELLOW
    size = int(TRESHOLD / 2)
    position = pygame.math.Vector2(int(SIZE / 2), int(SIZE / 2))
    direction = pygame.math.Vector2(0, 0)

    def move(self):
        """Pacmans move method"""
        self.position.x += self.direction.x
        self.position.y += self.direction.y

    def draw(self):
        """Pacmanss draw methog"""
        pygame.draw.circle(SCREEN,
                           self.color,
                           [int(self.position.x),
                            int(self.position.y)],
                           self.size)


def render(pacman):
    """Draw stuff on everyloop"""

    SCREEN.fill(BG)

    # Draw a grid
    for i in range(math.floor(TRESHOLD)):
        pygame.draw.line(SCREEN, BLUE, (i * TRESHOLD, 0), (i * TRESHOLD, SIZE), 1)
        pygame.draw.line(SCREEN, BLUE, (0, i * TRESHOLD), (SIZE, i * TRESHOLD), 1)

    # Draw pressed keys
    text = FONT.render(all_the_keys, True, GREEN, BG)
    SCREEN.blit(text, (0, 0))

    # Draw pacman
    pacman.draw()

def keys():
    """Get the keys that were pressed"""

    global pressed_keys
    pressed_keys = []

    the_keys = pygame.key.get_pressed()

    # check if keys in keymap are pressed
    for key in KEYMAP:
        if the_keys[key["name"]]:

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

def update(pacman):
    """Update the game elements"""

    keys()

    global all_the_keys
    all_the_keys = ""

    # Get vector from keys
    key_vector = pygame.math.Vector2(0, 0)

    # Make a string from all pressed keys
    for key in pressed_keys:
        all_the_keys = all_the_keys + " " + key

        if key == "w":
            key_vector.y += -1
        elif key == "s":
            key_vector.y += 1
        elif key == "a":
            key_vector.x += -1
        elif key == "d":
            key_vector.x += 1

    # If no keys pressed, reset direction
    if len(pressed_keys) == 0:
        pacman.direction.x = 0
        pacman.direction.y = 0

    # Else move in to vector
    else:
        pacman.direction.x = key_vector.x
        pacman.direction.y = key_vector.y

def main():
    """Main function."""

    pacman = Pacman()

    running = True

    first_time = 0
    last_time = time.process_time() / 10000000000.0
    passed_time = 0
    unprocessed_time = 0

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # Timer stuffs
        first_time = time.process_time() / 10000000000.0
        passed_time = first_time - last_time
        last_time = first_time

        unprocessed_time += passed_time

        while unprocessed_time >= UPDATECAP:
            unprocessed_time -= UPDATECAP
            update(pacman)

        # Do stuffs
        update(pacman)
        render(pacman)
        pacman.move()

        # Update screen
        pygame.display.update()


# if name main error in emacs
# if __name__ == "__main__":
main()

# After main, exit and cleanup
del FONT
pygame.quit()
# sys.exit(0)
