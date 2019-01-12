from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from .forms import PersonForm,AddressForm, PhoneForm,EmailForm,GroupForm
from .models import Person,Address,Phone,Group,Email
# Create your views here.


class newPerson(View):
    def get(self,request):
        form=PersonForm()
        return render(request, 'newPerson.html', {'form': form})

    def post(self,request):
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save(commit=True)
            p=Person.objects.get(id=person.pk)
            address = Address.objects.filter(person_id=p.id)
            phone = Phone.objects.filter(person_id=p.id)
            email = Email.objects.filter(person_id=p.id)
            return render(request,"show.html",locals())


class modifyPerson(View):
    def get(self,request,id):
        person=get_object_or_404(Person,id=id)
        form=PersonForm(instance=person)
        return render(request,'newPerson.html',locals())
    def post(self,request,id):
        person=get_object_or_404(Person,id=id)
        form=PersonForm(request.POST,instance=person)
        if form.is_valid():
            person=form.save(commit=True)
            return redirect('all')


class deletePerson(View):
    def get(self,request,id):
        person=get_object_or_404(Person,id=id)
        person.delete()
        return redirect('all')


class showPerson(View):
    def get(self,request,id):
        p=Person.objects.get(id=id)
        address=Address.objects.filter(person_id=id)
        phone=Phone.objects.filter(person_id=id)
        return render(request,"show.html",locals())


class showAllPersons(View):
    def get(self,request):
        persons_list=Person.objects.all().order_by('last_name','first_name')
        return render(request,"allPersons.html",locals())

class modifyAddress(View):
    def get(self,request,id):
        address = get_object_or_404(Address, id=id)
        form = AddressForm(instance=address)
        return render(request, 'newAddress.html', locals())
    def post(self,request,id):
        addr = get_object_or_404(Address, id=id)
        person_id = addr.person_id
        p = Person.objects.get(id=person_id)
        address = Address.objects.filter(person_id=person_id)
        phone = Phone.objects.filter(person_id=person_id)
        email = Email.objects.filter(person_id=person_id)
        form = AddressForm(request.POST, instance=addr)
        if form.is_valid():
            address_f = form.save(commit=True)
            return render(request, "show.html", locals())


class deleteAddress(View):
    def get(self,request,id):
        addr=get_object_or_404(Address,id=id)
        person_id = addr.person_id
        p = Person.objects.get(id=person_id)
        address = Address.objects.filter(person_id=person_id)
        phone = Phone.objects.filter(person_id=person_id)
        email = Email.objects.filter(person_id=person_id)
        addr.delete()
        return render(request, "show.html", locals())


class addAddress(View):
    def get(self,request,id):
        form = AddressForm()
        person=Person.objects.get(id=id)
        form.fields['person'].initial=person
        return render(request, 'newAddress.html', {'form': form})
    def post(self,request,id):
        form = AddressForm(request.POST)
        p = Person.objects.get(id=id)
        address = Address.objects.filter(person_id=id)
        phone = Phone.objects.filter(person_id=id)
        email = Email.objects.filter(person_id=id)
        if form.is_valid():
            address_f = form.save(commit=True)
            return render(request, "show.html", locals())


class modifyPhone(View):
    def get(self,request,id):
        phone = get_object_or_404(Phone, id=id)
        form = PhoneForm(instance=phone)
        return render(request, 'newPhone.html', locals())
    def post(self,request,id):
        ph = get_object_or_404(Phone, id=id)
        person_id = ph.person_id
        p = Person.objects.get(id=person_id)
        address = Address.objects.filter(person_id=person_id)
        phone = Phone.objects.filter(person_id=person_id)
        email = Email.objects.filter(person_id=person_id)
        form = PhoneForm(request.POST, instance=ph)
        if form.is_valid():
            phone_f = form.save(commit=True)
            return render(request, "show.html", locals())


class deletePhone(View):
    def get(self,request,id):
        ph = get_object_or_404(Phone, id=id)
        person_id=ph.person_id
        p = Person.objects.get(id=person_id)
        address = Address.objects.filter(person_id=person_id)
        phone = Phone.objects.filter(person_id=person_id)
        email = Email.objects.filter(person_id=person_id)
        ph.delete()
        return render(request, "show.html", locals())


class addPhone(View):
    def get(self,request,id):
        form = PhoneForm()
        person=Person.objects.get(id=id)
        form.fields['person'].initial=person
        return render(request, 'newPhone.html', {'form': form})
    def post(self,request,id):
        form = PhoneForm(request.POST)
        p = Person.objects.get(id=id)
        address = Address.objects.filter(person_id=id)
        phone = Phone.objects.filter(person_id=id)
        email = Email.objects.filter(person_id=id)
        if form.is_valid():
            phone_f = form.save(commit=True)
            return render(request, "show.html", locals())


class modifyEmail(View):
    def get(self, request, id):
        email = get_object_or_404(Email, id=id)
        form = EmailForm(instance=email)
        return render(request, 'newEmail.html', locals())

    def post(self, request, id):
        em = get_object_or_404(Email, id=id)
        person_id = em.person_id
        p = Person.objects.get(id=person_id)
        address = Address.objects.filter(person_id=person_id)
        phone = Phone.objects.filter(person_id=person_id)
        email = Email.objects.filter(person_id=person_id)
        form = EmailForm(request.POST, instance=em)
        if form.is_valid():
            email_f = form.save(commit=True)
            return render(request, "show.html", locals())


class deleteEmail(View):
    def get(self,request,id):
        em = get_object_or_404(Email, id=id)
        person_id=em.person_id
        p = Person.objects.get(id=person_id)
        address = Address.objects.filter(person_id=person_id)
        phone = Phone.objects.filter(person_id=person_id)
        email=Email.objects.filter(person_id=person_id)
        em.delete()
        return render(request, "show.html", locals())


class addEmail(View):
    def get(self,request,id):
        form = EmailForm()
        person=Person.objects.get(id=id)
        form.fields['person'].initial=person
        return render(request, 'newEmail.html', {'form': form})
    def post(self,request,id):
        form = EmailForm(request.POST)
        p = Person.objects.get(id=id)
        address = Address.objects.filter(person_id=id)
        phone = Phone.objects.filter(person_id=id)
        email = Email.objects.filter(person_id=id)
        if form.is_valid():
            email_f = form.save(commit=True)
            return render(request, "show.html", locals())


class addGroup(View):
    def get(self, request):
        form=GroupForm()
        return render(request, 'newGroup.html',{'form':form})

    def post(self, request):
        form=GroupForm(request.POST)
        if form.is_valid():
            g = form.save(commit=True)
            return render(request,"showGroup.html",locals())


class modifyGroup(View):
    def get(self,request,id):
        group=get_object_or_404(Group,id=id)
        form=GroupForm(instance=group)
        return render(request,'newGroup.html',locals())
    def post(self,request,id):
        group=get_object_or_404(Group,id=id)
        form=GroupForm(request.POST,instance=group)
        if form.is_valid():
            g = form.save(commit=True)
            return render(request, "showGroup.html", locals())

class deleteGroup(View):
    def get(self,request,id):
        group=get_object_or_404(Group,id=id)
        group.delete()
        return redirect('allGroups')


class showGroup(View):
    def get(self,request,id):
        g=Group.objects.get(id=id)
        return render(request,"showGroup.html",locals())

class allGroups(View):
    def get(self,request):
        groups_list=Group.objects.all().order_by('group_name')
        return render(request,"allGroups.html",locals())