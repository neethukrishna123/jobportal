from django.shortcuts import render

# Create your views here.
def addjob(request):
   return render(request,'addjob.html')
def cmprofile(request):
   return render(request,'cmprofile.html')
def notifi(request):
   return render(request,'notifi.html')