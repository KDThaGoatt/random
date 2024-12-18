#! python3

import random

cards = ["2 ♣", "2 ◆", "2 ♥", "2 ♠", "3 ♣", "3 ◆", "3 ♥", "3 ♠", "4 ♣", "4 ◆", "4 ♥", "4 ♠", "5 ♣", "5 ◆", "5 ♥", "5 ♠", "6 ♣", "6 ◆", "6 ♥", "6 ♠", "7 ♣", "7 ◆", "7 ♥", "7 ♠", "8 ♣", "8 ◆", "8 ♥", "8 ♠", "9 ♣", "9 ◆", "9 ♥", "9 ♠", "10 ♣", "10 ◆", "10 ♥", "10 ♠", "J ♣", "J ◆", "J ♥", "J ♠", "Q ♣", "Q ◆", "Q ♥", "Q ♠", "K ♣", "K ◆", "K ♥", "K ♠", "A ♣", "A ◆", "A ♥", "A ♠", ]

for i in range(1, 3):
    print(f"Deck {i} consists of the cards ", end=(""))
    for t in range (5):
        if i == 1:
            cardsindeck = 52 - t
        else:
            cardsindeck = 47 - t
        pick = random.randint(0, cardsindeck)
        cards.pop(pick)
        print(f"{cards[pick]}, ", end=(""))