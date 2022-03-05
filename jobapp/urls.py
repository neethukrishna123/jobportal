from django.urls import path
from. import views
urlpatterns=[
    path('index/',views.fnIndex,name='home'),
     path('loginpage/',views.fnLoginpage,name='loginpage'),
     path('registration/',views.fnRegistration,name='registration'),
     path('about/',views.fnAbout,name='about'),
     path('contact/',views.fnContact,name='contact'),
     path('secondregistration/',views.fnSecondregistration,name='secondregistration'),
     path('joblist/',views.fnJoblist,name='joblist'),
     path('forgot/',views.fnForgot,name='forgot'),
     path('userpage/',views.fnUserpage,name='userpage')
    

]