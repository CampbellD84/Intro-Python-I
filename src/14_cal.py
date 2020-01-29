"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime


curr_date = datetime.now()
clndr = calendar.TextCalendar()
arg = sys.argv


def numCheck(arg):
    if arg.isdigit():
        return int(arg)
    else:
        return False


if (len(arg) == False):
    print('Looking for input in thr form of: "year(optional), month')
    exit()


mnth = len(arg) > 1 and numCheck(arg[1]) or curr_date.month
year = len(arg) > 2 and numCheck(arg[2]) or curr_date.year

# No Args
clndr.prmonth(year, mnth)

# One arg (Month)
clndr.prmonth(year, 7)

# Two Args
clndr.prmonth(2020, 9)
