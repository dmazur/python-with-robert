first_choice = ''
player = 0
valid_choices = ['rock', 'paper', 'scissors']

print('Rock, paper, scissors!')
while True:
    if (first_choice == ''):
        player = '1'
    else:
        player = '2'
    usr_command = input('Player ' + player + ' enter your command (q to quit): ').lower()
    if usr_command == 'q':
        break
    elif usr_command not in valid_choices: 
        print('Wrong command!')
    else:
        if first_choice == '':
            first_choice = usr_command
        elif first_choice == usr_command:
            print('Draw!')
        elif first_choice == 'rock' and usr_command == 'paper':
            print('Paper beats rock! Player 2 won!')
        elif first_choice == 'rock' and usr_command == 'scissors':
            print('Rock beats scissors! Player 1 won!')
        elif first_choice == 'paper' and usr_command == 'rock':
            print('Paper beats rock! Player 1 won!')
        elif first_choice == 'paper' and usr_command == 'scissors':
            print('Scissors beat paper! Player 2 won!')
        elif first_choice == 'scissors' and usr_command == 'rock':
            print('Rock beats scissors! Player 2 won!')
        elif first_choice == 'scissors' and usr_command == 'paper':
            print('Scissors beat paper! Player 1 won!')