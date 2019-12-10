from django.http import HttpResponse, JsonResponse
import requests
from django.shortcuts import render
from django.conf import settings
import os
from api.models import FlightStatus
from api.serializer import FlightStatusSerializer


def origin_api(request):
    """
    List unique list of all origins.
    """
    if request.method == 'GET':
        origins = FlightStatus.getOrigins()
        return JsonResponse(origins, safe=False)

def destination_api(request):
    """
    List unique list of all destinations.
    """
    if request.method == 'GET':
        destinations = FlightStatus.getDestinations()
        return JsonResponse(destinations, safe=False)


def search_api(request):
    """
    List all Flights matching the criteria in the request.
    """
    if request.method == 'GET':
        origin = request.GET.get('origin')
        destination= request.GET.get('destination')
        if (((origin is not None) and len(origin) > 2)  or ((destination is not None)  and len(destination) > 2)):
        	#Origin and Destination contains a concatenation of airport code and full name. 
        	#Get the first 3 characters from origin and destination to get the airport code
        	if ((origin is not None) and len(origin) > 2):
        	    origin = origin[:3]
        	    print(origin)
        	if ((destination is not None)  and len(destination) > 2):
        	    destination = destination[:3]
        	    print(destination)
        flightStatus = FlightStatus.getFlightsFiltered(origin, destination)
        serializer = FlightStatusSerializer(flightStatus, many=True)
        return JsonResponse(serializer.data, safe=False)



def flightSearch(request):
    origin = request.GET.get('origin')
    destination= request.GET.get('destination')

    #Validate the form data before performing the search
    if (((origin is not None) and len(origin) > 2)  or ((destination is not None)  and len(destination) > 2)):
        #Origin and Destination contains a concatenation of airport code and full name. 
        #Get the first 3 characters from origin and destination to get the airport code
        if ((origin is not None) and len(origin) > 2):
        	origin = origin[:3]
        	print(origin)
        if ((destination is not None)  and len(destination) > 2):
        	destination = destination[:3]
        	print(destination)
        baseEndPoint = settings.API_END_POINT_FLIGHT_SEARCH
        apiEndPoint = baseEndPoint  + '?origin=' + origin +'&destination=' + destination
        response = requests.get(apiEndPoint)
        return render(request, 'flightStatus.html',{'flights':response.json(), 'origin':origin, 'destination': destination})

    #Form selection has not been made yet.
    return render(request, 'flightStatus.html',{} )



