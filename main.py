from labyrinth import Labyrinth, LabyrinthValidateError
from dude import FindWayError

import re


if __name__ == '__main__':
    try:
        with open('resources/labyrinth.txt', 'r') as file:
            labyrinth_str = file.read()
        labyrinth = Labyrinth(labyrinth_str)
        labyrinth.start_labyrinth()
    except (LabyrinthValidateError, FindWayError) as e:
        print(e.message)
