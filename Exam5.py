# Programmer: Hayden Archambault
# Program: Exam5.py
# Version: 1.0
# Program Description: Allows the user to search a json
# file for specific information. The search can be done
# by category or keyword.

import json
import Epic

# this function opens and reads a json file
def readFile(name):
    jsonTxt = ""
    f = open(name)
    for line in f:
        line = line.strip()
        jsonTxt = jsonTxt + line
    return jsonTxt

# if the user wants to search by category, this function is called
# search is not case sensitive
def catSearch(files):
    category = Epic.userString("Enter a category: ").lower()
    for file in files:
        if file["Category"].lower() == category:
            print "%s - %s" % (file["Product"], file["Price"])

# if the user wants to search by keyword, this function is called
# search is not case sensitive
def keySearch(files):
    keyword = Epic.userString("Enter a keyword: ").lower()
    for file in files:
        if keyword in file["Product"].lower():
            print "%s - %s" % (file["Product"], file["Price"])

# main function
# calls function to read specified json file
# asks for initial user input which determines what search function will be called
def main():
    txt = readFile('PetStore.json')
    files = json.loads(txt)
    
    search = Epic.userString("Search by category (c) or keyword (k): ")
    if search == "c":
        catSearch(files)
    if search == "k":
        keySearch(files)

main()