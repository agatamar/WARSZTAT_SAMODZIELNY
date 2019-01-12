from django import forms
from django.forms import SelectDateWidget
from .models import Person,Address,Email,Phone,Group


class PersonForm(forms.ModelForm):
    class Meta:
        model=Person
        fields=('first_name','last_name','description')


class AddressForm(forms.ModelForm):
            class Meta:
                model=Address
                fields=('city','street','building_number','apartment_number','person')


class PhoneForm(forms.ModelForm):
    class Meta:
        model=Phone
        fields=('phone_number','phone_type','person')


class EmailForm(forms.ModelForm):
    class Meta:
        model=Email
        fields=('email','email_type','person')

class GroupForm(forms.ModelForm):
    class Meta:
        model=Group
        fields=('group_name','person')
