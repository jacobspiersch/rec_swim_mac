import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and, {x}: '))
        if guess < random_number:
            print("Nope. Too low.")
        elif guess > random_number:
            print("Oof. Too high.")
    print(f"Yup. The number was {random_number}")


def you_guess(x):
    low = 1
    high = x
    feedback = ''
    print('Think of a number and I will guess it ')
    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Yay! I am a good computer! I guessed the number correctly!!')


you_guess(20)




