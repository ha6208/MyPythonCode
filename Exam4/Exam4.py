# Programmer: Hayden Archambault
# Program: Exam4.py
# Version: 1.0
# Program Description: Allows the user to enter a search term.
# If it is found, it is shown next to the file it was located in
# and tells how many times it was found.

import os

# function that organizes the files used into a dictionary
def createFiles(files):
    d = {}
    for item in files:
        l = []
        for line in open(item):
            line = line.strip().upper()
            l.append(line)
        d[item] = l
    return d

# function used to find the term entered by user
# also prints out the number that term was found
def findWord(s, data):
    count = 0
    answer = []
    
    for item in data:
        for line in data[item]:
            if s in line:
                count += 1
                answer.append(item + ': ' + line)
    print 'That term was found %s times.' % count
    return answer

# main function
def main():
    files = os.listdir(".")
    files = [x for x in files if '.txt' in x]
    data = createFiles(files)
    
    # obtain term from user
    print 'Please enter a search term: ',
    s = raw_input().upper()
    
    answer = findWord(s, data)
    
    # print out results for the user
    for found in answer:
        print found

main()