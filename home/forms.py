from django.forms import ModelForm, Textarea, FileInput, DateTimeField, TextInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Birth_Certificate

class DateInput(forms.DateInput):
    input_type  =   'date'

class Number(forms.TextInput):
    input_type  =   'text'

# Birth Certificate form
class Birth_CertificateForm(forms.ModelForm):
    class Meta:
        model   =   Birth_Certificate
        fields  =   [
            'first_name',
            'middle_name',
            'last_name',
            'Date_of_Birth',
            'e_mail_address',
            'phone_number'
          
        ]
        widgets = {
            'Date_of_Birth': DateInput(),
            'phone_number': Number(attrs={'placeholder':'0701234567'}),
            'e_mail_address': TextInput(attrs={'placeholder':'johndoe@email.com'}),
            }