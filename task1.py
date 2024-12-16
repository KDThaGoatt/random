#! python3

import random

x = random.randint(1, 100)

for i in range(1000):
    y = int(input("Guess the random number: "))
    if y > x:
        print("Too high!")
    if y < x:
        print("Too low!")
    if y == x:
        print(f"Wow! You got it right! It took you {i} tries.")
        break