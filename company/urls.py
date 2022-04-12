from django.urls import path
from. import views
urlpatterns=[
    path('addjob/',views.addjob,name='addjob'),
    path('cmprofile/',views.cmprofile,name='cmprofile'),
     path('notifi/',views.notifi,name='cmprofile')
]