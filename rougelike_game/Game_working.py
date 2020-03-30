from Map_handler import *
from Player import *
import random
import webbrowser
import time
import keyboard
import subprocess as sp
EMPTY_FIELD = '.'
level = []
e = 0
again = ''

b1 = 1
b2 = 1
level = handle_level(level)
looking = '@'

player1 = find_player(level, Player, looking)

looking = 'b'

bot = find_player(level, Player, looking)



#while True:  # making a loop
 #   try:  # used try so that if user pressed other than the given key error will not be shown
  #      if keyboard.is_pressed('q'):  # if key 'q' is pressed
   #         print('You Pressed A Key!')
    #        break  # finishing the loop
    #except:
     #   break  # if user pressed a key other than the given key the loop will break

while True:
    level[player1.y][player1.x] = '.'
    level[bot.x][bot.y] = '.'
    while True:
        try:
            if keyboard.is_pressed('e'):
                print('EXIT y/n')
                while True:
                    try:
                        if keyboard.is_pressed('y'):
                            print('Goodbye!')
                            b1 = 2
                            b2 = 2
                            sp.call('clear', shell=True)
                            break
                        elif keyboard.is_pressed('n'):
                            b2 = 2
                            sp.call('clear', shell=True)
                            break
                    except:
                        break



            elif keyboard.is_pressed('w') and player1.y > 0:
                if level[player1.y - 1][player1.x] != '#':
                    player1.move_up()
                    sp.call('clear', shell=True)
                    break

            elif keyboard.is_pressed('s') and player1.y < 21:
                if level[player1.y + 1][player1.x] != '#':
                    player1.move_down()
                    sp.call('clear', shell=True)
                    break


            elif keyboard.is_pressed('d') and player1.x < 21:
                if level[player1.y][player1.x + 1] != '#':
                    player1.move_right()
                    sp.call('clear', shell=True)
                    break


            elif keyboard.is_pressed('a') and player1.x > 0:
                if level[player1.y][player1.x - 1] != '#':
                    player1.move_left()
                    sp.call('clear', shell=True)
                    break

        except:
            e = 1
            level[player1.y][player1.x] = '@'
        if b2 == 2:
            break
    level[player1.y][player1.x] = '@'
    time.sleep(0.1)
    b2 = 1
    if b1 == 2:
        break
    level[player1.y][player1.x] = '@'



    while True:
        random_move_generator = random.randint(0, 1000)
        if random_move_generator <= 225 and bot.x > 0:
            if level[bot.x - 1][bot.y] != '#':
                bot.move_left()
                def where():
                    print('bot up')
                break
        elif random_move_generator >= 225 and random_move_generator <= 550  and bot.x < 21:
            if level[bot.x + 1][bot.y] != '#':
                bot.move_right()
                def where():
                    print('bot down')
                break
        elif random_move_generator >= 550 and random_move_generator <= 775  and bot.y < 21:
            if level[bot.x][bot.y + 1] != '#':
                bot.move_down()
                def where():
                    print('bot right')
                break
        elif random_move_generator >= 775 and random_move_generator <= 1000 and bot.y > 0:
            if level[bot.x][bot.y - 1] != '#':
                bot.move_up()
                def where():
                    print('bot left')
                break
        again = 'Again'
    level[bot.x][bot.y] = 'b'






    draw_level(level)
    where()
    print('bot_y', bot.y)
    print('bot_x', bot.x)
    print('player.x', player1.x)
    print('player.y', player1.y)
    print('e for exit')
    print('w - up')
    print('s - down')
    print('a - left')
    print('d - right')
    if e == 1:
        print('Error_Wrong_command')
    e = 0
    print(again)
    again = ''
    if bot.y == player1.x:
        if bot.x == player1.y:
            sp.call('clear', shell=True)
            print('GET DUNKED ON ')
            time.sleep(0.6)
            webbrowser.open('https://www.youtube.com/watch?v=7OqOY1kZhL0&t=67s')
            break



