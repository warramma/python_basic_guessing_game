#5-26-24

#guessing game - try and guess the secret word

print('Try and guess the SECRET WORD! ')

secret_word = 'rose'

def print_hints():
    print('Hint 1: a flower')
    print('Hint 2: very popular')

print_hints()

guess = input('What is the SECRET WORD? ')
limit = 3
i = 1

while not(guess.lower() == 'rose') and i < limit:
    print('Oops! Guess again! You have ' + str(limit - i) + ' tries left :)' )
    i += 1
    print_hints()
    guess = input('What is the SECRET WORD? ')


if i == limit:
    print('Better luck next time :(')
else:
    print('You\'ve done it! You\'ve figured out the SECRET WORD!!')