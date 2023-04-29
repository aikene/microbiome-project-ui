from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_email(self):
        return f"{self.email}"

    def __str__(self):
        return f"{self.username}"


class Metadata(models.Model):   # <- added by nlandi
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(blank=True)
    day_started = models.DateField()
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.first_name
