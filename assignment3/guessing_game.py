import random

num = random.randint(1, 10)
guess = int(input("Enter your guess: "))

while guess != num:
    if guess < num: print("Too low.")
    elif guess > num: print("Too high.")
    guess = int(input("Enter your guess: "))

if guess == num:
    print("Correct!")
