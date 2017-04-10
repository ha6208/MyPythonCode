import json
import Epic

def main():
    jsonTxt = ""
    f = open('contacts.json')
    for line in f:
        line = line.strip()
        jsonTxt = jsonTxt + line
    contacts = json.loads(jsonTxt)
    
    name = Epic.userString("Enter a name: ")
    for contact in contacts:
        if contact["Name"] == name:
            print "%s - %s" % (contact["Email"], contact["Phone"])