import time
import datetime
from datetime import timedelta


def duedate():
    year = int(input("enter a due date year: "))
    month = int(input("enter the month: "))
    day = int(input('enter the day: '))
    hour = int(input('enter the hour: '))
    duedate = datetime.datetime(year, month, day, hour,00)
    return duedate




def timeremain():
    start = datetime.datetime.today()
    delta = duedate()-start
    print(delta)
