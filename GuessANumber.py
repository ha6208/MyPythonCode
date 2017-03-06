import random
import Epic

def main():
    index = 0
    ans = random.randrange(1, 11)
    keepGoing = True
    while keepGoing:
        index = index + 1
        guess = Epic.userInt("Enter guess %s for a number 1 to 10: " % index)
        if guess > ans:
            print "too high"
        if guess < ans:
            print "too low"
        if index == 5:
            print "game over"
            keepGoing = False
        if guess == ans:
            print "you win"
            print "it took %s tries" % index
            keepGoing = False

main()