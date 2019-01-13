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
from addressbook.views import newPerson,modifyPerson,deletePerson,showPerson,showAllPersons,modifyAddress,deleteAddress,addAddress,modifyPhone,deletePhone,addPhone,modifyEmail,deleteEmail,addEmail,modifyGroup,deleteGroup,addGroup,allGroups,showGroup,addPersonToGroup,groupSearch

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^new/$', newPerson.as_view(),	name="new"),
    re_path(r'^modify/(?P<id>[0-9]+)/$', modifyPerson.as_view(),	name="modify"),
    re_path(r'^delete/(?P<id>[0-9]+)/$', deletePerson.as_view(),	name="delete"),
    re_path(r'^show/(?P<id>[0-9]+)/$', showPerson.as_view(),	name="show"),
    re_path(r'^all/$', showAllPersons.as_view(), name="all"),
    re_path(r'^modifyAddress/(?P<id>[0-9]+)/$', modifyAddress.as_view(),	name="modifyAddress"),
    re_path(r'^deleteAddress/(?P<id>[0-9]+)/$', deleteAddress.as_view(),	name="deleteAddress"),
    re_path(r'^addAddress/(?P<id>[0-9]+)/$', addAddress.as_view(),	name="addAddress"),
    re_path(r'^modifyPhone/(?P<id>[0-9]+)/$', modifyPhone.as_view(), name="modifyPhone"),
    re_path(r'^deletePhone/(?P<id>[0-9]+)/$', deletePhone.as_view(), name="deletePhone"),
    re_path(r'^addPhone/(?P<id>[0-9]+)/$', addPhone.as_view(), name="addPhone"),
    re_path(r'^modifyEmail/(?P<id>[0-9]+)/$', modifyEmail.as_view(), name="modifyEmail"),
    re_path(r'^deleteEmail/(?P<id>[0-9]+)/$', deleteEmail.as_view(), name="deleteEmail"),
    re_path(r'^addEmail/(?P<id>[0-9]+)/$', addEmail.as_view(), name="addEmail"),
    re_path(r'^addGroup/$', addGroup.as_view(), name="addGroup"),
    re_path(r'^allGroups/$', allGroups.as_view(), name="allGroups"),
    re_path(r'^showGroup/(?P<id>[0-9]+)/$', showGroup.as_view(), name="showGroup"),
    re_path(r'^modifyGroup/(?P<id>[0-9]+)/$', modifyGroup.as_view(), name="modifyGroup"),
    re_path(r'^deleteGroup/(?P<id>[0-9]+)/$', deleteGroup.as_view(), name="deleteGroup"),
    re_path(r'^addPersonToGroup/$',addPersonToGroup.as_view(),name="addPersonToGroup"),
    re_path(r'^groupSearch/$',groupSearch.as_view(),name="groupSearch"),
]
