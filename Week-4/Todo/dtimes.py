import time
import datetime
from datetime import timedelta

def duedate():
    duedatestring = input('Enter the date (yyyy-mm-dd): ')
    duehourstring = input('Enter the date (hh:mm): ') + ":00"
    duedate = duedatestring + ' ' + duehourstring
    return duedate




def timeremain():
    start = datetime.datetime.today()
    delta = duedate()-start
    print(delta)
