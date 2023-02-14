import re


class Labyrinth(object):
    @staticmethod
    def get_labyrinth_layers(labyrinth: str):
        return labyrinth.split('\n')

    def validate(self):
        pass

    def check_sizes(self, labyrinth):
        labyrinth_layers = self.get_labyrinth_layers(labyrinth)
        template_len = len(labyrinth_layers[0])
        for layer in labyrinth_layers:
            if layer != template_len:
                raise LabyrinthValidateError('Некорректные размеры лабиринта.')

    def check_symbols(self, labyrinth):
        if not re.fullmatch(r'[01\n]*S[01\n]*F[01\n]*', labyrinth):
            raise LabyrinthValidateError('Некорректные символы в введенном лабиринте.')

    def check_walls(self, labyrinth):
        labyrinth_layers = self.get_labyrinth_layers(labyrinth)
        left_wall = ''.join(layer[0] for layer in labyrinth_layers)
        right_wall = ''.join(layer[-1] for layer in labyrinth_layers)
        walls = labyrinth_layers[0] + labyrinth_layers[-1] + left_wall + right_wall
        # if re.fullmatch('[1]*')
        # TODO проверить углы

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
    a = Labyrinth()
    print(a.check_start_finish(labyrinth))
