import Epic

# if height is < 54 or age < 14 cannot ride
# if height == 54 and age == 14 ask attendant
# if height > 54 and age > 14 can ride

height = Epic.userInt("Please enter your height in inches: ")
age = Epic.userInt("Please enter your age: ")

canRide = height > 54 and age > 14   # will return either a true or false, will be stored in canRide
notRide = height < 54 or age < 14  # notice the 'or' and 'and' operators
ask = height == 54 and age == 14   #  these expressions can all be put into the if statements 

if canRide:    #same as    if canRide == True:
    print "You can ride!"
elif notRide:
    print "You cannot ride!"
elif ask:
    print "You must ask!"

# boolean expression  
# not (x and y)