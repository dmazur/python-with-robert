
def matrioszka(level):
    if level > 1:
        return '(' + matrioszka(level-1) + ')'
    else:
        return '( ͡° ͜ʖ ͡°)'

print(matrioszka(10))