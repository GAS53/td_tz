import datetime

from rest_framework.views import APIView
from rest_framework.response import Response

from driverapp.models import DriverLog
from driverapp.serializers import DriverMonthSerializer, DriverDaySerializer


class DriverDayResult(APIView):
    queryset = DriverLog.objects.all()
    serializer_class = DriverDaySerializer
    # permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def get(self, request, *args, **kwargs):
        now_year = datetime.date.today().year
        now_month = datetime.date.today().month
        response = {}
        year = request.query_params.get('month', None)
        month = request.query_params.get('month', None)
        day = request.query_params.get('month', None)
        
        if not month:
            Response({'error':'need month'}, status=404)
        elif not day:
            DriverLog.objects.filter(day)







        return Response({'error':'date not exists'})


class DriverMonthResult(APIView):
    queryset = DriverLog.objects.all()
    serializer_class = DriverMonthSerializer
    # permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


