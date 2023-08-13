from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


class Company(models.Model):
    id = models.BigIntegerField(verbose_name='company_id', primary_key=True, unique=True)
    full_name = models.CharField(verbose_name="full company name", max_length=200)
    short_name = models.CharField(verbose_name="full company name", max_length=50)


class DriverStatus(models.Model):
    value = models.CharField(verbose_name='value', max_length=10, default='not activ')
    description = models.CharField(verbose_name='description', max_length=200)


class DriverLog(models.Model):
    driver_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_id', default=0)
    company_id = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    status = models.ForeignKey(DriverStatus, on_delete=models.DO_NOTHING)
    day = models.SmallIntegerField(verbose_name='day now with status', default=0, validators=(MaxValueValidator(31), MinValueValidator(0)))
    month = models.SmallIntegerField(verbose_name='month now with status', default=0, validators=(MaxValueValidator(12), MinValueValidator(0)))
    time = models.SmallIntegerField(verbose_name='count ours with status', default=0, validators=(MaxValueValidator(24), MinValueValidator(0)))

    def __str__(self):
        return f"{self.first_name} ({self.last_name})"