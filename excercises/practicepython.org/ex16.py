import random
import string

while 1:
    password_length_str = input('How long should the password be? ')
    if (password_length_str.isdecimal):
        print(int(password_length_str))
    else:
        print('The password length has to be a number!')

def random_pass_loop():
    allowed_characters = '1234567890qwertyuiopasdfghjkzxcvbnmQWERTYUIPASDFGHJKLZXCVBNM!@#$%^&'
    password = ''
    for i in range(16):
        password += random.choice(allowed_characters)
    return password

def random_pass_allowed_chars():
    allowed_characters = '1234567890qwertyuiopasdfghjkzxcvbnmQWERTYUIPASDFGHJKLZXCVBNM!@#$%^&'
    return ''.join(random.choices(allowed_characters, k=16))
    
def random_pass_dicts():
    allowed_characters = string.ascii_letters + string.digits
    return ''.join(random.choices(allowed_characters, k=16))

print(random_pass_loop())
print(random_pass_allowed_chars())
print(random_pass_dicts())