from rest_framework import serializers

from driverapp.models import DriverLog



class DriverResultSerializer(serializers.Serializer):

    class Meta:
        model = DriverLog
        fields = '__all__'

