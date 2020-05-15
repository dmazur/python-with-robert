a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

first_results = [x for x in a for y in b if x == y]
print(first_results)

# other solution
second_results = [x for x in a if x in b]
print(second_results)

# now how to make it unique?
results_uq = []
for result in first_results:
    if result not in results_uq:
        results_uq.append(result)

print(results_uq)
