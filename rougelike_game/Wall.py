import subprocess as sp
import copy
from Player import *
EMPTY_FIELD = '.'
level = []

player1 = Player(10,10)

level_file = open('level.txt', 'r')
level_str = level_file.read()
rows = level_str.split('\n')

for row in rows:
    level.append(list(row))


def draw_level(level):
    for y in range(22):
        for x in range(22):
            print(level[y][x], end='')
        print('')

while True:
    level[player1.y][player1.x] = '.'

    command = input('> Please, write your command: ')
    sp.call('clear', shell=True)
    if command == 'exit':
        print('Goodbye!')
        break



    print("You've written " + command)


    if command == 'up' and player1.x > 0:
        if level[player1.y][player1.x - 1] != '#':
            player1.move_up()

    elif command == 'down' and player1.x < 20:
        if level[player1.y][player1.x + 1] != '#':
            player1.move_down()


    elif command == 'right' and player1.y < 20:
        if level[player1.y + 1][player1.x] != '#':
            player1.move_right()


    elif command == 'left' and player1.y > 0:
        if level[player1.y - 1][player1.x] != '#':
            player1.move_left()


    else:
        print('ERROR: Wrong command')

    level[player1.y][player1.x] = '@'

    draw_level(level)
    print(player1.y)
    print(player1.x)