import csv
import boto3


RIDER_CSV_FILE = 'riders.csv'
DRIVER_CSV_FILE = 'drivers.csv'
BUCKET_NAME = 'bucket-name'

def getCSV(key):
    bucket = BUCKET_NAME
    s3_resource = boto3.resource('s3')
    s3_object = s3_resource.Object(bucket, key)
    data = s3_object.get()['Body'].read().decode('utf-8').splitlines()
    lines = csv.reader(data)
    return lines

def getCSVHeaders(fileName):

    # creating an object of csv reader
    # with the delimiter as ,
    csv_reader = getCSV(fileName)
    list_of_column_names = next(csv_reader)
    return list_of_column_names

def readRidersCSVFile(csvFileName,headers):
    print(headers)
    userInformation = []
    csv_reader = getCSV(csvFileName)
    for line in csv_reader:
        if line ==headers:
            continue
        dict = {}
        for i in range(len(line)):
            dict[headers[i]]=line[i]
        userInformation.append(dict)
    print(userInformation)
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
    if (user[category] == 'Not Going'):
        dud = 0
    elif category not in ridersDict:
        entry = {}
        entry[user[category]] = [user["Name"]]
        ridersDict[category] = entry
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

