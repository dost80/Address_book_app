"""project_ab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

from app_ab.views import AddPerson, PersonList, show_person, EditPerson, delete_person,\
    add_address, EditAddress, delete_address, add_phone, EditPhone, delete_phone, \
    add_email, EditEmail, delete_email

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^new/$', AddPerson.as_view()),
    url(r'^show/(?P<id>\d+)/$', show_person),
    url(r'^modify/(?P<id>\d+)/$', EditPerson.as_view()),
    url(r'^delete/(?P<id>\d+)/$', delete_person),
    url(r'^$', PersonList.as_view()),
    url(r'^add_address/(?P<id>\d+)/$', add_address),
    url(r'^edit_address/(?P<person_id>\d+)/(?P<id>\d+)/$', EditAddress.as_view()),
    url(r'^delete_address/(?P<person_id>\d+)/(?P<address_id>\d+)/$', delete_address),
    url(r'^add_phone/(?P<id>\d+)/$', add_phone),
    url(r'^edit_phone/(?P<person_id>\d+)/(?P<id>\d+)/$', EditPhone.as_view()),
    url(r'^delete_phone/(?P<person_id>\d+)/(?P<phone_id>\d+)/$', delete_phone),
    url(r'^add_email/(?P<id>\d+)/$', add_email),
    url(r'^edit_email/(?P<person_id>\d+)/(?P<id>\d+)/$', EditEmail.as_view()),
    url(r'^delete_email/(?P<person_id>\d+)/(?P<email_id>\d+)/$', delete_email),
]
