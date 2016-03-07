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


class Room(models.Model):
    room_no = models.IntegerField(primary_key = True, unique = True)
    block_id = models.IntegerField(default=0)
    capacity = models.IntegerField(default=4)
    vacancy = models.IntegerField(default=0)
    def __str__(self):
        return str(self.room_no)

class Student(models.Model):

    join_year = models.IntegerField(default=0)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    gender = models.CharField(max_length = 1)
    age = models.IntegerField(default=0)
    branch = models.CharField(max_length = 50)
    roll_no = models.OneToOneField(User, on_delete = models.CASCADE, primary_key =True,unique = True )
    handicapped = models.BooleanField(default = False)
    graduate = models.BooleanField(default = False)

    def __str__(self):
        return str(self.roll_no)

class Change(models.Model):

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    reason = models.CharField(max_length = 300)

class Swap(models.Model):

    student1 = models.ForeignKey(Student, on_delete=models.CASCADE)
    student2 = models.CharField(max_length = 50)
    reason = models.CharField(max_length=300)
    accept = models.BooleanField(default=False)




