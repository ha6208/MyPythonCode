print 'please enter a sentence: ',
s1 = raw_input()
s1 = s1.replace('a', str(len(s1)))
s1 = s1.replace('e', str(len(s1) + 1))
s1 = s1.replace('i', str(len(s1) + 2))
s1 = s1.replace('o', str(len(s1) + 3))
s1 = s1.replace('u', str(len(s1) + 4))

print 'the encrypted sentece is: %s ' % s1

s1 = s1.replace(str(len(s1)), 'a')
s1 = s1.replace(str(len(s1) + 1), 'e')
s1 = s1.replace(str(len(s1) + 2), 'i')
s1 = s1.replace(str(len(s1) + 3), 'o')
s1 = s1.replace(str(len(s1) + 4), 'u')

print 'the decrypted sentence is: ' + s1