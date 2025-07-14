from django.shortcuts import render,redirect


from.models import Enquiry,AdminLogin

import datetime
from django.core.exceptions import ObjectDoesNotExist
from adminapp.models import Teacher,Student,Notification

# Create your views here.
def index(req):
    noti=Notification.objects.all()

    return render(req,"index.html",{'noti':noti})
def about(req):
     return render(req,"about.html")
def contact(req):
     if req.method=="POST":
          name=req.POST['name']
          email=req.POST['email']
          Contactno=req.POST['Contactno']
          enquirytext=req.POST['enquirytext']
          enq=Enquiry(name=name,email=email,Contactno=Contactno,enquirytext=enquirytext)
          enq.save()
          # msg="your enquiry is submitted succefully"
          return render(req,'contact.html',locals())
     return render(req,'contact.html')
def about2(req):
     return render(req,"about2.html") 
def about3(req):
     return render(req,"about3.html")   
def about4(req):
     return render(req,"about4.html")
def about5(req):
     return render(req,"about5.html")

def about6(req):
     return render(req,"about6.html")
def about7(req):
     return render(req,"about7.html")
def about8(req):
     return render(req,"about8.html")
def acadmic(req):
     return render(req,"acadmic.html")
def carrier(req):
     return render(req,"carrier.html")
def transport(req):
     return render(req,"transport.html")
def medical(req):
     return render(req,"medical.html")
def smartclass(req):
     return render(req,"smartclass.html")
def otfacilities(req):
     return render(req,"otfacilities.html")
def admission1(req):
     return render(req,"admission1.html")
def admission2(req):
     return render(req,"admission2.html")
def admission3(req):
     return render(req,"admission3.html")
def media1(req):
     return render(req,"media1.html")

def media2(req):
     return render(req,"media2.html")




def login(req):
     return render(req,"login.html")
def logcode(req):
     if req.method=="POST":
          usertype=req.POST['usertype']
          userid=req.POST['userid']
          password=req.POST['password']
          if usertype=="admin":              
               try:
                    user=AdminLogin.objects.get(userid=userid,password=password)
                    if user is not None:
                          req.session['adminid']=userid
                         
                          return redirect('adminapp:adminhome')
               except ObjectDoesNotExist:
                    return render(req,'login.html',{'msg':'Invalid user'})
          elif usertype=="teacher":
               try:
                    teacher=Teacher.objects.get(emailaddress=userid,password=password)
                    if teacher is not None:
                         req.session['teacherid']=userid
                         return redirect('teacherapp:teacherhome')
               except ObjectDoesNotExist:
                    return render(req,'login.html',{'msg':'Invalid user'})
          
          
          elif usertype=="student":
               try:
                    student=Student.objects.get(emailaddress=userid,password=password)
                    if student is not None:
                         req.session['studentid']=userid
                         return redirect('studentapp:studenthome')
               except ObjectDoesNotExist:
                    return render(req,'login.html',{'msg':'Invalid user'})
          else:
               return render(req,'login.html')
                    
                
                   
               
