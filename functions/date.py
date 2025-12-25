# framework example
# this library code returns the time data as either a time or a date
import datetime

def date(datetype):
  if datetype == "clock":
    return datetime.datetime.now().strftime("%H:%M:%S.%f")
  elif datetype == "date":
    return datetime.datetime.now().strftime("%d-%m-%Y")
