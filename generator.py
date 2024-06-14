import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

num = int(input('Number of passwords '))
length = int(input('Password length '))
numbers = input('Do we include numbers? ')
up_letters = input('Do we include capital letters? ')
low_letters = input('Do we include lower-case letters ')
symbols = input('Do we include !#$%&*+-=?@^_? ')
n_symbols = input('Do we exclude ambiguous symbols like il1Lo0O? ')
if numbers.lower() == 'yes':
    for _ in range(length):
        chars += random.choice(digits)
if up_letters.lower() == 'yes':
    for _ in range(length):
        chars += random.choice(uppercase_letters)
if low_letters.lower() == 'yes':
    for _ in range(length):
        chars += random.choice(lowercase_letters)
if symbols.lower() == 'yes':
    for _ in range(length):
        chars += random.choice(punctuation)
if n_symbols.lower() == 'yes':
    for letter in chars:
        if letter in 'il1Lo0O?':
            chars = chars.replace(letter, '')


def generate_password(pw_length, pw_chars):
    password = ''
    for i in range(length):
        password += random.choice(chars)
    return password


for _ in range(num):
    print(generate_password(length, chars))
