import Epic

words = ['cat', 'dog', 'apple', 'house', 'chicken']
lengths = []

for word in words:
    l = len(word)
    lengths.append(l)
    
print 'here are the lengths %s' % lengths