# Programmer: Hayden Archambault
# Version: 1.0
# Program Description: This program reads a file containing information from NASA
# concerning data about yearly global temperature from the recorded past. It calculates 
# the average deviation from a first percentage of years and how many positive temperature anomalies
# occurred in that set.

import Epic

# reads from the temps.txt file and puts into a list -> temps
def readTemps():
    file = open('temps.txt', 'r')
    temps = []
    for line in file:
        words = line.replace("\n", "")
        temps.append(float(words))
    return temps

# calculates standard deviation
def calculateAv(temps, start, stop):
    total = 0.0
    for index in range(start, stop):
        total = total + float(temps[index])
    av1 = (total / (stop-start))
    return av1

# calculates positive temp anomaly
def count(temps, start, stop):
    count = 0
    for index in range(start, stop):
        if temps[index] > 0:
            count = count + 1
    return count

def main():
    temps = readTemps()
    
    # finding the percent of years
    percent = Epic.userInt("Enter the percentage of years you wish to view, which will be shown in comparison to the remaining percent: ")
    percent = (percent / 100.0)
    percent = percent * 116.0
    percent = int(percent)
    
    # first years
    av1 = calculateAv(temps, 0, percent)
    numberofpos = count(temps, 0, percent)
    
    opptotal = 116 - percent
    
    # last years
    av2 = calculateAv(temps, percent, 116)
    numberofpos2 = count(temps, percent, 116)
    
    print "\nDuring the first %d years, the average deviation from the temperature anomaly is %s" % (percent, av1)
    print "During the first %d years, %s had a positive temperature anomaly" % (percent, numberofpos)
    print "During the last %d years, the average deviation from the temperature anomaly is %s" % (opptotal, av2)
    print "During the last %d years, %s had a positive temperature anomaly" % (opptotal, numberofpos2)

main()