from django.contrib.auth import authenticate
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
import qrcode
from Student.models import Student, StudentData

def student_home(request):
    return render(request,'studenthome.html')

def studentlogin(request):
    if request.method == "POST":
        email=request.POST["txtmail"]
        password=request.POST["txtpswd"]
        try:
            user = Student.objects.get(email=email)
            if user.password == password:
                return render(request,'studentmainhome.html')
            else:
                return render(request, 'studentlogin.html')
        except Student.DoesNotExist:
            return render(request, 'studentlogin.html')
    return render(request,'studentlogin.html')


def studentsignup(request):
    if request.method == "POST":
        name=request.POST["txtname"]
        email=request.POST["txtmail"]
        password=request.POST["txtpswd"]
        if Student.objects.filter(Q(name=name)|Q(email=email)).exists():
            return render(request,'studentsign.html')
        else:
            s1 = Student(name=name,email=email,password=password)
            s1.save()
            return redirect('login')
    return render(request,'studentsign.html')


def student_filldata(request):
    if request.method=="POST":
        name=request.POST["name"]
        age=request.POST["age"]
        mobile=request.POST["mobile"]
        email=request.POST["email"]
        gender=request.POST["gender"]
        if "skills" in request.POST:
            skills = request.POST.getlist("skills")
        else:
            skills = []
        place=request.POST["place"]
        education=request.POST["education"]
        image = request.FILES.get("image")
        s1 = StudentData(name=name,age=age,mobile=mobile,email=email,gender=gender,skills=skills,place=place,education=education,image=image)
        s1.save()
        return HttpResponse("<h1>success</h1>")
    return render(request,'studentreg.html')


def studentqrgenerate(request):
    try:
        students = StudentData.objects.all()
        for student in students:
            name = student.name
            mobile = student.mobile
            qr_img = qrcode.make(f"{name}:{mobile}")
            qr_img.save(f"c://qrcode//{name}_{mobile}.png")
    except:
        return HttpResponse('<h1>please fill your details </h1>')
    else:

        return HttpResponse('<h1>successfully generated</h1>')