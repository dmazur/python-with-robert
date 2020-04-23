number = int(input('Give me a number'))

if number % 4 == 0:
    print('The number can be divided by 4')
elif number % 2 > 0:
    print('The number is odd')
else:
    print('The number is even')
