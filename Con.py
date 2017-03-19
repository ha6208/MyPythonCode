import Epic
import random

l = ['bird', 'dog', 'snake', 'fish', 'cat', 'mouse', 'starfish', 'woodchuck', 'crab']
repeat = random.randrange(0, 10)
l.append(l[repeat])
random.shuffle(l)

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
        print 'You win! it took %s tries.' % (tries)
        break