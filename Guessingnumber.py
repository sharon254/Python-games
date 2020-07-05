# This is a guessing the number game.

import random

play = True

while play:
    myName = input('Hello! What is your name? ')
    level = int(input('Pick the  level of difficulty 1(easy), 2(medium), 3(hard): '))
    if level == 1:
        top = 100
        tries = 20
    elif level == 2:
        top = 100
        tries = 10
    elif level == 3:
        top = 100
        tries = 5
    else:
        top = 100
        tries = 10
    if level == 1:
        print("Okay, " + myName + ". You have choosen easy. You have 20 guesses")
    if level == 2:
        print("Okay, " + myName + ". You have choosen medium. You have 10 guesses.")
    if level == 3:
        print("Okay, " + myName + ". You have choosen hard. You have 5 guesses.")
    elif level != 1 and level != 2 and level != 3:
        print("Invalid input!")

    number = random.randint(1, 100)
    print('Try to guess the number! Its between 1 and 100.')
    guessesTaken = 0
    while guessesTaken <= tries:
        guess = int(input('Take a guess: '))
        guessesTaken += 1
        if guess < number:
            print('Your guess is too low.')
        if guess > number:
            print('Your guess is too high.')
        if guess == number:
            break
    if guess == number:
        guessesTaken = str(guessesTaken)
        print('Good job, ' + myName + '! You guessed the number in ' + guessesTaken + ' guesses!')

    if guess != number:
        number = str(number)
        print('Nope. The number was ' + number)
    count = 1
    again = str(input("Do you want to play again, type yes or no "))
    if again == "no":
        play = False
