import random as rd

ans = rd.randint(0,100)
guess = 0
count = 0

while ans != guess:
    count += 1
    guess = int(input('Guess my number(1-100)?'))
    if guess == ans:
        print('Bingo')
    elif count == 7:
        print('You lose')
        break
    elif guess > ans:
        print('A little too large :(')
    elif guess < ans:
        print('Too small :(')
    