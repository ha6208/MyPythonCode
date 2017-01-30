print 'please enter a sentence: ',
s1 = raw_input()
length = len(s1)
s1 = s1.replace('a', str(length))
s1 = s1.replace('e', str(length + 1))
s1 = s1.replace('i', str(length + 2))
s1 = s1.replace('o', str(length + 3))
s1 = s1.replace('u', str(length + 4))

print 'the encrypted sentece is: %s ' % s1

s1 = s1.replace(str(length), 'a')
s1 = s1.replace(str(length + 1), 'e')
s1 = s1.replace(str(length + 2), 'i')
s1 = s1.replace(str(length + 3), 'o')
s1 = s1.replace(str(length + 4), 'u')

print 'the decrypted sentence is: ' + s1