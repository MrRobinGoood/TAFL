class Dude(object):
    def __init__(self, x, y, direction, labyrinth):
        self.__x = x
        self.__y = y
        self.__direction = direction
        self.__labyrinth = labyrinth

    def __str__(self):
        return f'x: {self.__x}\ny: {self.__y}\nDirection: {self.__direction}'

    def look_forward(self):
        coord_shifts = {'forward': (0, -1),
                        'back': (0, 1),
                        'left': (-1, 0),
                        'right': (1, 0)}
        forward_coordinates = [self.__x + coord_shifts[self.__direction][0], self.__y + coord_shifts[self.__direction][1]]
        return self.__labyrinth.give_content(*forward_coordinates)

    def print(self):
        def get_default_labyrinth():
            default_labyrinth = self.__labyrinth.get_str_labyrinth().split('\n')
            for i in range(len(default_labyrinth)):
                default_labyrinth[i] = list(default_labyrinth[i])
            return default_labyrinth
        history_of_play_labyrinth = [[f'x: -\ny: -\nDirection: -', self.__labyrinth.get_str_labyrinth()]]
        direction_symbol = {'forward': '↑',
                            'back': '↓',
                            'left': '←',
                            'right': '→'}
        print(self)
        labyrinth_with_person = get_default_labyrinth()
        labyrinth_with_person[self.__y][self.__x] = direction_symbol[self.__direction]
        for i in range(len(labyrinth_with_person)):
            labyrinth_with_person[i] = ''.join(labyrinth_with_person[i])
        history_of_play_labyrinth.append([str(self), '\n'.join(labyrinth_with_person)])
        print('\n'.join(labyrinth_with_person), '\n')
        return [str(self), '\n'.join(labyrinth_with_person)]

    def is_start_to_the_right(self):
        return self.look_right() == 'S'

    def is_start_forward(self):
        return self.look_forward() == 'S'

    def is_on_finish(self) -> bool:
        return self.__labyrinth.give_content(self.__x, self.__y) == 'F'

    def look_right(self):
        coord_shifts = {'forward': (1, 0),
                        'back': (-1, 0),
                        'left': (0, -1),
                        'right': (0, 1)}
        right_coordinates = [self.__x + coord_shifts[self.__direction][0], self.__y + coord_shifts[self.__direction][1]]
        return self.__labyrinth.give_content(*right_coordinates)

    def step_forward(self):
        coord_shifts = {'forward': (0, -1),
                        'back': (0, 1),
                        'left': (-1, 0),
                        'right': (1, 0)}
        self.__x += coord_shifts[self.__direction][0]
        self.__y += coord_shifts[self.__direction][1]
        return self.__x, self.__y

    def turn_right(self):
        directions = {'forward': 'right',
                      'right': 'back',
                      'back': 'left',
                      'left': 'forward'}
        self.__direction = directions[self.__direction]

    def turn_left(self):
        directions = {'forward': 'left',
                      'right': 'forward',
                      'back': 'right',
                      'left': 'back'}
        self.__direction = directions[self.__direction]

    # def __move(self):
    #     if self.look_right() == '1' and self.look_forward() == '1':
    #         self.turn_left()
    #     elif self.look_right() == '1' and self.look_forward() != '1':
    #         self.step_forward()
    #     else:
    #         self.turn_right()
    #         self.step_forward()


class FindWayError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'FindWayError, {self.message[0]}'
        else:
            return 'FindWayError has been raised'
