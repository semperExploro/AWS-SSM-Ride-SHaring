from email import header
from extraction import*
from assignments import* 
from parseToCsv import*



def lambda_handler(event,context):
    #Extract Information
    riderHeaders = getCSVHeaders(RIDER_CSV_FILE)
    driverHeaders = getCSVHeaders(DRIVER_CSV_FILE)
    riderInformation = readRidersCSVFile(RIDER_CSV_FILE,riderHeaders)
    driverInformation = readRidersCSVFile(DRIVER_CSV_FILE,driverHeaders)
    
    headers = riderHeaders
    del headers[0:3]

    #Assign Riders to Dictionaries
    driverDict = {}
    riderDict = {}
    compileDictionary(driverInformation, driverDict)
    sortDriversCapacity(driverDict)
    compileDictionary(riderInformation, riderDict)
    
    #Configure for Ride Assignment
    masterRides, masterCount = getMasterRidesList(riderDict)
    finalList = assignRidersToDrivers(masterRides,masterCount,driverDict)

    #Print to CSV
    morning = headers[0:int(len(headers)/2)]
    afternoon = headers[int(len(headers)/2):len(headers)]
   
    convertDictToCSV(finalList,morning,afternoon)


if __name__ == '__main__':
    lambda_handler()
