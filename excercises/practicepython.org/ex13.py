# n > 2: fib(n) = fib(n-1) + fib(n-2)
# n <= 2: 1
def fib(number):
    if number < 2:
        return 1
    else:
        return fib(number-1) + fib(number-2)

for i in range(0, 10):
    print(fib(i))
