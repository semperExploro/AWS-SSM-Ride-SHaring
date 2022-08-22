import csv


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
    if (user[category] == 'Not Going'):
        return 0
    else:
        user[category] = user[category].split(",")
    if (category in driverDict):
        # If category exists
        for subTimes in user[category]:
            if subTimes not in driverDict[category]:
                # create a new subTime if none exists
                driverDict[category][subTimes] = [
                    (user["Name"], user['What is your carry capacity?'])]
            else:
                # append to existing subTime
                driverDict[category][subTimes].append((
                    user["Name"], user['What is your carry capacity?']))
    else:
        # If category doesn't exists
        subTimeDict = {}
        for subTimes in user[category]:
            subTimeDict[subTimes] = [
                (user["Name"], user['What is your carry capacity?'])]
        driverDict[category] = subTimeDict


def addRiders(category, ridersDict, user):
    # print(user)
    if (user[category] == 'Not Going'):
        dud = 0
    elif category not in ridersDict:
        #print("Category not added "+category)
        entry = {}
        entry[user[category]] = [user["Name"]]
        ridersDict[category] = entry
        # print(ridersDict)
    elif user[category] not in ridersDict[category]:
        ridersDict[category][user[category]] = [user["Name"]]
    else:
        ridersDict[category][user[category]].append(user["Name"])


def compileDictionary(userInformation, typeDict):
    for user in userInformation:

        for category in user:

            if category == 'Timestamp' or category == 'Email' or category == 'Name' or category == 'What is your carry capacity?':

                continue
            if 'What is your carry capacity?' in user.keys():
                # Drivers
                addDrivers(category, typeDict, user)
            else:
                # Riders
                addRiders(category, typeDict, user)

        # print(user)
