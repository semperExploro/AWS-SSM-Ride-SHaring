import csv
from lib2to3.pgen2 import driver

CSV_FILE = 'rides.csv'
DRIVER_QUESTION = "DRIVERS ONLY - If you're a driver, please indicate how many students you can carry"


def readCSVFile():
    userInformation = []
    with open(CSV_FILE, newline='') as csvfile:
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
        eventDictionary = {}
        eventDictionary[user[category]
                        ] = [user["Name"]+"," + user[DRIVER_QUESTION]]
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
                        ] = [user["Name"]+"," + user[DRIVER_QUESTION]]
        ridersDict[category] = eventDictionary


def compileDictionary(userInformation, ridersDict, driverDict):
    for user in userInformation:

        for category in user:
            # print(driverDict)

            if category == 'Timestamp' or category == 'Email Address' or category == 'Name' or category == DRIVER_QUESTION:
                continue
            if user[DRIVER_QUESTION] != '':
                # Drivers
                addDrivers(category, driverDict, user)
            else:
                # Riders
                addRiders(category, ridersDict, user)


def lambda_handler():
    userInformation = readCSVFile()
    userDict = {}
    driverDict = {}
    riderDict = {}
    #print(userInformation)
    compileDictionary(userInformation, userDict, driverDict)
    print(driverDict)
    compileDictionary(userInformation, riderDict, driverDict)
    print(userDict)


if __name__ == '__main__':
    lambda_handler()
