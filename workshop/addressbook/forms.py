from django import forms
from django.forms import SelectDateWidget
from .models import Person,Address,Email,Phone,Group


class PersonForm(forms.ModelForm):
    class Meta:
        model=Person
        fields=('first_name','last_name','description')

