import random

link = 'https://www.youtube.com/watch?v=ZEE4rVaj7sE&feature=emb_logo'
def good_password_generator(length=10):

    letters = 'abcdefgihjklmnopqrstuvwxyz'
    upper_letters = letters.upper()
    digit = '0123456789'
    symbols = '.,!@#$%^&*())))_+-:;\'"'

    alphabet = letters + upper_letters + digit + symbols
    #print(alphabet[(random.randint(0,(len(alphabet)-1)))])
    print(random.choice(alphabet))
    # generator
    password = ''
    for i in range(length):
        char = random.choice(alphabet)
        password += char
    return password
print(good_password_generator(15))
popular_password = """123456
12345678
1234
qwerty
12345
dragon
pussy
baseball
football
"""
popular_passwords = popular_password.split('\n')


class c1:


    def bad_password_generator(counter = 0, length=10):
        password = popular_passwords[counter]
        counter += 1
        return password

    print(bad_password_generator())

#bad_password_generator = c1()
#print(bad_password_generator())
