from django.shortcuts import render,redirect
from numpy import roll
from adminapp.models import Student,Attendence
from teacherapp.models import StudyMaterial
from django.core.files.storage import FileSystemStorage


from django.views.decorators.cache import cache_control

# Create your views here.
@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def studenthome(req):
    try:
        if req.session['studentid']!=None:    
            studentid=req.session['studentid']
            student=Student.objects.get(emailaddress=studentid)
            

            return render(req,'studenthome.html',{'studentid':studentid,'student':student})
    except KeyError:
        return redirect('login')
@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def stuattend(req):
    try:
        if req.session['studentid']!=None:    
            studentid=req.session['studentid']
            student=Student.objects.get(emailaddress=studentid)
            att=Attendence.objects.filter(sid=student.id)
            return render(req,'stuattend.html',{'studentid':studentid,'student':student,'att':att})
    except KeyError:
        return redirect('login')
@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def stuslm(req):
    try:
        if req.session['studentid']!=None:    
            studentid=req.session['studentid']
            student=Student.objects.get(emailaddress=studentid)
            slm=StudyMaterial.objects.filter(tclass=student.sclass)
            return render(req,'stuslm.html',{'student':student,'slm':slm})
    except KeyError:
        return redirect('login')

@cache_control(no_store=True,no_cache=True,must_revalidate=True)       
def studentlogout(req):
    try:
        if req.session['studentid']!=None:
            del req.session['studentid']
            return redirect('login')
    except KeyError:
            return redirect('login')

@cache_control(no_store=True,no_cache=True,must_revalidate=True)  
def stchangepass(req):
    try:
        if req.session['studentid']!=None:
            studentid=req.session['studentid']
            student=Student.objects.get(emailaddress=studentid)
            if req.method=="POST":
                oldpassword=req.POST['oldpassword']
                newpassword=req.POST['newpassword']
                cnfpassword=req.POST['cnfpassword']
                if newpassword!=cnfpassword:
                    msg="Password did not match"
                    return render(req,'stchangepass.html',{'msg':msg})
                elif student.password!=oldpassword:
                    msg="Wrong password"
                    return render(req,'stchangepass.html',{'msg':msg})
                elif student.password==oldpassword:
                    Student.objects.filter(emailaddress=studentid).update(password=newpassword)
                    return redirect('login')
            return render(req,'stchangepass.html',{'student':student})
    except KeyError:
        return redirect('login')
    
@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def stprofile(req):
    try:
        if req.session['studentid']!=None:    
            studentid=req.session['studentid']
            student=Student.objects.get(emailaddress=studentid)
            if req.method=="POST":
                rollno=req.POST['rollno']
                name=req.POST['name']
                fname=req.POST['fname']
                mname=req.POST['mname']
                gender=req.POST['gender']
                dob=req.POST['dob']
                contactno=req.POST['contactno']
                address=req.POST['address']
                feepaid=req.POST['feepaid']
                duefees=req.POST['duefees']
               
               
                Student.objects.filter(emailaddress=studentid).update(name=name,rollno=rollno ,fname=fname,mname=mname,gender=gender,dob=dob,contactno=contactno,address=address,feepaid=feepaid,duefees=duefees)

            return render(req,'stprofile.html',{'studentid':studentid,'student':student})
    except KeyError:
        return redirect('login')



@cache_control(no_store=True,no_cache=True,must_revalidate=True)
def uploadpic(req):
     if req.method=="POST":
            studentid=req.session['studentid']
            student=Student.objects.get(emailaddress=studentid)
            pic=req.FILES['pic']
            fs=FileSystemStorage()
            filename=fs.save(pic.name,pic)
            student.pic=filename
            student.save()
            return redirect('studentapp:stprofile')