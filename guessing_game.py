#5-26-24

#guessing game - try and guess the secret word

print('Try and guess the SECRET WORD! ')

secret_word = 'rose'

def print_hints():
    print('Hint 1: a flower')
    print('Hint 2: very popular')

print_hints()

guess = input('What is the SECRET WORD? ')

while not(guess.lower() == 'rose'):
    print('Oops! Guess again!')
    print_hints()
    guess = input('What is the SECRET WORD? ')

print('You\'ve done it! You\'ve figured out the SECRET WORD!!')