EMPTY_FIELD = '.'

# nasza tablica
level = []

# wypełniamy pustą tablicę kropkami
for x in range(20):
    # stwórz wiersz z dwusdzietku pustych elementów listy
    # i przypisz go do naszej tablicy
    level.append([EMPTY_FIELD] * 20)

level[2][5] = '@'

# drukowanie zawartości tablicy level
for x in range(20):
    for y in range(20):
        # wydrukuj element tablicy o współrzędnych x,y
        # normalnie instrukcja print przechodzi do nowej linii
        # (nowa linia to specjalny niewidoczny znak '\n')
        print(level[y][x], end='')
    # tutaj na każdym końcu wyższej pętli drukujemy pusty znak
    # a print automatycznie przechodzi jeszcze do nowej linii
    print('')
