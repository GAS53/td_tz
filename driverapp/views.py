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

        find_set = DriverLog.objects.filter(driver_id=driver_id)
        if not find_set:
            return Response({'error': 'dont have this user in db'}, status=404)
        elif not month:
            Response({'error': 'need month'}, status=404)

        find_set = find_set.filter(month=month)
        
        response = {}

        if day:
            find_set = find_set.filter(day=day)

        day_di = {}
        for i in find_set:
            if day:
                if day_di.get(i.status.description):
                    day_di[i.status.description] += i.time
                else:
                    day_di[i.status.description] = i.time
                response[f'{i.day}-{i.month}-{i.year}'] = day_di    
            else:
                if day_di.get(i.status.description):
                    day_di[i.status.description] += i.time
                else:
                    day_di[i.status.description] = i.time
                response[f'{i.month}-{i.year}'] = day_di 


        return Response(response, status=200)




