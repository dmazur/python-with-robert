# matrioszka(n) = skorupka + matrioszka(n-1) + skorupka
# matrioszka(1) = :)

def matrioszka(level):
    if level == 1:
        return ':)'
    else:
        return '(' + matrioszka(level - 1) + ')'


print(matrioszka(5))

((matrioszka(3)))

# fib(1) = 1
# fib(2) = 1
# fib(3) = 2
# fib(4) = 3
# fib(5) = 5
# fib(6) = 8

# n > 2: fib(n) = fib(n-1) + fib(n-2)
# n <= 2: 1