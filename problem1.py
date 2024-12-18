#! python3

import random

ask = input("Which method would you like to choose? (type A or B): ")

stats = ["Strength", "Intelligence", "Wisdom", "Dexterity", "Constitution", "Charisma"]

print("Your characters stats are; ", end=(""))

if ask == "A":
    for i in range(6):
        a = random.randint(1,6)
        b = random.randint(1,6)
        c = random.randint(1,6)
        d = random.randint(1,6)
        removal = min(a, b, c, d)
        final = a + b + c + d - removal
        print(f"{stats[i]}: {final}, ", end=(""))

if ask == "B":
    for i in range(6):
        a = random.randint(2,6)
        b = random.randint(2,6)
        c = random.randint(2,6)
        final = a + b + c
        print(f"{stats[i]}: {final}, ", end=(""))