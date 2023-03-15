from django.contrib.auth.models import User
from django.db import models
# Create your models here.


class Account(models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="Владелец")


class Tag(models.Model):
    name = models.CharField("Название", max_length=50)

