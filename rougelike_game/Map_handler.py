
looking = ' '

def draw_level(level):
    for y in range(22):
        for x in range(22):
            print(level[y][x], end='')
        print('')


def handle_level(level):
    level_file = open('Maps/map1.txt', 'r')
    level_str = level_file.read()
    rows = level_str.split('\n')

    for row in rows:
        level.append(list(row))

    return level


def find_player(level, Player, looking):
    for y in range(22):
        for x in range(22):
            if level[y][x] == looking:
                print(y, x)
                position_of_sprite = Player(y, x)
                return position_of_sprite


