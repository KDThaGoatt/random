#! python3

"""1 is heads 2 is tails"""

import random

x = (input("Heads or Tails?: "))
y = random.randint(1,2)

if x == "Heads":
    x = 1
if x == "Tails":
    x = 2

if x == y:
    print("You were correct!")
else:
    print("You were not correct")