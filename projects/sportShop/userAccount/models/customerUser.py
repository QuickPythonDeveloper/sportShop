from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class CustomerUser(AbstractBaseUser):

    username = models.CharField(max_length=200,
                                unique=True)
    password = models.CharField(max_length=30)

    USERNAME_FIELD = 'username'
    