from .models import Profile
from django import forms


class ProfileForm(forms.ModelForm):
    class meta:
        model = Profile
        fields=('name', 'email', 'date_of_birth', 'phone_number')

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=('name', 'email', 'date_of_birth', 'phone_number')