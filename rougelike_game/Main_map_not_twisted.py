import subprocess as sp
from Player import *
EMPTY_FIELD = '.'
level = []


player1 = Player(10,10)
Map = open('map', 'r')
map_str = (Map.read())

map_row = map_str.split()
for x in map_row:
    level.append(list(x))





def draw_level(level):
    for y in range(22):
        for x in range(22):
            print(level[y][x], end='')
        print('')

while True:
    level[player1.x][player1.y] = '.'


    command = input('> Please, write your command: ')
    sp.call('cls',shell=True)
    if command == 'exit':
        print('Goodbye!')
        break



    print("You've written " + command)

    if command == 'left' and player1.y > 0:
        if level[player1.x][player1.y - 1] != '#':
            player1.move_up()

    elif command == 'right' and player1.y < 20:
        if level[player1.x][player1.y + 1] != '#':
            player1.move_down()


    elif command == 'down' and player1.x < 20:
        if level[player1.x + 1][player1.y] != '#':
            player1.move_right()


    elif command == 'up' and player1.x > 0:
        if level[player1.x - 1][player1.y] != '#':
            player1.move_left()


    else:
        print('ERROR: Wrong command')

    level[player1.x][player1.y] = '@'
    draw_level(level)
    print(player1.y)
    print(player1.x)
