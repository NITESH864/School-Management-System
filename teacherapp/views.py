import datetime
from turtle import title
from django.shortcuts import render,redirect
from adminapp.models import Teacher,Student,Attendence
from . models import StudyMaterial
from django.core.files.storage import FileSystemStorage

# from smsproject.teacherapp.models import StudyMaterial
# Create your views here.
def teacherhome(req):
    try:
        if req.session['teacherid']!=None:
            teacherid=req.session['teacherid']
            teacher=Teacher.objects.get(emailaddress=teacherid)
            stu_count=Student.objects.all().count()

            return render(req,'teacherhome.html',{'teacher':teacher,'stu_count':stu_count})
    except KeyError:
        return redirect('login')
def teacherprofile(req):
    try:
        if req.session['teacherid']!=None:
            teacherid=req.session['teacherid']
            teacher=Teacher.objects.get(emailaddress=teacherid)
            if req.method=="POST":
                name=req.POST['name']
                fname=req.POST['fname']
                mname=req.POST['mname']
                gender=req.POST['gender']
                dob=req.POST['dob']
                contactno=req.POST['contactno']
                address=req.POST['address']
                qualification=req.POST['qualification']
               
                Teacher.objects.filter(emailaddress=teacherid).update(name=name,fname=fname,mname=mname,gender=gender,dob=dob,contactno=contactno,address=address,qualification=qualification)  
                return redirect('teacherapp:teacherprofile')
            return render(req,'teacherprofile.html',{'teacher':teacher})
    except KeyError:
        return redirect('login')
def uploadpic(req):
     if req.method=="POST":
            teacherid=req.session['teacherid']
            teacher=Teacher.objects.get(emailaddress=teacherid)
            pic=req.FILES['pic']
            fs=FileSystemStorage()
            filename=fs.save(pic.name,pic)
            teacher.pic=filename
            teacher.save()
            return redirect('teacherapp:teacherprofile')
def tchangepass(req):
    try:
        if req.session['teacherid']!=None:
            teacherid=req.session['teacherid']
            teacher=Teacher.objects.get(emailaddress=teacherid)
            if req.method=="POST":
                oldpassword=req.POST['oldpassword']
                newpassword=req.POST['newpassword']
                cnfpassword=req.POST['cnfpassword']
                if newpassword!=cnfpassword:
                    msg="Password did not match"
                    return render(req,'tchangepass.html',{'msg':msg})
                elif teacher.password!=oldpassword:
                    msg="Wrong password"
                    return render(req,'tchangepass.html',{'msg':msg})
                elif teacher.password==oldpassword:
                    Teacher.objects.filter(emailaddress=teacherid).update(password=newpassword)
                    return redirect('login')
            return render(req,'tchangepass.html',{'teacher':teacher})
    except KeyError:
        return redirect('login')

def teacherlogout(req):
    try:
        if req.session['teacherid']!=None:
            del req.session['teacherid']
            return redirect('login')
    except KeyError:
            return redirect('login')
def addattend(req):
    try:
        if req.session['teacherid']!=None:
            teacherid=req.session['teacherid']
            teacher=Teacher.objects.get(emailaddress=teacherid)
            st=Student.objects.filter(sclass=teacher.tclass)
            if req.method=="POST":
                sid=req.POST['sid']
                rollno=req.POST['rollno']
                name=req.POST['name']
                status=req.POST['status']

                created_date=req.POST['created_date']
                a=Attendence.objects.filter(sid=sid,created_date=datetime.date.today())
                if a is not None:
                    msg="Already Marked attendenc for this student"
                    return render(req,'addattend.html',{'msg':msg,'st':st,'teacher':teacher})
                else:
                    att=Attendence(sid=sid,name=name,rollno=rollno,sclass=teacher.tclass,tclass=teacher.tclass,status=status,created_date=created_date)
                    att.save()
                    return redirect('teacherapp:addattend')

            return render(req,'addattend.html',{'teacher':teacher,'st':st})
    except KeyError:
        return redirect('login')    
def viewattend(req):
    try:
        if req.session['teacherid']!=None:
            teacherid=req.session['teacherid']
            teacher=Teacher.objects.get(emailaddress=teacherid)
            att=Attendence.objects.filter(sclass=teacher.tclass)


            return render(req,'viewattend.html',{'teacher':teacher,'att':att})
            
    except KeyError:
        return redirect('login')   
def addslm(req):
    try:
        if req.session['teacherid']!=None:
            teacherid=req.session['teacherid']
            teacher=Teacher.objects.get(emailaddress=teacherid)        
            if req.method=="POST":
                title=req.POST['title']
                sm=req.FILES['sm']
                tclass=req.POST['tclass']
                slm=StudyMaterial(title=title,sm=sm,tclass=tclass)
                slm.save()
                return redirect('teacherapp:viewslm')

            return render(req,'addslm.html',{'teacher':teacher})
    except KeyError:
        return redirect('login')      

def viewslm(req):
    try:
        if req.session['teacherid']!=None:
            teacherid=req.session['teacherid']
            teacher=Teacher.objects.get(emailaddress=teacherid)
            att=Attendence.objects.filter(sclass=teacher.tclass)
            slm=StudyMaterial.objects.filter(tclass=teacher.tclass)


            return render(req,'viewslm.html',{'teacher':teacher,'att':att,'slm':slm})
            
    except KeyError:
        return redirect('login')   
