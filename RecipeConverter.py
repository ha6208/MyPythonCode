# Programmer: Hayden Archambault
# Date: 1/21/17
# Program Details: Converts the original recipe provided by the user and modifies it accordingly 
# depending on adjustment factor. Also shows the modified recipe in grams.

print "-- Original Recipe --"
print "Enter the amount of Flour (cups): ",
flour = raw_input()
print "Enter the amount of water (cups): ",
water = raw_input()
print "Enter the amount of salt (teaspoons): ",
salt = raw_input()
print "Enter the amount of yeast (teaspoons): ",
yeast = raw_input()

print "Enter the loaf adjustment factor (e.g. 2.0 double the size): ",
adj = raw_input()
nflour = float(flour) * float(adj)
nwater = float(water) * float(adj)
nsalt = float(salt) * float(adj)
nyeast = float(yeast) * float(adj)

print '\n-- Modified Recipe --'
print 'BreadFlour: %.2f cups.' % float(nflour)
print 'Water: %.2f cups.' % float(nwater)
print 'Salt: %.2f teaspoons.' % float(nsalt)
print 'Yeast %.2f teaspoons.' % float(nyeast)
print 'Happy Baking!'

# avoiding magic numbers
flourgrams = 120
watergrams = 237
saltgrams = 5
yeastgrams = 3

print '\n-- Modified Recipe in Grams --'
print 'BreadFlour: %.2f g.' % (float(nflour) * flourgrams)
print 'Water: %.2f g.' % (float(nwater) * watergrams)
print 'Salt: %.2f g.' % (float(nsalt) * saltgrams)
print 'Yeast %.2f g.' % (float(nyeast) * yeastgrams)
print 'Happy Baking!'