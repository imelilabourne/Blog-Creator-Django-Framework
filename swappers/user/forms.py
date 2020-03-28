from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from base.models import Profile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta: 
        model = User
        fields = ['username', 'email', 'first_name', 'last_name' , 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta: 
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio', 'PFeaturedimage', 'PFeaturedimage2', 'TFeaturedimage', 'TFeaturedimage2']
