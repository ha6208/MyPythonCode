import json
import Epic

def main():
    jsonTxt = ""
    f = open('classMcla.json')
    for line in f:
        line = line.strip()
        jsonTxt = jsonTxt + line
    files = json.loads(jsonTxt)
    
    name = Epic.userString("Enter a name: ")
    for file in files:
        if file["ProfName"] == name:
            print "%s" % file["Class"]
            for location in file["Location"]:
                print location

main()