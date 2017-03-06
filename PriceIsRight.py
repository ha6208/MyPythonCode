import random
import time
import Epic

def main():
    # initialize prizes
    good_prizes = [ 'a new car', '100 dollars', 'brand new jordans', 'new laptop']
    bad_prizes = ['an old sock', 'a garbage can', 'a sore throat', 'more homework']
    
    # create list for the doors
    doors = ['','','']
    
    # place random bad prizes behind all three doors
    random.shuffle(bad_prizes)
    doors[0] = bad_prizes[0]
    doors[1] = bad_prizes[1]
    doors[2] = bad_prizes[2]
    
    # replace bad with good
    random.shuffle(good_prizes)
    iGoodPrize = random.randrange(0,3)
    doors[iGoodPrize] = good_prizes[0]
    
    # let user pick a door
    door = Epic.userInt("pick a door(1, 2, or 3):")
    print 'you win... '
    time.sleep(.5)
    print '...%s' % doors[door-1]

main()