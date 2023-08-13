from rest_framework import serializers

from driverapp.models import DriverLog

# DriverMonthSerializer, DriverDaySerializer

class DriverMonthSerializer(serializers.Serializer):

    class Meta:
        model = DriverLog
        fields = '__all__'
    # name = serializers.CharField(max_length=128)
    # birthday_year = serializers.IntegerField()

    # result = serializers.SerializerMethodField()

    # def get_result(self, instance):
    #     instance.


class DriverDaySerializer(serializers.Serializer):

    class Meta:
        model = DriverLog
        fields = '__all__'