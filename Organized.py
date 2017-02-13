# put comments above functions
def getGrades():
    grades = [87, 66, 92, 75]
    return grades
    
# like this
def getMax(grades):
    largest = 0
    for g in grades:
        if g > largest:
            largest = g
    return largest

def main():
    grades = getGrades()
    best = getMax(grades)
    print "Your best grade is %s." % best

main()    # dont forget to call main