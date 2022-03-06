from django.urls import path
from. import views
urlpatterns=[
    path('addjob/',views.fnAddjob,name='addjob'),
    path('cmprofile/',views.fnCmprofile,name='cmprofile')
]