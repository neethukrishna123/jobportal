from django.urls import path
from. import views
urlpatterns=[
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('admindashboard/',views.admindashboard,name='admindashboard'),
    path('msg/',views.msg,name='msg'),
     path('logout/',views.logout,name='logout')
]
