# Programmer: Hayden Archambault
# Version: 1.1
# Program Description: This program asks the user to enter to four verses, a chorus, and how many times to repeat the chorus.
# The song is then organised and printed out

import Epic

song = ['first verse', 'second verse', 'third verse', 'fourth verse']
csong = []

# this loop gets the user input for the four verses
for part in song:
    complete = Epic.userString('Enter the %s: ' % part)
    csong.append(complete)  

# makes every verse upper case
csong[:] = [item.upper() for item in csong]    

chorus = raw_input('Enter the chorus: ').lower()  # makes the chorus lower case
chorus = chorus + ' '

# rep is the amount of times to repeat
rep = int(raw_input('Enter the chorus repeat: '))

csong.insert(1, (chorus*rep))
csong.insert(3, (chorus*rep))
csong.insert(5, (chorus*rep))
csong.insert(7, (chorus*(rep+1)))

repeat = '...one more time!...'
csong = csong * 2
csong.insert(8, repeat)
print csong

csong[:] = [item.replace('COOKIES', '_______') for item in csong]

print
# prints the final song for the user
for verse in csong:
    print verse