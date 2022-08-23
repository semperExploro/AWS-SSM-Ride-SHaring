# AWS - SSM Ride Sharing

This program provides automatic ride sharing coordination for Stepping Stone Ministry at Johns Hopkins University 

# Guidance for Google Forms

---

## Rider Forms

The parameters for the forms for riders must goes as follows. The word Exact means that that parameter MUST follow the same spelling and formatting. 

### Questions

| Parameter | Exact | Description |
| --- | --- | --- |
| Email | N | Grabs user emails |
| Name | Y | Asks for user’s name |
| Services | N | The list of times for services |

### Options

| Parameter | Exact | Description |
| --- | --- | --- |
| Not Going | Y | Option for early arrival |
| Early - 8:10 AM | Y | Early Arrival |
| Normal - 8:50 AM | Y | Normal Arrival |
| After service - 11:00 PM | Y | After Service |
| After lunch - 12:30 PM | Y | After Lunch |

## Drive Forms

The parameters for the forms for riders must goes as follows. The word Exact means that that parameter MUST follow the same spelling and formatting. 

### Questions

| Parameter | Exact | Description |
| --- | --- | --- |
| Email | N | Grabs user emails |
| Name | Y | Asks for user’s name |
| Services | N | The list of times for services |
| What is your carry capacity? | Y | Number of people the driver can carry. 

NOTE: The program assumes the driver has the same number of seats each week |

### Options

| Parameter | Exact | Description |
| --- | --- | --- |
| Not Going | Y | Option for early arrival |
| Early - 8:10 AM | Y | Early Arrival |
| Normal - 8:50 AM | Y | Normal Arrival |
| After service - 11:00 PM | Y | After Service |
| After lunch - 12:30 PM | Y | After Lunch |

# Utilizing the Automated System

---

## Upload to the Google Drive Folder Under `SSM Ride Sharing/Input`

The responses for riders from the Google form MUST be titled `riders.csv` and uploaded to the folder `SSM Ride Sharing/Input`

The responses for drivers from the Google form MUST be titled `drivers.csv` and uploaded to the folder `SSM Ride Sharing/Input`

## Retrieve the files under `SSM Ride Sharing/Output`

The files are outputted as `riders`+fileNumber + `.csv`

Each number corresponds to the nth-1 Sunday of that month. For instance, `rides0.csv` corresponds to the first Sunday of the month, `rides1.csv` corresponds to the second Sunday of the month, so on and so fourth. 

In the event there are events in addition to Sundays, the order of the files goes in the order of the dates that are listed in the Google forms. 

# Methodology

---

The program works by prioritizing drivers to times that have the highest demand. If there isn’t a driver available, an uber is assigned.

# Flow

---
![alt text](https://https://github.com/semperExploro/AWS-SSM-Ride-Sharing/blob/master/AWS%20SSM%20Workflow.png
