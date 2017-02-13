# Programmer: Hayden Archambault
# Version: 1.0
# Program Description: Determines the number of people speeding during 
# rush hour and not during rush hour. Also determines the total fines 
# during rush hour and not during rush hour. A person is considered 
# speeding if they are traveling faster than 69 MPH. The fine for 
# speeding during rush hour is $150. The fine for speeding not 
# during rush hour is $100.

# reads the speeds in the specified file (filename) and returns them as a list of integers
def readData(filename):
    file = open(filename)
    speeds = []
    for line in file:
        speeds.append(int(line.strip()))
    return speeds
    
# calculates and returns the average of the numbers for specified list
def getAverage(speeds):
    avg = float(sum(speeds)) / len(speeds)
    return avg

# counts and returns number of speeds greater than or equal to maxSpeed
def countSpeeders(speeds, maxSpeed):
    count = 0
    for speed in speeds:
        if (speed >= maxSpeed):
            count = count + 1
    return count

def main(): 
    speeds = readData('rush.txt')
    speeds2 = readData('notrush.txt')
    
    # generates average of speeds
    avg1 = getAverage(speeds)
    avg2 = getAverage(speeds2)
    
    # calculates amount of speeders
    amtspeeders = countSpeeders(speeds, 70)
    amtspeeders2 = countSpeeders(speeds2, 70)
    
    # calculates fine amount, but beware of magic numbers.   150 = rushfine   100 = notrushfine
    rushfine = amtspeeders * 150
    notrushfine = amtspeeders2 * 100
    
    print 'The average speed during rush hour was %.2f' % avg1
    print 'The average speed not during rush hour was %.2f' % avg2
    print 'There were %s speeders during rush hour. Total fine = $%s' % (amtspeeders, rushfine)
    print 'There were %s speeders not during rush hour. Total fine = $%s' % (amtspeeders2, notrushfine)

    
# run program
main()