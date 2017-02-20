# Programmer: Hayden Archambault
# Program: Birds.py
# Version: 1.4
# Program Description: Asks user to enter a bird name and 
# the program reads a .txt file and returns a dictionary
# where the information is analyzed and informtation is printed
# out for the user accordingly.

import Epic
import sys,time,random

# reads specified file and returns a dictionary whose keys are bird names and values are number of times the bird was seen
def countBirds(filename):
    d = {}
    for line in open(filename):
        temp = line.split(',')
        birdname = temp[0].strip().lower()
        timeseen = int(temp[1].strip())
        if birdname in d:
            d[birdname] += timeseen
        else:
            d[birdname] = timeseen
    return d

# finds the bird that was seen the most times
def birdMax(y):
    seenBird = 0
    mostBird = ''
    for x in y:
        if y[x] > seenBird:
            seenBird = y[x]
            mostBird = x
    ultra = {'timeseen' : seenBird, 'bird' : mostBird}
    return ultra

# gets the bird name from user and prints out information from dictionary
def askUser(d):
    ultra = birdMax(d)
    
    # some slow text for fun!
    for letter in str('I have been out bird sighting! Ask me if I have seen any specific birds!\n'):
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(.04)

    while True:
        enterbird = Epic.userString('Enter a bird name (exit to close): ').lower()
        if enterbird == 'exit':
            print '\nFeel free to come back and ask about my bird sightings anytime!'
            break
        
        # if bird entered is max, this is printed
        if enterbird == ultra['bird']:
            print 'I have seen a %s the most times, clocking in at %s sightings!\n' % (ultra['bird'], ultra['timeseen'])
            
        elif enterbird in d:
            print 'I have seen a %s %s times.' % (enterbird, d[enterbird])
            
            # checking whether or not a tie was found
            tie = ""
            for item in d:
                if item != enterbird:
                    if d[item] == d[enterbird]:
                        tie += (item + ", ")
            tie = tie.strip(", ")
            if tie != "":
                print 'I have seen these birds %s times as well: %s' % (d[enterbird], tie)
            
            # showing max
            print 'I have seen a %s the most times.\n' % ultra['bird']
            
        else:
            print 'I have not seen that bird.\n'

# run program
def main():
    birds = countBirds('birds.txt')
    askUser(birds)

main()