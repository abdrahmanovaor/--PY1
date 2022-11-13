import random
from random import sample
def get_random_password() -> str:
    symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    password = ''
    i = random.sample(symbols, 8)
    password += str (i)
    return(password)

print(get_random_password())
