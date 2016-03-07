from django import forms
from django.contrib.auth.models import User
from hostel.models import Diff, Student, Room


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class DiffForm(forms.ModelForm):
    class Meta:
        model = Diff
        fields = ('is_student',)


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('gender', 'age', 'branch', 'handicapped')


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('room_no', )


