number = int(input('Give me a number: '))

possible_divisors = range(2, (number // 2)+1)
print(possible_divisors)

print('The number divisors are:')
print(1)
for divisor in possible_divisors:
    if number % divisor == 0:
        print(divisor)
print(number)
