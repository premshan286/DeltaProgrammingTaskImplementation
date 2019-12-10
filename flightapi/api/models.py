from django.db import models
import csv
import os

#variables to hold the cached data (Contents parsed from the csv file)
origin_list = []
destination_list = []
flight_status_list = []

class FlightStatus(models.Model):
    recordID = models.TextField()
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()
    flightID = models.TextField()
    flightNum = models.TextField()
    scheduledOriginGate = models.TextField()
    scheduledDestinationGate = models.TextField()
    outGMT = models.DateTimeField()
    inGMT = models.DateTimeField()
    offGMT = models.DateTimeField()
    onGMT = models.DateTimeField()
    destination = models.TextField()
    origin = models.TextField()
    destinationFullName = models.TextField()
    originFullName = models.TextField()



    def __init__(self, recordID, createdAt, updatedAt, flightID, flightNum, scheduledOriginGate, scheduledDestinationGate, outGMT, inGMT, offGMT, onGMT, destination, origin, destinationFullName, originFullName):
        self.recordID = recordID
        self.createdAt = createdAt 
        self.updatedAt = updatedAt 
        self.flightID = flightID 
        self.flightNum = flightNum 
        self.scheduledOriginGate = scheduledOriginGate 
        self.scheduledDestinationGate = scheduledDestinationGate 
        self.outGMT = outGMT 
        self.inGMT = inGMT 
        self.offGMT = offGMT 
        self.onGMT = onGMT 
        self.destination = destination 
        self.origin = origin 
        self.destinationFullName = destinationFullName 
        self.originFullName = originFullName 


    #Initialize and cache the flight data with the contents of the csv file   
    def importDataFromCSV():
        print('*******caching file data**************')
        #dataFile = 'C:\\DeltaAssignment\\ods-full-stack-coding-assignment-master\\ods-full-stack-coding-assignment-master\\data\\flights.csv'
        dataFile = os.path.join( os.getcwd(),'flights.csv' )
        with open(dataFile, 'r') as csv_file:
        	reader = csv.reader(csv_file)
        	next(reader, None)  # Skip the header.
        	# Unpack the row directly in the head of the for loop.
        	for recordID, createdAt, updatedAt, flightID, flightNum, scheduledOriginGate, scheduledDestinationGate, outGMT, inGMT, offGMT, onGMT, destination, origin, destinationFullName, originFullName in reader:
        		# Now create the Flight Status instance and append it to the list.
        		flight_status_list.append(FlightStatus(recordID,createdAt, updatedAt, flightID, flightNum, scheduledOriginGate, scheduledDestinationGate, outGMT, inGMT, offGMT, onGMT, destination, origin, destinationFullName, originFullName))
        		origin_list.append(origin + '(' + originFullName + ')')
        		destination_list.append(origin + '(' + originFullName + ')')


    #Return the list of unique origins from the csv file 
    def getOrigins():
        if (len(flight_status_list) == 0):
        	FlightStatus.importDataFromCSV()	
        return sorted(list(set(origin_list)))

    #Return the list of unique origins from the csv file  
    def getDestinations():
        if (len(flight_status_list) == 0):
        	FlightStatus.importDataFromCSV()	
        return sorted(list(set(destination_list)))

    #Return the list of flights that match the criteria based on Origin and Destination   
    def getFlightsFiltered(originParam, destinationParam):
        filteredFlights = []
        print (originParam.upper())
        print (destinationParam.upper())
        if (len(flight_status_list) == 0):
        	FlightStatus.importDataFromCSV()	
        filteredFlights = list(filter(lambda x: ((originParam.upper() in x.origin.upper()) and (destinationParam.upper() in x.destination.upper())), flight_status_list))
        print ('returning flights count: ' + str(len(filteredFlights)))
        return filteredFlights