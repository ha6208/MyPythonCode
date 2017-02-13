# Programmer: Hayden Archambault
# Version: 1.0
# Program Description: This program reads a file containing information from NASA
# concerning data about yearly global temperature from the recoreded past. It calculates 
# the average deviation from the first 81 years and the last 35 years of data, and displays
# how many had a positive temperature anomaly in those groups.

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
    
    # first years
    av1 = calculateAv(temps, 0, 81)
    numberofpos = count(temps, 0 , 81)
    
    # last years
    av2 = calculateAv(temps, 81, 116)
    numberofpos2 = count(temps, 81 , 116)
    
    print "During the first 81 years, the average deviation from the temperature anomaly is %s" % av1
    print "During the first 81 years, %s had a positive temperature anomaly" % numberofpos
    print "During the last 35 years, the average deviation from the temperature anomaly is %s" % av2
    print "During the last 35 years, %s had a positive temperature anomaly" % numberofpos2

main()