from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from . models import Profile 
from django import forms 



class UserForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = ('username', 'first_name', 'last_name', 'email') 


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile 
        fields = ('bio', 'location', 'birthdate', 'gender', 'images') 
        widgets = {
            'bio' : forms.Textarea(attrs= {'rows': 5, 'cols': 24}),
        }


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField() 
    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User 
        model = Profile
        fields = '__all__'
        


