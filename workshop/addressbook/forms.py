from django import forms
from django.forms import SelectDateWidget,Select,ModelChoiceField
from django.forms.widgets import CheckboxSelectMultiple
from django.forms import widgets

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
        fields=('group_name',)

class GroupPersonForm(forms.ModelForm):
    class Meta:
        model=Group
        fields=('group_name','person')

    def __init__(self, *args, **kwargs):
        super(GroupPersonForm, self).__init__(*args, **kwargs)
        self.fields['person'].widget = CheckboxSelectMultiple()
        self.fields['person'].queryset = Person.objects.all()
        self.fields["group_name"].widget=Select(choices=list(Group.objects.all().values_list("group_name","group_name").order_by("group_name")))
