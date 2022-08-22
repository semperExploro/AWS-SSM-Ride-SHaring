import csv
from lib2to3.pgen2 import driver

RIDER_CSV_FILE = 'riders.csv'
DRIVER_CSV_FILE = 'drivers.csv'

def readRidersCSVFile(csvFileName):
    userInformation = []
    with open(csvFileName, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            userInformation.append(row)
    return userInformation


def addDrivers(category, driverDict, user):
    # Drivers
    if (user[category] == 'Not Going'):
        dud = 0
    elif (category in driverDict):
        # append if already exists
        driverDict[category][user[category]].append(
            user["Name"])
    else:
        # otherwise create a new event
        subTimes = [user[category]]
        if "," in user[category]:
            subTimes = user[category].split(",")
        for subTime in subTimes:
            #print(subTime)
            eventDictionary = {}
            eventDictionary[subTime
                            ] = [user["Name"]+"," + user['What is your carry capacity?']]
            driverDict[category] = eventDictionary


def addRiders(category, ridersDict, user):
    # Drivers
    #print(userInformation)
    if (user[category] == 'Not Going'):
        dud = 0
    elif (category in ridersDict):
        # append if already exists
        ridersDict[category][user[category]].append(
            user["Name"])
    else:
        # otherwise create a new event
        eventDictionary = {}
        eventDictionary[user[category]
                        ] = [user["Name"]]
        ridersDict[category] = eventDictionary


def compileDictionary(userInformation, typeDict):
    for user in userInformation:

        for category in user:
            # print(driverDict)

            if category == 'Timestamp' or category == 'Email Address' or category == 'Name' or category == 'What is your carry capacity?':
                continue
            if 'What is your carry capacity?' in user:
                # Drivers
                addDrivers(category, typeDict, user)
            else:
                # Riders
                addRiders(category, typeDict, user)


def lambda_handler():
    riderInformation = readRidersCSVFile(RIDER_CSV_FILE)
    driverInformation = readRidersCSVFile(DRIVER_CSV_FILE)
    driverDict = {}
    riderDict = {}

    print(driverInformation)

    #print(userInformation)
    compileDictionary(driverInformation, driverDict)
    #print(driverDict)
    compileDictionary(riderInformation, riderDict)
    #print(riderDict)


if __name__ == '__main__':
    lambda_handler()
