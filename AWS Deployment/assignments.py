
from collections import OrderedDict
import operator


def getMasterRidesList(riderDict):
    masterRidesList = {}
    masterRidesCount = {}
    for date in riderDict:
        for subTime in riderDict[date]:
            masterRidesList[date+","+subTime] = riderDict[date][subTime]
            masterRidesCount[date+","+subTime] = len(riderDict[date][subTime])
    return masterRidesList,masterRidesCount

def sortDriversCapacity(driverDict):
    for date in driverDict:
        for subTime in driverDict[date]:
            driverSets = driverDict[date][subTime]
            sortedDriverSets = sorted(
                driverSets,
                key=lambda t: t[1],
                reverse = True
            )
            driverDict[date][subTime] = sortedDriverSets

def assignRidersToDrivers(masterRide, masterCount, driverDict):
    finalList = {}
    while(len(masterCount)!=0):
        masterCount = dict(sortDictionaryByValue(masterCount))
        date = list(masterCount.items())[-1][0]
        day = date.split(",")[0]
        time = date.split(",")[1]
        if(day not in driverDict or time not in driverDict[day]):
            #UBER - the day or the day and time cannot be find 
            uberConfig(masterCount,date,finalList,masterRide)
        else: 
            driverData = driverDict[day][time][0]
            driverName = driverData[0]
            driverCapcity = int(driverData[1])
            masterRide[date]
            if date in finalList:
                #if there's already existing date
                if(masterCount[date]>driverCapcity):
                    #more than four people per in the car
                    finalList[date].append(((masterRide[date][0:driverCapcity]),driverName))
                    masterCount[date] = masterCount[date]-driverCapcity
                    del masterRide[date][0:driverCapcity]

                else:
                    #less than four people per in the car 
                    finalList[date].append(((masterRide[date][0:len(masterRide[date])]),driverName))
                    masterCount[date] = masterCount[date]-len(masterRide[date])
                    del masterRide[date][0:len(masterRide[date])]

            else:
                #if there isn't an existing driver
                if(masterCount[date]>driverCapcity):
                    #more than four people per in the car
                    finalList[date]=[((masterRide[date][0:4]),driverName)]
                    masterCount[date] = masterCount[date]-driverCapcity
                    del masterRide[date][0:driverCapcity]

                else:
                    #less than four people in the car 
                    finalList[date]=[((masterRide[date][0:len(masterRide[date])]),driverName)]
                    masterCount[date] = masterCount[date]-len(masterRide[date])
                    del masterRide[date][0:len(masterRide[date])]
            #driverDict[day][time].remove(driverData)
            removeDriver(driverDict,day,driverData)

        #delete empty dates
        if((masterCount[date])==0):
            masterCount.pop(date,None)
        if(len(masterRide[date])==0):
            masterRide.pop(date,None)
    return finalList

def removeDriver(driverDict,day,driverData):
    for sets in list(driverDict[day].keys()):
        if driverData in driverDict[day][sets]:
            driverDict[day][sets].remove(driverData)
        if(len(driverDict[day][sets]) == 0):
            del driverDict[day][sets]
    if(len(driverDict[day])==0):
        del driverDict[day]



def uberConfig(masterCount,date,finalList,masterRide):
    if date in finalList:
        #if there's already existing ubers
        if(masterCount[date]>4):
            #more than four people per uber
            finalList[date].append(((masterRide[date][0:4]),"UBER"))
            masterCount[date] = masterCount[date]-4
            del masterRide[date][0:4]
        else:
            #less than four people per uber 
            finalList[date].append(((masterRide[date][0:len(masterRide[date])]),"UBER"))
            masterCount[date] = masterCount[date]-len(masterRide[date])
            del masterRide[date][0:len(masterRide[date])]
    else:
        #if there isn't an existing uber
        if(masterCount[date]>4):
            #more than four people per uber
            finalList[date]=[((masterRide[date][0:4]),"UBER")]
            masterCount[date] = masterCount[date]-4
            del masterRide[date][0:4]
        else:
            #less than four people per uber 
            finalList[date]=[((masterRide[date][0:len(masterRide[date])]),"UBER")]
            masterCount[date] = masterCount[date]-len(masterRide[date])
            del masterRide[date][0:len(masterRide[date])]


def sortDictionaryByValue(dict1):
    sorted_tuples = sorted(dict1.items(), key=operator.itemgetter(1))
    sorted_dict = OrderedDict()
    for k, v in sorted_tuples:
        sorted_dict[k] = v
    return sorted_dict