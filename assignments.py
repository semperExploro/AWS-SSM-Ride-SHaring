
from doctest import master


def getMasterRidesList(riderDict):
    masterRidesList = {}
    for date in riderDict:
        for subTime in riderDict:
            masterRidesList[date+" "+subTime] = riderDict[subTime]
    return masterRidesList

