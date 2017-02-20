import Epic

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

def findTie(y):
    for x in y:
        if x == d[y]
    
def askUser(d):
    while True:
        enterbird = Epic.userString('Enter a bird name (exit to close): ').lower()
        if enterbird == 'exit':
            print '\nFeel free to come back and ask about my bird sightings anytime!'
            break
        elif enterbird in d:
            print 'I have seen a %s %s times' % (enterbird, d[enterbird])
        else:
            print 'I have not seen that bird.'

def main():
    birds = countBirds('birds.txt')
    askUser(birds)

main()