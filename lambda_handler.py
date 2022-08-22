from extraction import*
from assignments import* 

def lambda_handler():
    #Extract Information
    riderInformation = readRidersCSVFile(RIDER_CSV_FILE)
    driverInformation = readRidersCSVFile(DRIVER_CSV_FILE)
    #print(driverInformation)
    #Assign Riders to Dictionaries
    driverDict = {}
    riderDict = {}
    compileDictionary(driverInformation, driverDict)
    sortDriversCapacity(driverDict)
    compileDictionary(riderInformation, riderDict)
    
    #print(driverDict)
    #Configure for Ride Assignment
    masterRides, masterCount = getMasterRidesList(riderDict)
    #print("Master Rides")
    #print(masterRides)
    #print("Master Count")
    #print(masterCount)
    #print("Driver Dictionary")
    #print(driverDict)

    finalList = assignRidersToDrivers(masterRides,masterCount,driverDict)
    print(finalList)

if __name__ == '__main__':
    lambda_handler()
