from numpy import random

x = random.randint(100)
guess = int(input('Guess The Number\n'))
while True:
        if guess == x:
            print('Got it!')
            exit()
        elif guess > x:
            print('Too high!')
            guess = int(input('Guess again!\n'))
        elif guess < x:
            print('Too low!')
            guess = int(input('Guess again!\n'))