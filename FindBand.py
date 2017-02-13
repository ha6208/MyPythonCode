import Epic

band = Epic.userString("Enter the band: ")
file = open('concerts.txt')   #no need for 'r'??

for line in file:
    if band in line:
        print line,

print"\nhave fun"