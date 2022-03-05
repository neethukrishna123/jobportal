from django.shortcuts import render

# Create your views here.

def fnIndex(request):
   return render(request,'index.html')
def fnLoginpage(request1):
   return render(request1,'loginpage.html')
def fnRegistration(request2):
   return render(request2,'Registration.html')
def fnAbout(request3):
   return render(request3,'about.html')
def fnContact(request4):
   return render(request4,'contact.html')
def fnSecondregistration(request5):
   return render(request5,'secondregistration.html')
def fnJoblist(request6):
   return render(request6,'joblist.html')

def fnAdminlogin(req):
   return render(req,'adminlogin.html')
def fnAddjob(req1):
   return render(req1,'addjob.html')  
def fnForgot(req2):
   return render(req2,'forgot.html')  
def fnUserpage(req3):
   return render(req3,'userpage.html') 
         
      
   
