from datetime import date, timedelta

def allsundays(year, month, day):
    d = date(year, month, day)                    # January 1st
    d += timedelta(days=6 - d.weekday())  # First Sunday
    while d.month == month:
        yield d
        d += timedelta(days=7)


def getDate():
    today = str(date.today())
    rawStrings = today.split("-")
    dateNums = []
    for element in rawStrings:
        dateNums.append(int(element))
    dates = []
    for d in allsundays(dateNums[0], dateNums[1]+1, 1):
        dates.append(str(d))
    return dates
