##Python Ver: 3.4.4
##Author: Yuchin Pan
##Item 58 Python Course

##Scenario: The company you work for just opened two new branches. One is in New York City,
##the other in London. They need a very simple program to find out if the branches are open or
##closed based on the current time of the Headquarters here in Portland. The hours of both
##branches are 9:00AM - 9:00PM in their own time zone.
##What is asked of you:
##Create code that will use the current time of the Portland HQ to find out the time in the NYC &
##London branches, then compare that time with the branches hours to see if they are open or
##closed.
##Print out if each of the two branches are open or closed.

from datetime import datetime
from time import strftime

##Currently in Tuples need it to not be so it can be adjusted. At least the Time Portion needs to be seperated and changed
format = "%a %b %d %Y %I:%M:%S %p"
s = datetime.now().strftime(format)
print ('Portland Date/Time:', s)
print (s)

#print ('Portland Date and Time: ', datetime.now(s))
#print ('New York Date and Time: ', (datetime.now()+3:00:00))
