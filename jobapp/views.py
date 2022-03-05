from django.shortcuts import render

# Create your views here.

def fnIndex(request):
   return render(request,'index.html')
def fnLoginpage(request1):
   return render(request1,'loginpage.html')
def fnRegistration(request2):
   return render(request2,'Registration.html')
def fnAbout(request3):
   return render(request3,'About.html')
def fnContact(request4):
   return render(request4,'Contact.html')
def fnSecondregistration(request5):
   return render(request5,'Secondregistration.html')
def fnJoblist(request6):
   return render(request6,'joblist.html')

def fnAdminlogin(req):
   return render(req,'Adminlogin.html')
def fnAddjob(req1):
   return render(req1,'Addjob.html')  
def fnForgot(req2):
   return render(req2,'Forgot.html')  
def fnUserpage(req3):
   return render(req3,'Userpage.html') 
         
      
   
