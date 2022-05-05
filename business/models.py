from django.db import models

ADMIN = 1
VIPClIENT = 2
CLIENT = 3
USER_TYPE = (
    (ADMIN,'ADMIN'),
    (VIPClIENT,'VIP-ClIENT'),
    (CLIENT,'CLIENT')
)
MALE = 1
FEMALE = 2
GENDER_TYPE = (
    (MALE, 'MALE'),
    (FEMALE, 'FEMALE'),
)


class CustomUser(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    user_type = models.IntegerField(choices=USER_TYPE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField('phone_number', max_length=15)
    age = models.IntegerField()
    gender = models.IntegerField(choices=GENDER_TYPE)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)


class GeektechDirections(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    image = models.ImageField()



