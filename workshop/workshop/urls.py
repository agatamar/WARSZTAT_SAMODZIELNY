"""workshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from addressbook.views import newPerson,modifyPerson,deletePerson,showPerson,showAllPersons

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^new/$', newPerson.as_view(),	name="new"),
    re_path(r'^modify/(?P<id>[0-9]+)/$', modifyPerson.as_view(),	name="modify"),
    re_path(r'^delete/(?P<id>[0-9]+)/$', deletePerson.as_view(),	name="delete"),
    re_path(r'^show/(?P<id>[0-9]+)/$', showPerson.as_view(),	name="show"),
    re_path(r'^all/$', showAllPersons.as_view(), name="all"),
]
