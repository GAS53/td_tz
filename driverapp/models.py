from authapp.models import BaseUser
from django.db import models


class Company(models.Model):
    id = models.BigIntegerField(verbose_name='company_id', primary_key=True, unique=True)
    full_name = models.CharField(verbose_name="full company name", max_length=200)
    short_name = models.CharField(verbose_name="full company name", max_length=50)


class DriverStatus(models.Model):
    value = models.CharField(verbose_name='value', max_length=10, default='not activ')
    description = models.CharField(verbose_name='description', max_length=200)


class DriverLog(BaseUser):
    driver_id = models.ForeignKey(BaseUser, on_delete=models.SET_NULL)
    company_id = models.ForeignKey(Company, on_delete=models.SET_NULL)
    status = models.ForeignKey(DriverStatus, on_delete=models.SET_DEFAULT, default='not activ')

    def __str__(self):
        return f"{self.first_name} ({self.last_name})"