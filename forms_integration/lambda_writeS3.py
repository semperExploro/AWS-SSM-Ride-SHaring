import os.path
import json
import ast
from writeS3_dates import getDate
from lambda_deposit_queue import lambda_handler

# CONSTANTS
dict = {'Information': 'jonathany330@gmail.comJoe Shmo', 'Sunday Services - Arrival': 'Early - 8:10 AMEarly - 8:10 AMEarly - 8:10 AMEarly - 8:10 AM', 'Sunday Services- Departures': 'After service - 11:00 PMAfter service - 11:00 PMAfter service - 11:00 PMAfter service - 11:00 PM'}
DRIVERSFILE = "drivers.txt"
RIDERSFILE = "riders.txt"


def formatDriverDictionary(dict, monthNum):
    # create table
    # if the file doesn't exist, use S3
    print("File status "+str(os.path.exists(DRIVERSFILE)))
    fileData = ""
    rawDictionary = {}
    #read file information into string buffer
    if (os.path.exists(DRIVERSFILE)):
        pointer = open(DRIVERSFILE, "r")
        fileList = pointer.readlines()
        fileData = format(fileList)
        rawDictionary = ast.literal_eval(fileData)
        pointer.close()
        
    #existing Dictionary
    
    #deposit function
    userDictionary = {}
    pointer = open(DRIVERSFILE, "w")
    formatDictionaryDriverDeposit(dict, userDictionary, monthNum)
    addToDictionary(userDictionary,rawDictionary)

    #print(rawDictionary)
    pointer.write(json.dumps(rawDictionary))
    pointer.close()

def formatRidersDictionary(dict, monthNum):
    # create table
    # if the file doesn't exist, use S3
    #print("File status "+str(os.path.exists(DRIVERSFILE)))
    fileData = ""
    rawDictionary = {}
    #read file information into string buffer
    if (os.path.exists(RIDERSFILE)):
        pointer = open(RIDERSFILE, "r")
        fileList = pointer.readlines()
        fileData = format(fileList)
        rawDictionary = ast.literal_eval(fileData)
        pointer.close()
        
    #existing Dictionary
    
    #deposit function
    userDictionary = {}
    pointer = open(RIDERSFILE, "w")
    formatDictionaryRiderDeposit(dict, userDictionary, monthNum)
    addToDictionary(userDictionary,rawDictionary)

    #print(rawDictionary)
    pointer.write(json.dumps(rawDictionary))
    pointer.close()


def addToDictionary(userSet, rideDictionary):
    for key in userSet:
        if key == 'Driver Information':
            continue
        if key in rideDictionary:
            rideDictionary[key].append(userSet[key][0])
        else:
            rideDictionary[key] = userSet[key]
    

def formatDictionaryRiderDeposit(dict, set, monthNum):
    for key in dict:
        index = 0
        if (key == "Information" or key == "Driver Information"):
            continue
        if ("AM" in dict[key]):
            output = dict[key].replace("AM", "AM,")
        else:
            output = dict[key].replace("PM", "PM,")
        keys = output.split(',')
        keys.pop()
        for element in keys:
            set[element +" "+ monthNum[index]] = [dict["Information"]]
            index = index+1


def formatDictionaryDriverDeposit(dict, set, monthNum):
    for key in dict:
        index = 0
        if (key == "Information" or key == "Driver Information"):
            continue
        if ("AM" in dict[key]):
            output = dict[key].replace("AM", "AM,")
        else:
            output = dict[key].replace("PM", "PM,")
        keys = output.split(',')
        keys.pop()
        for element in keys:
            set[element +" "+ monthNum[index]] = [dict["Information"]+" "+dict["Driver Information"]]
            index = index+1

def format(lines):
    string = ""
    for element in lines:
        string = string + element
    string.replace("\n","")
    return string

def lambda_handler(event, context):
    monthNum = (getDate())
    filter_dictionary(dict)
    #print(dict)
    if( 'Driver Information' in dict):
        formatDriverDictionary(dict, monthNum)
    else:
        formatRidersDictionary(dict,monthNum)

def filter_dictionary(dict):
    output = dict['Information']
    foundAt = False
    for i in range(len(output)):
        if(output[i:(i+1)] == '@'):
            foundAt = True
        if(foundAt and output[i:i+1] == '.'):
            name = output[i+4:len(output)]
    dict['Information'] = name

if __name__ == '__main__':
    lambda_handler("bob", "ross")
