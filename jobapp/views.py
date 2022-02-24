from django.shortcuts import render

# Create your views here.

def fnIndex(request):
   return render(request,'index.html')
def fnLoginpage(request):
   return render(request,'loginpage.html')
def fnRegistration(request):
   return render(request,'Registration.html')
def fnAbout(request):
   return render(request,'About.html')
def fnContact(request):
   return render(request,'Contact.html')
def fnSecondregistration(request):
   return render(request,'Secondregistration.html')
def fnJoblist(request):
   return render(request,'Joblist.html')

def fnAdminlogin(request):
   return render(request,'Adminlogin.html')
def fnAddjob(request):
   return render(request,'Addjob.html')   
         
      
   
