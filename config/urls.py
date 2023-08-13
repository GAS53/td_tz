from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("driver/v1/", include('driverapp.urls', namespace='driver_api_v1')),

]
