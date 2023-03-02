import re

import labyrinth
from labyrinth import Labyrinth, LabyrinthValidateError
from dude import FindWayError
from output_window import App


class LSA_interpreter(object):
    with open('resources/LSA.txt', 'r') as file:
        input_algorithm = file.read()
    with open('resources/labyrinth.txt', 'r') as file:
        labyrinth_str = file.read()
    labyrinth = Labyrinth(labyrinth_str)
    history = []


    def is_valid_algorithm(self):
        if not re.fullmatch(r'[XYWUDsf0-9]*', self.input_algorithm):
            raise TypeError('Ошибка. Алгоритм содержит некорректные символы.')
        return self.input_algorithm

    def is_valid_commands(self, commands):
        # проверка наличия и правильной позиции Ys Yf
        if not(commands.count('Ys') == 1 and commands.count('Yf') == 1):
            raise TypeError('Ошибка. Более одной открывающей Ys или закрывающей Yf команды.')
        if not(commands[0] == 'Ys' and commands[-1] == 'Yf'):
            raise TypeError('Ошибка. Открывающая Ys или закрывающая Yf команда находятся в середине алгоритма.')

        # проверка под каждую U есть D
        for command in commands:
            if re.fullmatch(r'X\d+U\d+', command):
                u_number = command.split('U')[1]
                if commands.count(f'D{u_number}') < 1:
                    raise TypeError(f'Ошибка. Нет команды D{u_number}, на которую ссылается {command}.')
                if commands.count(f'D{u_number}') > 1:
                    raise TypeError(f'Ошибка. Более одной команды D{u_number}, на которую ссылается {command}.')

            if re.fullmatch(r'WU\d+', command):
                u_number = command.split('U')[1]
                if commands.count(f'D{u_number}') < 1:
                    raise TypeError(f'Ошибка. Нет команды D{u_number}, на которую ссылается {command}.')
                if commands.count(f'D{u_number}') > 1:
                    raise TypeError(f'Ошибка. Более одной команды D{u_number}, на которую ссылается {command}.')

        return commands


    def input_binary_code(self):
        binary_code = input('Введите бинарный код, либо оставьте поле пустым: ')
        if not re.fullmatch(r'[0-1]+|', binary_code):
            while not re.fullmatch(r'[0-1]+|', binary_code):
                binary_code = input(
                    f'Ошибка. Бинарный код может состоять только из 0 и 1, либо быть пустым.\nВведите бинарный код, либо оставьте поле пустым: ')
        return binary_code


    def parse_algorithm(self):
        commands = []

        pattern = r'Ys|Yf|Y\d+|X\d+U\d+|WU\d+|D\d+'
        word = ''
        self.is_valid_algorithm()
        for symbol in self.input_algorithm:
            # TODO возможно нужна проверка на WU(если после W цифры)
            # TODO проверить на вторую входящую U(вроде сделал уже и работает)
            if re.fullmatch(r'[0-9]', symbol) or (re.fullmatch(r'U', symbol) and ('U' not in word)):
                word += symbol
            else:
                if re.fullmatch(pattern, word):
                    commands.append(word)
                    word = ''
                word += symbol

        if re.fullmatch(pattern, word):
            commands.append(word)
            word = ''

        if word:
            raise TypeError(f'Ошибка. Неверная команда, с вхождением на индексе:{len(self.input_algorithm)-len(word)+1}')
        return commands


    def read_commands(self, commands):
        i = 0
        binary_count = 0
        while commands[i] != 'Yf':
            if commands[i] == 'Ys':
                self.ys()
                i += 1
            elif re.fullmatch(r'Y\d+', commands[i]):
                self.y(commands[i])
                i += 1
            elif re.fullmatch(r'D\d+', commands[i]):
                self.d(commands[i])
                i += 1
            elif re.fullmatch(r'WU\d+', commands[i]):
                i = self.wu(commands, i)
            elif re.fullmatch(r'X\d+U\d+', commands[i]):
                i = self.xu(commands, i)
        self.yf()


    def xu(self, commands, current_index):
        u_number = commands[current_index].split('U')[1]
        x_number = commands[current_index].split('U')[0].strip('X')
        match x_number:
            case '1':
                condition = self.labyrinth.dude.is_on_finish()
            case '2':
                condition = self.labyrinth.dude.is_start_to_the_right()
            case '3':
                condition = self.labyrinth.dude.is_start_forward()
            case '4':
                condition = self.labyrinth.dude.look_right() == '1'
            case '5':
                condition = self.labyrinth.dude.look_forward() == '1'
            case _:
                raise TypeError(f'Неизвестный индекс Х: {x_number}')
        print(f'Пройден Х{x_number}')
        if condition:
            return current_index + 1
        else:
            return commands.index(f'D{u_number}')

    def wu(self, commands, current_index):
        u_number = commands[current_index].strip('WU')
        print(f'Пройдено WU{u_number}')
        return commands.index(f'D{u_number}')


    def d(self, command):
        print(f'Пройдено D{command.strip("D")}')


    def ys(self):
        print('Начало работы программы')


    def yf(self):
        print('Программа успешно завершена')
        if self.history:
            app = App(self.history)
            app.mainloop()


    def y(self, command):
        command = command.strip('Y')
        match command:
            case '1':
                raise FindWayError('Выход недостижим!kkk')
            case '2':
                self.labyrinth.dude.turn_left()
            case '3':
                self.labyrinth.dude.turn_right()
            case '4':
                self.labyrinth.dude.step_forward()
            case _:
                raise TypeError(f'Неизвестный индекс Y: {command}')
        print(f'Пройден Y{command}')
        self.history.append(self.labyrinth.dude.print())

    def start(self):
        try:
            self.read_commands(self.is_valid_commands(self.parse_algorithm()))
        except TypeError as e:
            print(e)