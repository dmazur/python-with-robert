test_str = input('Give me a sentence to reverse: ')

print(test_str)
word_list = test_str.split()
print(word_list)
word_list.reverse()
print(word_list)
str_reversed = ' '.join(word_list)

print(str_reversed)
