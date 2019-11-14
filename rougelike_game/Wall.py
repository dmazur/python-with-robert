import subprocess as sp
from Player import *
EMPTY_FIELD = '.'
level = []

player1 = Player(10,10)

def create_level():
    for x in range(22):
       level.append([EMPTY_FIELD] * 22)
    return level

def draw_level(level):
    for x in range(22):
        for y in range(22):
            print(level[y][x], end='')
        print('')

while True:
    level = create_level()
    level[player1.x][player1.y] = '.'


    command = input('> Please, write your command: ')
    sp.call('cls',shell=True)
    if command == 'exit':
        print('Goodbye!')
        break



    print("You've written " + command)



#lewa stona

    level[0][0] = "#"
    level[0][1] = "#"
    level[0][2] = "#"
    level[0][3] = "#"
    level[0][4] = "#"
    level[0][5] = "#"
    level[0][6] = "#"
    level[0][7] = "#"
    level[0][8] = "#"
    level[0][9] = "#"
    level[0][10] = "#"
    level[0][11] = "#"
    level[0][12] = "#"
    level[0][13] = "#"
    level[0][14] = "#"
    level[0][15] = "#"
    level[0][16] = "#"
    level[0][17] = "#"
    level[0][18] = "#"
    level[0][19] = "#"
    level[0][20] = "#"
    level[0][21] = "#"

#prawa strona






    level[7][2] = "#"
    level[7][3] = "#"
    level[7][4] = "#"
    level[7][5] = "#"


    if command == 'up' and player1.y > 0:
        if level[player1.x][player1.y - 1] != '#':
            player1.move_up()

    elif command == 'down' and player1.y < 20:
        if level[player1.x][player1.y + 1] != '#':
            player1.move_down()


    elif command == 'right' and player1.x < 20:
        if level[player1.x + 1][player1.y] != '#':
            player1.move_right()


    elif command == 'left' and player1.x > 0:
        if level[player1.x - 1][player1.y] != '#':
            player1.move_left()


    else:
        print('ERROR: Wrong command')

    level[player1.x][player1.y] = '@'

    draw_level(level)
    print(player1.y)
    print(player1.x)