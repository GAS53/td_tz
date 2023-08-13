import datetime

from rest_framework.views import APIView
from rest_framework.response import Response

from driverapp.models import DriverLog, DriverStatus
from driverapp.serializers import DriverResultSerializer



class DriverResult(APIView):
    queryset = DriverLog.objects.all()
    serializer_class = DriverResultSerializer
    # permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def get(self, request, *args, **kwargs):
        driver_id = kwargs.get('driver_id', None)
        now_year = datetime.date.today().year
        
        year = request.query_params.get('year', now_year)
        month = request.query_params.get('month', None)
        day = request.query_params.get('day', None)
        # print(f'y m d {year} {month} {day}')

        find_set = DriverLog.objects.filter(driver_id=driver_id)
        if not find_set:
            return Response({'error': 'dont have this user in db'}, status=404)
        elif not month:
            Response({'error': 'need month'}, status=404)

        find_set = find_set.filter(month=month)
        if day:
            find_set = find_set.filter(day=day)

        response = {}
        for i in find_set:
            status_di = {}
            for status in DriverStatus.objects.all():
                if status_di.get(status.description):
                    status_di[status.description] += i.time
                else:
                    status_di[status.description] = i.time

            response[f'{i.day}{i.month}{i.year}'] = status_di
        return Response(status_di, status=200)




