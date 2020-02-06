import subprocess as sp
import copy
from Player import *
EMPTY_FIELD = '.'
level = []

level_file = open('map.txt', 'r')
level_str = level_file.read()

rows = level_str.split('\n')
del rows[-1]
for row in rows:
    level.append(list(row))

y_cnt = len(rows)
x_cnt = len(rows[0])
player_position = level_str.find('@')
player_y = player_position // x_cnt
player_x = player_position % x_cnt - player_y
player1 = Player(player_x, player_y)

def draw_level(level):
    for y in range(y_cnt):
        for x in range(x_cnt):
            print(level[y][x], end='')
        print('')

draw_level(level)

while True:
    level[player1.y][player1.x] = '.'

    command = input('> Please, write your command: ')
    sp.call('clear', shell=True)
    if command == 'exit':
        print('Goodbye!')
        break



    print("You've written " + command)


    if command == 'up' and player1.x > 0:
        if level[player1.y - 1][player1.x] != '#':
            player1.move_up()

    elif command == 'down' and player1.x < x_cnt:
        if level[player1.y + 1][player1.x] != '#':
            player1.move_down()


    elif command == 'right' and player1.y < y_cnt:
        if level[player1.y][player1.x + 1] != '#':
            player1.move_right()


    elif command == 'left' and player1.y > 0:
        if level[player1.y][player1.x - 1] != '#':
            player1.move_left()


    else:
        print('ERROR: Wrong command')

    level[player1.y][player1.x] = '@'

    draw_level(level)
    print(player1.y)
    print(player1.x)