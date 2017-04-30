# Programmer: Hayden Archambault
# Program: Weather.py
# Version: 1.0
# Program Description: Allows the user to enter
# a location and find out the current weather.

import urllib2
import json
import Epic
import sys,time,random

for letter in str("Lets check the weather!\n"):
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(.04)

while True:
    location = Epic.userString("Enter location: ")
    url = 'https://api.apixu.com/v1/forecast.json?key=d2b10c2e93fe4ad984d25256172404&q=' + location

    jsonTxt = urllib2.urlopen(url).read()
    data = json.loads(jsonTxt)
    
    choice = Epic.userString("Would you like results in Farenheight or Celsius (f or c)? ")

    for letter in str("\nHere is the current weather for %s, %s\n" % (data['location']['name'], data['location']['region'])):
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(.04)
    
    if choice == 'f':        
        print "%s and %s degrees (F)" % (data['current']['condition']['text'], data['current']['temp_f'])
        print "It actually feels like %s degrees (F)" % (data['current']['feelslike_f'])
        print "This information was last updated on %s" % data['current']['last_updated']
    if choice == 'c':
        print "%s and %s degrees (C)" % (data['current']['condition']['text'], data['current']['temp_c'])
        print "It actually feels like %s degrees (C)" % (data['current']['feelslike_c'])
        print "This information was last updated on %s" % data['current']['last_updated']
        
    again = Epic.userString("\nWant to check another location (y/n)? ")
    if again == 'n':
        for letter in str('Come back anytime to check the weather!'):
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(.04)
        break