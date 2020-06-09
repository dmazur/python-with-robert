names = ["Michele", "Robin", "Sara", "Michele", "Michele", "Robin", "Sara", "Michele"]

def remove_duplicates_sets(input_list):
    return list(set(input_list))

def remove_duplicates_loops(input_list):
    list_wt_dups = []
    for element in input_list:
        if element not in list_wt_dups:
            list_wt_dups.append(element)
    return list_wt_dups

print(remove_duplicates_sets(names))
print(remove_duplicates_loops(names))