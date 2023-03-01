class Dude(object):
    def __init__(self, x, y, direction, labyrinth):
        self.__x = x
        self.__y = y
        self.__direction = direction
        self.__labyrinth = labyrinth

    def __str__(self):
        return f'x: {self.__x}\ny: {self.__y}\ndir: {self.__direction}'

    def __look_forward(self):
        coord_shifts = {'forward': (0, 1),
                        'back': (0, -1),
                        'left': (-1, 0),
                        'right': (1, 0)}
        forward_coordinates = [self.__x + coord_shifts[self.__direction][0], self.__y + coord_shifts[self.__direction][1]]
        return self.__labyrinth.give_content(*forward_coordinates)

    def find_way_out(self):
        # TODO: print labyrinth on every step
        while self.__labyrinth.give_content(self.__x, self.__y) != 'F':
            self.__move()

    def __look_right(self):
        coord_shifts = {'forward': (1, 0),
                        'back': (-1, 0),
                        'left': (0, 1),
                        'right': (0, -1)}
        right_coordinates = [self.__x + coord_shifts[self.__direction][0], self.__y + coord_shifts[self.__direction][1]]
        return self.__labyrinth.give_content(*right_coordinates)

    def __step_forward(self):
        coord_shifts = {'forward': (0, 1),
                        'back': (0, -1),
                        'left': (-1, 0),
                        'right': (1, 0)}
        self.__x += coord_shifts[self.__direction][0]
        self.__y += coord_shifts[self.__direction][1]
        return self.__x, self.__y

    def __turn_right(self):
        directions = {'forward': 'right',
                      'right': 'back',
                      'back': 'left',
                      'left': 'forward'}
        self.__direction = directions[self.__direction]

    def __turn_left(self):
        directions = {'forward': 'left',
                      'right': 'forward',
                      'back': 'right',
                      'left': 'back'}
        self.__direction = directions[self.__direction]

    def __move(self):
        if self.__look_right() == '1' and self.__look_forward() == '1':
            self.__turn_left()
        elif self.__look_right() == '1' and self.__look_forward() == '0':
            self.__step_forward()
        else:
            self.__turn_right()
            self.__step_forward()

