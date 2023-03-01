from dude import Dude

import re


class Labyrinth(object):
    def __init__(self, labyrinth: str):
        self.__labyrinth = labyrinth
        self.__labyrinth_layers = self.get_labyrinth_layers(labyrinth)
        self.validate()
        self.dude = Dude(*self.give_start_coordinates(), self.give_direction(), self)

    def start_labyrinth(self):
        self.dude.find_way_out()
        print('labyrinth solved')

    def give_content(self, x, y):
        return self.__labyrinth_layers[y][x]

    def give_start_coordinates(self):
        for i in self.__labyrinth_layers:
            for j in i:
                if j == 'S':
                    return i.index(j), self.__labyrinth_layers.index(i)

    def give_direction(self):
        wall_directions = {'left wall': 'right',
                           'right wall': 'left',
                           'front wall': 'back',
                           'back wall': 'front'}
        return wall_directions[self.find_start()]

    def find_start(self):
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
    def get_labyrinth_layers(labyrinth: str):
        return labyrinth.split('\n')

    def validate(self):
        self.check_sizes()
        self.check_walls()
        self.check_symbols()
        self.check_no_s_f_inside()

    def check_sizes(self):
        template_len = len(self.__labyrinth_layers[0])
        for layer in self.__labyrinth_layers:
            if len(layer) != template_len:
                raise LabyrinthValidateError('Некорректные размеры лабиринта.')

    def check_symbols(self):
        if not re.fullmatch(r'[01F\n]*S[01F\n]*F[01F\n]*|[01F\n]*F[01F\n]*S[01F\n]*', self.__labyrinth):
            raise LabyrinthValidateError('Некорректные символы в введенном лабиринте.')

    def check_walls(self):
        left_wall = ''.join(layer[0] for layer in self.__labyrinth_layers)
        right_wall = ''.join(layer[-1] for layer in self.__labyrinth_layers)
        walls = self.__labyrinth_layers[0] + self.__labyrinth_layers[-1] + left_wall + right_wall
        if not re.fullmatch(r'[1SF]+', walls):
            raise LabyrinthValidateError('Дырки в стенах лабиринта.')
        # TODO проверить углы зачем?

    def check_no_s_f_inside(self):
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


if __name__ == '__main__':
    with open('resources/labyrinth.txt', 'r') as file:
        labyrinth = file.read()
    labyrinth_layers = Labyrinth.get_labyrinth_layers(labyrinth)
    left_wall = ''.join(layer[0] for layer in labyrinth_layers)
    a = Labyrinth(labyrinth)
    print(a.give_start_coordinates(), a.give_direction(), '\n')
