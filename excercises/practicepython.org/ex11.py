def get_integer(help_text="Give me a number: "):
    return int(input(help_text))

def is_a_prime_number(number):
    possible_divisors = range(2, (number // 2)+1)
    for divisor in possible_divisors:
        if number % divisor == 0:
            return False
    return True

number = get_integer()

if is_a_prime_number(number):
    print(number, "is a prime number")
else:
    print(number, "is NOT a prime number")
