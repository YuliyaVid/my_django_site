from django import forms
from .models import Client

class PostForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('Name', 'Surname', 'Fathername', 'Address', 'Phone_number')

