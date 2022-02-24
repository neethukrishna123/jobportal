from django.shortcuts import render

# Create your views here.

def fnIndex(request):
   return render(request,'index.html')
def fnLoginpage(requ):
   return render(requ,'loginpage.html')
def fnRegistration(reque):
   return render(reque,'Registration.html')
def fnAbout(reques):
   return render(reques,'About.html')
def fnContact(req):
   return render(req,'Contact.html')
def fnSecondregistration(req):
   return render(req,'Secondregistration.html')
def fnJoblist(req):
   return render(req,'Joblist.html')

def fnAdminlogin(req):
   return render(req,'Adminlogin.html')
def fnAddjob(req):
   return render(req,'Addjob.html')   
         
      
   
