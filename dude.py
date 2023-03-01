class Dude(object):
    def __init__(self, x, y, direction, labyrinth):
        self.x = x
        self.y = y
        self.direction = direction
        self.labyrinth = labyrinth

    @property
    def get_position(self):
        return self.x, self.y

    def __str__(self):
        return f'x: {self.x}\ny: {self.y}\ndir: {self.direction}'

    def look_forward(self):
        coord_shifts = {'forward': (0, 1),
                        'back': (0, -1),
                        'left': (-1, 0),
                        'right': (1, 0)}
        forward_coordinates = [self.x + coord_shifts[self.direction][0], self.y + coord_shifts[self.direction][1]]
        return self.labyrinth.give_content(*forward_coordinates)

    def find_way_out(self):
        # TODO: print labyrinth on every step
        while self.labyrinth.give_content(self.x, self.y) != 'F':
            self.move()

    def look_right(self):
        coord_shifts = {'forward': (1, 0),
                        'back': (-1, 0),
                        'left': (0, 1),
                        'right': (0, -1)}
        right_coordinates = [self.x + coord_shifts[self.direction][0], self.y + coord_shifts[self.direction][1]]
        return self.labyrinth.give_content(*right_coordinates)

    def step_forward(self):
        coord_shifts = {'forward': (0, 1),
                        'back': (0, -1),
                        'left': (-1, 0),
                        'right': (1, 0)}
        self.x += coord_shifts[self.direction][0]
        self.y += coord_shifts[self.direction][1]
        return self.x, self.y

    def turn_right(self):
        directions = {'forward': 'right',
                      'right': 'back',
                      'back': 'left',
                      'left': 'forward'}
        self.direction = directions[self.direction]

    def turn_left(self):
        directions = {'forward': 'left',
                      'right': 'forward',
                      'back': 'right',
                      'left': 'back'}
        self.direction = directions[self.direction]

    def move(self):
        if self.look_right() == '1' and self.look_forward() == '1':
            self.turn_left()
        elif self.look_right() == '1' and self.look_forward() == '0':
            self.step_forward()
        else:
            self.turn_right()
            self.step_forward()

