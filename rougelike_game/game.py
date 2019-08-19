import subprocess as sp

EMPTY_FIELD = '.'
AVAILABLE_COMMANDS = ['up', 'down', 'left', 'right', 'exit']

player_x = 3
player_y = 3

def create_level():
    # nasza tablica
    level = []
    # wypełniamy pustą tablicę kropkami
    for x in range(20):
        # stwórz wiersz z dwusdzietku pustych elementów listy
        # i przypisz go do naszej tablicy
        level.append([EMPTY_FIELD] * 20)
    return level

def draw_level(level):
    # drukowanie zawartości tablicy level
    for x in range(20):
        for y in range(20):
            # wydrukuj element tablicy o współrzędnych x,y
            # normalnie instrukcja print przechodzi do nowej linii
            # (nowa linia to specjalny niewidoczny znak '\n')
            print(level[y][x], end='')
        # tutaj na każdym końcu wyższej pętli drukujemy pusty znak
        # a print automatycznie przechodzi jeszcze do nowej linii
        print('')


while True:
    command = input('> Please, write your command: ')
    sp.call('clear',shell=True)

    if command == 'exit':
        print('Goodbye!')
        break

    print("You've written " + command)

    if command not in AVAILABLE_COMMANDS:
        print('ERROR: Wrong command, available commands are: ' + ', '.join(AVAILABLE_COMMANDS))
    elif command == 'up' and player_y > 0: 
        player_y -= 1
    elif command == 'down' and player_y < 19: 
        player_y += 1
    elif command == 'right' and player_x < 19: 
        player_x += 1
    elif command == 'left' and player_x > 0:
        player_x -= 1
    else: print('ERROR: You can\'t go outside the map')

    level = create_level()

    level[player_x][player_y] = '@'

    draw_level(level)