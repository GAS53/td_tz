from django.db import models
from django.contrib.auth.models import AbstractUser


class BaseUser(AbstractUser):
    id = models.BigAutoField(verbose_name='user id')
    birthday = models.PositiveIntegerField(verbose_name="birthday")
    email = models.CharField(verbose_name="email", max_length=40, unique=True)
    first_name = models.CharField(verbose_name="name", max_length=60)
    last_name = models.CharField(verbose_name="surname", max_length=60)
    patronymic = models.CharField(verbose_name="patronymic", max_length=40, default="")
    password = models.CharField(verbose_name="password", max_length=40)
    registration_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_driver = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} ({self.last_name})"