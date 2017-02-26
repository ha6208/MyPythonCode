# Programmer: Hayden Archambault
# Program: Birds.py
# Version: 1.0
# Program Description: Reads from a file containing names
# of rubiks cube competitors and their completion times.
# The program then organizes them into groups based on
# time.

# reads from a file and creates dictionary
def create(filename):
    d = {}
    for line in open(filename):
        temp = line.split(',')
        name = temp[0].strip()
        time = float(temp[1].strip())
        d[name] = time
    return d

# finds names of competitors based on time and groups into list
def findName(d,x,y):
    l = []
    for name in d:
        if d[name] > x and d[name] < y:
            l.append(name)
    for i in l:
        print '\t%s' % i
    return ''

# main function
def main():
    ok = create('timings.txt')
    
    print 'Cube Head (0-9.99):'
    print findName(ok, 0, 9.99)
    print 'Square Master (10-19.99):'
    print findName(ok, 10, 19.99)
    print 'Advanced Twister (20-29.99):'
    print findName(ok, 20, 29.99)
    print 'Intermediate Turner (30-39.99):'
    print findName(ok, 30, 39.99)
    print 'Average Mover (40-59.99):'
    print findName(ok, 40, 59.99)
    print 'Pathetic (60 and beyond):'
    print findName(ok, 60, 2000)

main()