import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low , high)
        else:
            guess = low
        feedback = input(f"is {guess} too high (h) or too low (l): ").lower()
        if feedback == 'h':
            high  = guess - 1 
        elif  feedback == 'l':
            low  = guess + 1
    print(f" yey your guess {guess} is correct")

computer_guess(100)