from django.shortcuts import render

# Create your views here.
def fnAddjob(request):
   return render(request,'addjob.html')
def fnCmprofile(request):
   return render(request,'cmprofile.html')