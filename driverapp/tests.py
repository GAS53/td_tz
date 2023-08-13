import calendar
import datetime
from random import choice

from rest_framework.test import APIClient, APITestCase
from django.urls import reverse

from authapp.models import BaseUser
from driverapp.models import DriverLog, DriverStatus, Company

class GetDriverDayTestCase(APITestCase):


    def setUp(self):
        self.month = 1
        self.statuses = []
        self.statuses.append(DriverStatus.objects.create(value=0, description='work'))
        self.statuses.append(DriverStatus.objects.create(value=1, description='sleep'))
        self.statuses.append(DriverStatus.objects.create(value=2, description='stay'))
        self.statuses.append(DriverStatus.objects.create(value=3, description='off'))
        self.statuses.append(DriverStatus.objects.create(value=3, description='eating'))


        self.drivers = []

        for i in range(5):
            self.drivers.append(BaseUser.objects.create(
                first_name=f'first_name_{i}',
                last_name=f'last_name_{i}',
                email=f'email_{i}',
                password = f'password_{i}',
                birthday='2023-01-01'
            ))

        self.company = Company.objects.create(
            id=1,
            full_name='Full company name ....',
            short_name='short comp. name'
        )

        now_year = datetime.date.today().year
        calendar_ = calendar.Calendar(firstweekday=0)
        for day in calendar_.itermonthdates(now_year, self.month):
            for driver in self.drivers:
                DriverLog.objects.create(
                    driver_id=driver,
                    company_id=self.company,
                    status=choice(self.statuses),
                    day=day,
                    time=choice(range(1, 9))
                )


            

    def test_get_days(self):
        url = reverse('driver_api_v1:get_driver_day', args=[1,])
        data = {'month': 2 }
        response = self.client.get(url, data=data)
        print(response)