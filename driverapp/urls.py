from django.urls import path

from driverapp.views import DriverDayResult, DriverMonthResult

app_name = 'driverapp'


urlpatterns = [
    path("day_result/<int:driver_id>", DriverDayResult.as_view(), name='get_driver_day'),
    path("month_result/<int:driver_id>", DriverMonthResult.as_view(), name='get_driver_month'),
]