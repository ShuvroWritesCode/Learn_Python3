from random import randint
secret = randint(1, 9)
test_case = 1
while test_case <= 3:
    guess = int(input('Guess: '))
    test_case = test_case + 1
    if guess == secret:
        print('You win!')
        break
else:
    print('Sorry...Try again!')
print(f'The right guess was {secret}')
