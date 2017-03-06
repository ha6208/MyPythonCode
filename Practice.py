import random
import Epic

def main():
    ans = random.randrange(1, 11)
    keepGoing = True
    while keepGoing:
        guess = Epic.userInt("Enter a guess from 1 to 10: ")
        if guess == ans:
            print "you win"
            keepGoing = False
main()