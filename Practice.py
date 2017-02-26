#import Epic

def main():
    print 'Here are all the ways I can araange the number 1, 2, 3'
    r = range(1, 4)   #up to but not including 4  so 1 2 and 3
    for a in r:
        for b in r:
            for c in r:
                print '%s%s%s' % (a, b, c)
main()