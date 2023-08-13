from django.db import models
from django.contrib.auth.models import AbstractUser


class BaseUser(AbstractUser):
    id = models.BigIntegerField(verbose_name='id user', primary_key=True)
    birthday = models.PositiveIntegerField(verbose_name="birthday")
    patronymic = models.CharField(verbose_name="patronymic", max_length=40, default="")
    password = models.CharField(verbose_name="password", max_length=40)
    create_date = models.DateTimeField(auto_now_add=True)
    is_superuser = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_driver = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} ({self.last_name})"