from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from .forms import PersonForm
from .models import Person,Address,Phone,Group,Email
# Create your views here.

class newPerson(View):
    def get(self,request):
        form=PersonForm()
        return render(request, 'newPerson.html', {'form': form})
        pass

    def post(self,request):
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save(commit=True)
            return redirect(reverse('all'))
        pass

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
        return render(request,"show.html",locals())


class showAllPersons(View):
    def get(self,request):
        persons_list=Person.objects.all().order_by('id')
        return render(request,"allPersons.html",locals())
