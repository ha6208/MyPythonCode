d = {}

for line in open('dg.txt'):
    temp = line.split(':')
    name = temp[0].strip()
    grades = temp[1].split(',')
    for index in range(0, len(grades)):         #only way to strip? cant strip and split same line?
        grades[index] = grades[index].strip()
    d[name] = grades

print "Please enter a name: ",
s = raw_input()
if s in d:
    print '%s' % d[s]
else:
    print 'nah'