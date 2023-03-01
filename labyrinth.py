import time

from dude import Dude
from output_window import App

import re


class Labyrinth(object):
    def __init__(self, labyrinth: str):
        self.__labyrinth = labyrinth
        self.__labyrinth_layers = self.__get_labyrinth_layers(labyrinth)
        self.__validate()
        self.dude = Dude(*self.__give_start_coordinates(), self.__give_direction(), self)

    def get_str_labyrinth(self):
        return self.__labyrinth

    def start_labyrinth(self):
        history_of_play_labyrinth = self.dude.find_way_out()
        print('labyrinth solved')

        app = App(history_of_play_labyrinth)


        app.mainloop()


    def give_content(self, x, y):
        return self.__labyrinth_layers[y][x]

    def __give_start_coordinates(self):
        for i in self.__labyrinth_layers:
            for j in i:
                if j == 'S':
                    return i.index(j), self.__labyrinth_layers.index(i)

    def __give_direction(self):
        wall_directions = {'left wall': 'right',
                           'right wall': 'left',
                           'front wall': 'back',
                           'back wall': 'front'}
        return wall_directions[self.__find_start()]

    def __find_start(self):
        walls = {''.join(layer[0] for layer in self.__labyrinth_layers): 'left wall',
                 ''.join(layer[-1] for layer in self.__labyrinth_layers): 'right wall',
                 self.__labyrinth_layers[0]: 'front wall',
                 self.__labyrinth_layers[-1]: 'back wall'}
        start_location = {}
        for i in walls.keys():
            if i.find('S') != -1:
                start_location[walls[i]] = True
        if len(start_location) > 1:
            raise TypeError('Я в углу спасите')
        elif len(start_location) < 1:
            raise TypeError('Старт не найден, провалидируйте')
        else:
            return tuple(start_location.keys())[0]

    @staticmethod
    def __get_labyrinth_layers(labyrinth: str):
        return labyrinth.split('\n')

    def __validate(self):
        self.__check_sizes()
        self.__check_walls()
        self.__check_symbols()
        self.__check_no_s_f_inside()

    def __check_sizes(self):
        template_len = len(self.__labyrinth_layers[0])
        for layer in self.__labyrinth_layers:
            if len(layer) != template_len:
                raise LabyrinthValidateError('Некорректные размеры лабиринта.')

    def __check_symbols(self):
        if not re.fullmatch(r'[01F\n]*S[01F\n]*F[01F\n]*|[01F\n]*F[01F\n]*S[01F\n]*', self.__labyrinth):
            raise LabyrinthValidateError('Некорректные символы в введенном лабиринте.')

    def __check_walls(self):
        left_wall = ''.join(layer[0] for layer in self.__labyrinth_layers)
        right_wall = ''.join(layer[-1] for layer in self.__labyrinth_layers)
        walls = self.__labyrinth_layers[0] + self.__labyrinth_layers[-1] + left_wall + right_wall
        if not re.fullmatch(r'[1SF]+', walls):
            raise LabyrinthValidateError('Дырки в стенах лабиринта.')
        # TODO проверить углы зачем?

    def __check_no_s_f_inside(self):
        inner_part = ''
        for i in self.__labyrinth_layers[1:-1]:
            inner_part += i[1:-2]
        if not re.fullmatch(r'[10]+', inner_part):
            raise LabyrinthValidateError('Старт и/или финиш вне стен лабиринта.')




class LabyrinthValidateError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'LabyrinthValidateError, {self.message[0]}'
        else:
            return 'LabyrinthValidateError has been raised'
