from django import forms
from . import models

class CreateProfile(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ['first_name','last_name','age','email','image']