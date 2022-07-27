# type: ignore
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import PasswordInput,SelectMultiple

from Passengers.models import passengers


from blog.models import answer
from blog.models import blog



class RegisterForm(passengersCreationForm):

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control input-text'})
        self.fields['password2'].widget = PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control input-text'})
    

    class Meta:
        model = passengers
        fields = ['email','fn','password1','password2','subject','is_teacher']
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control input-text','placeholder': 'Email Adress'}),
            'fn': forms.TextInput(attrs={'class': 'form-control input-text','placeholder': 'passport'}),
            #'is_teacher': forms.CheckboxInput(attrs={'class': 'checkbx'}),
            #'subject': forms.Select(attrs={'class': 'form-control input-text'}),
        }
        
