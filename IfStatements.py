import Epic

sentence = Epic.userString("Please enter a sentence: ")
words = sentence.split(' ')  #creates a list
largeWords = []
medWords = []
smallWords = []

for word in words:
    if len(word) > 5:
        largeWords.append(word)  # if bigger than 3, store word in largeWords
    elif len(word) > 3:
        medWords.append(word)
    else:
        smallWords.append(word)
        
print largeWords
print medWords
print smallWords