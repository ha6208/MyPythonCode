import Epic

ratings = []
flavors = ['vanilla', 'chocolate', 'strawberry', 'bacon']

for flavor in flavors:
    rating = Epic.userString('Rate %s from 1 to 5: ' % flavor)
    ratings.append('%s rated as a %s' % (flavor, rating))
    
print ratings