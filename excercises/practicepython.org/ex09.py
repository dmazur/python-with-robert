import random

counter = 0
wins = 0

while True:
    random_number = random.randint(0, 9)

    guess = input('Take your guess (or type "exit" to quit): ')

    if guess == 'exit':
        if (counter > 0):
            pct = wins / counter * 100
            print('Thanks for playing! You\'ve guessed ' + str(counter) + ' times and you were correct ' + str(pct) + '% of the time')
        break

    if guess.isnumeric() == False:
        print('The guess has to be a number!')
        continue

    counter += 1
    if random_number > int(guess):
        print('You guessed too low')
    elif random_number < int(guess):
        print('You guessed too high')
    else:
        print('Correct! The number was ' + guess)
        wins += 1