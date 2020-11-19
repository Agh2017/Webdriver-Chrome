import random
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