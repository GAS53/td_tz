from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin


class BaseUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField("first name", max_length=150)
    last_name = models.CharField("last name", max_length=150)
    email = models.EmailField("email address", unique=True)
    birthday = models.DateField(verbose_name="birthday")
    patronymic = models.CharField(verbose_name="patronymic", max_length=40, default="")
    password = models.CharField(verbose_name="password", max_length=40)
    create_date = models.DateTimeField(auto_now_add=True)
    is_superuser = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_driver = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.first_name} ({self.last_name})"
    
    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name"]

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        abstract = False

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

