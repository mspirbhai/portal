from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    is_updater = models.BooleanField(default=False, verbose_name="Updater Status")
    is_controller  = models.BooleanField(default=False, verbose_name="Controller Status")

    def __str__(self):
        return self.email
