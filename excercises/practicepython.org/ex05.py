a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for elem_a in a:
    if elem_a in b:
        if elem_a not in c:
            c.append(elem_a)

print(c)

# alt version
print(set(filter(lambda elem: elem in b, a)))