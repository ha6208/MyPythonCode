import Epic

kmWeekday = Epic.userInt('How many km have you traveled on a weekday?')
kmWeekend = Epic.userInt('How many km have you traveled on a weekend?')
miWeekday = Epic.kmToMi(kmWeekday)
miWeekend = Epic.kmToMi(kmWeekend)

dollarsWeekday = miWeekday * 0.13;
dollarsWeekend = miWeekend * 0.24;

print 'Weekday $%.2f' % dollarsWeekday
print 'Weekend $%.2f' % dollarsWeekend
print 'Total $%.2f' % (dollarsWeekday + dollarsWeekend)