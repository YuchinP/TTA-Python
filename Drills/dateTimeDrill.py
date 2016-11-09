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

##Modules
import datetime
from datetime import *
import pytz
from pytz import *

##Compares the current hour of the branch to whether or not they fit in the open range
def is_it_closed(x):
    if branch_open <= x and x <= branch_close:
        print ('This Location is Open!')
    else:
        print('This Location is Closed!')

##Defines the hours the branches are open and closed
branch_close = time(hour=22,minute=0,second=0)
branch_open = time(hour=9,minute=0,second=0)        

##Defines the 3 timezones that are going to be used
utc_time = datetime.utcnow()
tz = timezone('America/Los_Angeles')
etz = timezone('America/New_York')
ltz = timezone('Europe/London')

##Converts the general UTC time to the correct timezone needed
P = pytz.utc.localize(utc_time).astimezone(tz)
NY = pytz.utc.localize(utc_time).astimezone(etz)
LON = pytz.utc.localize(utc_time).astimezone(ltz)

##Converts the datetime objects to time types
Portland = time(hour = P.hour) 
New_York = time(hour = NY.hour)
London = time(hour = LON.hour)

##Printing and determinations of the branches
print('Portland Date and time: ', P)
is_it_closed(Portland)
print('New York Date and time: ', NY)
is_it_closed(New_York)
print('London Date and time: ', LON)
is_it_closed(London)





