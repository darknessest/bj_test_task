from random import randint
from string import ascii_lowercase


def gen_rand_word(length=5):
    word = ''
    for _ in range(length):
        word += ascii_lowercase[randint(0, len(ascii_lowercase) - 1)]

    return word


def gen_rand_email():
    return gen_rand_word() + "@" + gen_rand_word() + "." + gen_rand_word(2)


def gen_rand_text():
    text = ''
    for i in range(randint(5, 15)):
        text += gen_rand_word(randint(4, 8))
        text += ' '
    return text.rstrip()

