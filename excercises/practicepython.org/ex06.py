str = input('Give me a string: ')

if str == str[::-1]:
    print(str, 'is a palindrome')
else:
    print(str, 'is NOT a palindrome')