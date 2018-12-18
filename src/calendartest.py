import datetime

def main():
    event = datetime.datetime.strftime(input(" Welcome to the ACE Calendar. Please enter the date of you event separated with % (%YYYY%MM%DD). For example, if your event is on January 2, 2019 you would enter %2019%01%02: "), '%Y%m%d')
    #event = datetime.datetime.strptime(date, '%Y%m%d')
    today = datetime.datetime.today().date()
    print(today)
    here = input(" now here")
    away = (event - today).days
    print(away)


class Event:
    """This class creates the ability to create events with a name, date, and priority."""
    def __init__(self, userID, event_name, date, priority, status):
        self.userID = userID #string
        self.ename = event_name #string
        self.date = date #string
        self.priority = priority #int
        self.status = status #string
    #end of __init__()
#end of class


def getToday():
    """returns today's data in yyyy-mm-dd format"""
    today = int(date.today()) #time.datetime.today().strftime('%Y-%m-%d') # On one line. Is a string
    print(today)
    yyyy = int(today[0:4])
    mm = int(today[5:7])
    dd = int(today[8:10])
    today = datetime.date(yyyy,mm,dd) #todays date
    return today
    #end of getToday()

main()
