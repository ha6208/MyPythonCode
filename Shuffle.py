# Programmer: Hayden Archambault
# Program: Shuffle.py
# Version: 1.0
# Program Description: This program performs a perfect shuffle
# of an accurately built deck of fifty two cards. The user can 
# also determine how many times they would like the deck to be
# shuffled.

import Epic

# create the deck of cards
def buildDeck(rank, suit):
    deck = [x + ' of ' + y for x in rank for y in suit]
    return deck

# perform the perfect shuffle
def shuffle(deck):
    i = 0
    z = []
    while i < 26:
        x = deck[:len(deck)/2]
        y = deck[len(deck)/2:]
        z += [x[i]]
        z += [y[i]]
        i += 1
    return z

# deal a hand of five cards
def deal(deck):
    print deck[:5]

# main function
def main():
    rank = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    suit = ['Clubs', 'Hearts', 'Diamonds', 'Spades']
    
    # call the function to build the deck using the rank and suit lists
    deck = buildDeck(rank, suit)
    
    # call function to shuffle the deck a certain number of times based on user input
    shufAmount = Epic.userInt("Enter the amount of times to shuffle: ")
    for keepGoing in range(0, shufAmount):
        deck = shuffle(deck)
    
    # deal five cards from the shuffled deck
    deal(deck)

main()