from labyrinth import Labyrinth
from dude import Dude

import re


if __name__ == '__main__':
    with open('resources/labyrinth.txt', 'r') as file:
        labyrinth_str = file.read()
    labyrinth = Labyrinth(labyrinth_str)
    labyrinth.start_labyrinth()
