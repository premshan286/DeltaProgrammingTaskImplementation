from rest_framework import serializers
from api.models import FlightStatus


class FlightStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightStatus
        fields = ['createdAt', 'updatedAt', 'flightID', 'flightNum', 'scheduledOriginGate', 'scheduledDestinationGate', 'outGMT', 'inGMT', 'offGMT', 'onGMT', 'destination', 'origin', 'destinationFullName', 'originFullName']

