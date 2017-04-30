# Exam6.py
# Programmer: Hayden Archambault
# Description: Helps you cheat at Clue!
# this version ignores case

import Epic

# function that determines the clue from user
# finds whther it is a weapon or suspect
# asks for the weapon/suspect and removes it from the list
# when there is only one possibilty left, it tells you who did it
def loop(suspects, weapons):
    while((len(suspects) * len(weapons)) != 1):
        clue = Epic.userString("Is the clue about a weapon or a suspect (w or s)?")
        if clue == "w":
            weaponNotUsed = Epic.userString("Enter the weapon not used %s: " % (weapons)).lower()
            if weaponNotUsed in weapons:
                weapons.remove(weaponNotUsed)
            else:
                print "That weapon does not exist."
        elif clue == "s":
            innocentSuspect = Epic.userString("Enter the innocent suspect %s: " % (suspects)).lower()
            if innocentSuspect in suspects:
                suspects.remove(innocentSuspect)
            else:
                print "That suspect does does not exist."
        print "%s possiblities left." % ((len(suspects) * len(weapons)))
        if((len(suspects) * len(weapons)) == 1):
            print "It was %s with a %s!" % ("".join(suspects), ", ".join(weapons))

# main loop
# initialize suspects and then make them lower case
# for case insensitivity
def main():
    suspects = ["Miss Scarlet", "Col Mustard", "Mr Green"]
    weapons = ["Candlestick", "Wrench", "Pipe"]
    
    # only way I could ignore case, but at the cost of everything being lower case
    suspects = [x.lower() for x in suspects]
    weapons = [x.lower() for x in weapons]
    
    print "%s possiblities left." % ((len(suspects) * len(weapons)))
    
    loop(suspects, weapons)
    
main()