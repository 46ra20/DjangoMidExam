from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

# from django import forms

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

class UpdateUser(UserChangeForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email']
        exclude =['password']


