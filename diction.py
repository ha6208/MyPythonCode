d = {}

for line in open('test1.txt'):
    temp = line.split(',')
    name = temp[0].strip()
    age = temp[1].strip()
    d[name] = age

print 'enter a name: ',
n = raw_input()
print d[n]         # will print their age