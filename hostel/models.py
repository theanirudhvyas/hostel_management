from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# Creating a user profile. Link: www.turnkeylinux.org/blog/django-profile
class Diff(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key =True, )
    is_student = models.BooleanField(default = True)

    def __str__(self):
        return str(self.user)

class Student(models.Model):

    join_year = models.IntegerField(default=0)
    room_no = models.IntegerField(default=0)
    gender = models.CharField(max_length = 1)
    age = models.IntegerField(default=0)
    branch = models.CharField(max_length = 50)
    roll_no = models.OneToOneField(User, on_delete = models.CASCADE, primary_key =True,unique = True )
    handicapped = models.BooleanField(default = False)
    graduate = models.BooleanField(default = False)

    def __str__(self):
        return str(self.roll_no)


class Room(models.Model):
    room_id = models.IntegerField(primary_key = True, unique = True)
    block_id = models.IntegerField(default=0)
    capacity = models.IntegerField(default=4)
    vacancy = models.IntegerField(default=0)
