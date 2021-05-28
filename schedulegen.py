#!/usr/bin/env python3
"""Convert a text schedule into a personal information manager (e.g. google calander) friendly iCal format.

Original author: Chris Faesi (@cfaesi)
Modified by: Mike Zevin (@michaelzevin), Jenny Calahan (@jkcalahan), Nathan Sanders (@nesanders)
"""

import datetime
import os
import string

#############################################
## INPUT PARAMETERS
#############################################
infile: str = 'example_schedule.txt' # input txt filename
outfile: str = 'example_schedule.ics' # output iCal filename
startdate: datetime.datetime = datetime.datetime(2021,5,25)  # year, month, date
repeats: int = 1 # number of times to add events
starttime: str = 'T060000' # time of day to place each event on calendar
endtime: str = 'T080000' # end time of day for each event

#############################################
## Execution
#############################################
oneday = datetime.timedelta(days=1)
curdate = startdate
g = open(outfile, 'w')
# header
g.write('BEGIN:VCALENDAR\n')
g.write('BEGIN:VTIMEZONE\n')
g.write('TZID:America/New_York\n')
g.write('BEGIN:DAYLIGHT\n')
g.write('TZOFFSETFROM:-0500\n')
g.write('DTSTART:20070311T020000\n')
g.write('TZNAME:EDT\n')
g.write('TZOFFSETTO:-0400\n')
g.write('END:DAYLIGHT\n')
g.write('BEGIN:STANDARD\n')
g.write('TZOFFSETFROM:-0400\n')
g.write('TZNAME:EST\n')
g.write('TZOFFSETTO:-0500\n')
g.write('END:STANDARD\n')
g.write('END:VTIMEZONE\n')
g.write('X-WR-CALNAME:Astrobites schedule\n')
# repeat the specified number of times
for i in range(repeats):
  # step through input file
  f=open(infile,'r')
  for line in f:
    # read in event
    title=line.split()[2]+' '+line.split()[3]
    # write to output
    g.write('BEGIN:VEVENT\n')
    g.write('DTSTART;TZID=America/New_York:'+str(curdate.year)+str(curdate.month).zfill(2)+str(curdate.day).zfill(2)+starttime+'\n')
    g.write('DTEND;TZID=America/New_York:'+str(curdate.year)+str(curdate.month).zfill(2)+str(curdate.day).zfill(2)+endtime+'\n')
    g.write('SUMMARY:'+title+'\n')
    g.write('END:VEVENT\n')
    # advance clock
    curdate=curdate+oneday
  f.close()
#  EOF
g.write('END:VCALENDAR')
g.close()
