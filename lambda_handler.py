from extraction import*

def lambda_handler():
    riderInformation = readRidersCSVFile(RIDER_CSV_FILE)
    driverInformation = readRidersCSVFile(DRIVER_CSV_FILE)
    driverDict = {}
    riderDict = {}

    #print(driverInformation)
    #print(userInformation)
    compileDictionary(driverInformation, driverDict)
    print(driverDict)
    compileDictionary(riderInformation, riderDict)
    #print(riderDict)


if __name__ == '__main__':
    lambda_handler()
