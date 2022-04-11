from django.shortcuts import render

# Create your views here.

def index(request):
   return render(request,'userapp/index.html')

def loginpage(request1):
   return render(request1,'userapp/loginpage.html')

def registration(request2):
   return render(request2,'userapp/registration.html')

def about(request3):
   return render(request3,'userapp/about.html')

def contact(request4):
   return render(request4,'userapp/contact.html')

def secondregistration(request5):
   return render(request5,'userapp/secondregistration.html')

def joblist(request6):
   return render(request6,'userapp/joblist.html')

def adminlogin(req):
   return render(req,'userapp/adminlogin.html')

def addjob(req1):
   return render(req1,'userapp/addjob.html')  

def forgot(req2):
   return render(req2,'userapp/forgot.html') 

def userpage(req3):
   return render(req3,'userapp/userpage.html')

def userprofile(req3):
   return render(req3,'userapp/userprofile.html') 

def applications(req3):
   return render(req3,'userapp/applications.html') 
   
# def master(req3):
#    return render(req3,'userapp/master.html')
          
         
      
   
