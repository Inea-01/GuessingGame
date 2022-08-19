import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Enter a number between 1 and {x} : "))
        assert guess > 0, "It has to be a numeric guess"
        if guess > random_number:
            print("Nah!Too high, try again!")
        elif guess < random_number:
            print("Nah! Too low. Try again!")
    print(f"Yay! You got it this time!{random_number}\n\n\n")


guess(10)


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    print("Guess a number and store it in your head and the computer will try and guess the number.")
    while feedback != 'c':
        comp_guess = random.randint(low, high)
        feedback = input(
            f"The computer's guess is: {comp_guess}\n\n Enter 'c' incase the guess is correct, 'h' incase the guess "
            f"is high "
            f"and 'l' incase the "
            f"guess is low : ").lower()
        if feedback == 'h':
            high = comp_guess - 1
        elif feedback == "l":
            low = comp_guess + 1
    print("Yay! I got it")


computer_guess(10)
