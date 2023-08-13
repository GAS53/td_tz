from django.urls import path

from driverapp.views import DriverResult

app_name = 'driverapp'


urlpatterns = [
    path("result/<int:driver_id>", DriverResult.as_view(), name='get_driver_day'),
]