# Programmer: Hayden Archambault
# Program: HotDog.py
# Version: 1.2
# Program Description: Simulates a hot dog eating contest
# and asks the user to guess a winnner. User also places
# a bet that is updated depending on the outcome of the
# contest(s).

import Epic
import random
import time

# determine who is the hot dog eating champion
def win(d):
    x = 0
    champ = ''
    for item in d:
        if d[item] >= x:
            x = d[item]
            champ = item
    return champ

# determines how much each contestant eats, by a random number 1 through 10
# also prints out results in real time, every half second
def engine(d):
    print 'Ready, set, eat!\n'
    
    while True:
        for item in d:
            d[item] += random.randrange(1, 11)
        
        print 'chomp ... chomp ... chomp\n'
        time.sleep(0.5)
        print 'Tom ate %s ' % d['Tom']
        print 'Sally ate %s ' % d['Sally']
        print 'Fred ate %s \n' % d['Fred']
        
        if d['Sally'] > 50:
            break
        if d['Fred'] > 50:
            break
        if d['Tom'] > 50:
            break
    return d

# main function
def main():

    # what the user can bet with, initialized at 100
    wallet = 100
    
    while True:
        contest = {'Sally' : 0, 'Tom' : 0, 'Fred' : 0}
        
        # guess for contestant to win
        while True:
            guess = Epic.userString('Enter a guess for the winner of the contest! (Fred, Sally, or Tom): ')
            
            if guess not in contest:
                print 'That contestant does not exist...\n'
            else:
                break
        
        # place a bet using current wallet
        while True:
            bet = Epic.userInt('Place a bet ($%s in wallet): ' % wallet)
        
            if bet > wallet:
                print 'You dont have that much money...\n'
            else:
                break
        
        # calling other functions
        result = engine(contest)
        champ = win(result)
    
        print 'The winner of the Hot Dog Contest is none other than %s!' % champ
        
        # determines if user was correct, and updates current wallet 
        if guess in champ:
            print 'Congratulations, you have guessed correctly!'
            wallet += bet
            print 'Current wallet contains: $%s\n' % wallet
        else:
            print 'You were wrong, better luck next time!'
            wallet -= bet
            print 'Current wallet contains: $%s\n' % wallet
        
        # game ends if wallet is empty
        if wallet <= 0:
            print 'You are out of money!\nThanks for playing!'
            break
        
        # prompt to play again
        again = Epic.userString('Would you like to try again (y or n): ')
        if again == 'n':
            print '\nThanks for playing!'
            break

main()