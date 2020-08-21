from django.contrib.auth.models import User
from apps.flights.models import Schedule
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = User
        fields = ('url', 'username', 'email')

class Schedule(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Schedule
        fields = (
            'airlines',
            'flight_no',
            'trip_type',
            'departure_airport',
            'arrival_airport',
            'departure_date',
            'return_date'
        )