from extraction import*
from assignments import* 

def lambda_handler():
    #Extract Information
    riderInformation = readRidersCSVFile(RIDER_CSV_FILE)
    driverInformation = readRidersCSVFile(DRIVER_CSV_FILE)

    #Assign Riders to Dictionaries
    driverDict = {}
    riderDict = {}
    compileDictionary(driverInformation, driverDict)
    compileDictionary(riderInformation, riderDict)

    #Configure for Ride Assignment
    getMasterRidesList(riderDict)

if __name__ == '__main__':
    lambda_handler()
