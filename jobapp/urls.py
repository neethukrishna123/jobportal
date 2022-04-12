from doctest import master
from django.urls import path
from. import views

urlpatterns=[

    path('index/',views.index,name='home'),
     path('loginpage/',views.loginpage,name='loginpage'),
     path('registration/',views.registration,name='registration'),
     path('about/',views.about,name='about'),
     path('contact/',views.contact,name='contact'),
     path('secondregistration/',views.secondregistration,name='secondregistration'),
     path('joblist/',views.joblist,name='joblist'),
     path('forgot/',views.forgot,name='forgot'),
     path('userpage/',views.userpage,name='userpage'),
     path('userprofile/',views.userprofile,name='userprofile'),
     path('applications/',views.applications,name='applications'),
      path('notifications/',views.notifications,name='notifications'),
    # path('master/',views.master,name='master')


]