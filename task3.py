#! python3

"""rock is 1, paper is 2, scissors is 3, lizard is 4, spock is 5"""

import random

x = (input("Rock Paper Scissors Lizard Spock?: "))
y = random.randint(1, 5)

if x == "Rock":
    x = 1
if x == "Paper":
    x = 2
if x == "Scissors":
    x = 3
if x == "Lizard":
    x = 4
if x == "Spock":
    x = 5

if x == y:
    print("Its a draw!")
if x == 3 and y == 2:
    print("Scissors cuts paper, you win!")
if x == 2 and y == 3:
    print("Paper gets cut by scissors, you lose!")
if x == 2 and y == 1:
    print("Paper covers rock, you win!")
if x == 1 and y == 2:
    print("Rock gets covered by paper, you lose!")
if x == 1 and y == 4:
    print("Rock crushes lizard, you win!")
if x == 4 and y == 1:
    print("Lizard gets crushed by rock, you lose!")
if x == 4 and y == 5:
    print("Lizard poisons Spock, you win!")
if x == 5 and y == 4:
    print("Spock gets poisoned by lizard, you lose!")
if x == 5 and y == 3:
    print("Spock smashes scissors, you win!")
if x == 3 and y == 5:
    print("Scissors gets smashed by Spock, you lose!")
if x == 3 and y == 4:
    print("Scissors decapitates lizard, you win!")
if x == 4 and y == 3:
    print("Lizard gets decapitated by scissors, you lose!")
if x == 4 and y == 2:
    print("Lizard eats paper, you win!")
if x == 2 and y == 4:
    print("Paper gets eaten by lizard, you lose!")
if x == 2 and y == 5:
    print("Paper disproves Spock, you win!")
if x == 5 and y == 2:
    print("Spock gets disapproved by paper, you lose!")
if x == 5 and y == 1:
    print("Spock vaporizes rock, you win!")
if x == 1 and y == 5:
    print("Rock gets vaporized by spock, you lose!")
if x == 1 and y == 3:
    print("Rock crushes scissors, you win!")
if x == 3 and y == 1:
    print("Scissors gets smashed by rock, you lose!")