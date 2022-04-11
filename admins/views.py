from django.shortcuts import render

# Create your views here.
def adminlogin(request):
   return render(request,'admapp/adminlogin.html')
def admindashboard(request):
   return render(request,'admapp/admindashboard.html')
def msg(request):
   return render(request,'admapp/msg.html')
def logout(request):
   return render(request,'admapp/logout.html')



