from labyrinth import LabyrinthValidateError
from dude import FindWayError
from LSA_interpreter import LSA_interpreter

import re


if __name__ == '__main__':
    try:
        LSA_interpreter().start()

            # read_commands(is_valid_commands(parse_algorithm(is_valid_algorithm(input_algorithm))), input_binary_code())
    except (LabyrinthValidateError, FindWayError) as e:
        print(e.message)
