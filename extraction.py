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
    if(user[category] == 'Not Going'):
        return 0
    else:
        user[category] = user[category].split(",")
    if(category in driverDict):
        #If category exists
        for subTimes in user[category]:
            if subTimes not in driverDict[category]:
                #create a new subTime if none exists
                driverDict[category][subTimes] = [user["Name"]]
            else: 
                #append to existing subTime 
                driverDict[category][subTimes].append(user["Name"])
    else: 
        #If category doesn't exists
        subTimeDict ={}
        for subTimes in user[category]:
            subTimeDict[subTimes] = [user["Name"]]
        driverDict[category] = subTimeDict


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
            if 'What is your carry capacity?' in user.keys():
                # Drivers
                addDrivers(category, typeDict, user)
            else:
                # Riders
                addRiders(category, typeDict, user)

        #print(user)
