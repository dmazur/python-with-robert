import subprocess as sp
def command_line():
    command = input('> Please, write your command: ')
    sp.call('clear', shell=True)
    return command
