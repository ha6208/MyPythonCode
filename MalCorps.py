print 'how many malcorps did you find on planet exflon? ',
exfl = raw_input()
print 'how many malcorps did you find on planet mobiles? ',
mobi = raw_input()
print 'how many malcorps did you find on planet monsantoes? ',
mons = raw_input()

total = int(exfl) + int(mobi) + int(mons)
print 'you found %s malcorps!' % total
print 'the average malcorps per planet is %.2f' % (total / 3.0)