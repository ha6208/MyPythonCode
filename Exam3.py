# Programmer: Hayden Archambault
# Program: Exam3.py
# Version: 1.1
# Program Description: A game that has the use turn over cards
# until they can find a matching pair. Also calculates how
# many tries it takes to win.

import Epic
import random

# takes a list and finds a random element to add to itself, and then shuffles the list
def cards(l):
    repeat = random.randrange(0, 10)
    l.append(l[repeat])
    random.shuffle(l)
    return l

# asks the user to turn over cards and shows the cards they chose
# when the guesses for each card match, the user wins
# also calculates the number of tries it took to win
def engine(l):
    tries = 0

    while(True):
        while(True):
            num1 = Epic.userInt('Pick the first card to turn over (0-9): ')
            if num1 < 0 or num1 > 9:
                print 'Invalid choice. You must pick different cards and the card must be a number from 0-9.'
            else:
                break
        while(True):
            num2 = Epic.userInt('Pick the second card to turn over (0-9): ')
            if num2 < 0 or num2 > 9:
                print 'Invalid choice. You must pick different cards and the card must be a number from 0-9.'
            else:
                break

        print 'Card %s is a %s' % (num1, l[num1])
        print 'Card %s is a %s' % (num2, l[num2])
    
        tries = tries + 1
    
        if l[num1] == l[num2]:
            print 'You win! It took %s tries.' % (tries)
            break

# creates list and calls functions
def main():
    l = ['bird', 'dog', 'snake', 'fish', 'cat', 'mouse', 'starfish', 'woodchuck', 'crab']
    cards(l)
    engine(l)

main()