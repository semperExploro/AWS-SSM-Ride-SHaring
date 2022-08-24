import boto3

EARLY_MORNING_MARKER = "Early - 8:10 AM"
MORNING_NORMAL_MARKER = "Normal - 8:50 AM"
AFTER_SERVICE_MARKER = "After service - 11:00 PM"
AFTER_LUNCH_MARKER = "After lunch - 12:30 PM"
BUCKET_NAME  = "bucket-name"
s3 = boto3.client('s3')

def parseString(dict, eraMarker, alpha, date, riders, drivers):
    for marker in eraMarker:
        individualDate = date+","+marker
        if individualDate not in dict:
            continue
        for array in dict[individualDate]:
            alpha = alpha + individualDate.replace(",", "-")+","
            drivers = drivers + array[1]+","
            riders.append(array[0])

    return alpha, riders, drivers

def getLengthAllElements(array):
    count = 0
    for element in array:
        count = count + len(element)
    return count

def getMax(array):
    list = []
    for element in array:
        list.append(len(element))
    list.sort()
    if list[len(list)-1] < len(array):
        return len(array)
    else: 
        return (list[len(list)-1])

def writeToCSV(dateLine, drivers, riders,COUNTER):
    fileName = "rides "+str(COUNTER)+".csv"
    
    index = 0
    count = getLengthAllElements(riders)
    max = getMax(riders)
    fullLine = dateLine+"\n"+drivers+"\n"
    while (count != 0):
        if index > 100:
            raise ValueError("Index passes realistic amount for number of occupants for a car")
        line = ""
        for car in range(max):
            if index > len(riders[car])-1:
                line = line + ","
            else:
                line = line + riders[car][index] + ","
                count = count - 1
        fullLine = fullLine + line + "\n"
        index = index+1
    encoded_string = fullLine.encode("utf-8")
    s3.put_object(Bucket=BUCKET_NAME,Key=fileName,Body=encoded_string)
    COUNTER = COUNTER + 1
    return COUNTER


def convertDictToCSV(dict, morning, afternoon):
    earlyMarker = [EARLY_MORNING_MARKER, MORNING_NORMAL_MARKER]
    lateMarker = [AFTER_SERVICE_MARKER, AFTER_LUNCH_MARKER]
    COUNTER = 0
    for i in range(len(morning)):
        dateLine = ""
        drivers = ""
        riders = []
        date = morning[i]

        dateLine, riders, drivers = parseString(
            dict, earlyMarker, dateLine, date, riders, drivers)
        date = afternoon[i]
        dateLine, riders, drivers = parseString(
            dict, lateMarker, dateLine, date, riders, drivers)
        COUNTER = writeToCSV(dateLine,drivers,riders,COUNTER)