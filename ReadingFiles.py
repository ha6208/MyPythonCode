file = open('Matisse.txt', 'r')  # assumes same directory,  'r' means just for reading

discarded = []

for line in file:
    words = line.split(" ")
    for word in words:
        temp = word.replace(",", "")
        temp = temp.replace(".", "")  #temp becomes word, without the commas or periods
        if len(temp) == 4:
            discarded.append(temp)
        else:
            print word + " ",  # must replace spaces that split took out  OR NOT?????

print "\n\nDiscarded words: %s" % discarded