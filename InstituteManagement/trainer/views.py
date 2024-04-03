from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from Student.models import StudentData


# Create your views here.
def trainer_home(request):
    return render(request,'trainerhome.html')


def login_fun(request):
    if request.method=='POST':
        name = request.POST['txtname']
        password = request.POST['txtpassword']
        user = authenticate(username=name,password=password)
        if user is not None:
            if user.is_superuser:
                return  HttpResponse(f"<h1>successfully loged in</h1>")
            else:
                return render(request,'trainerlogin.html')
        else:
            return render(request,'trainerlogin.html')
    else:
        return render(request,'trainerlogin.html')


def signup_fun(request):
    if request.method=='POST':
        name=request.POST['txtname']
        email=request.POST['txtemail']
        password=request.POST['txtpassword']
        if User.objects.filter(Q(username=name)|Q(email=email)|Q(password=password)).exists():
            return render(request,'trainersignup.html')
        else:
            u1=User.objects.create_superuser(username=name,email=email,password=password)
            u1.save()
            return render(request,'trainerlogin.html')
    return render(request,'trainersignup.html')


def add_fun(request):
    return render(request,'studentreg.html')


def display_fun(request):
    data=StudentData.objects.all()
    return render(request,'trainerdisplay.html',{"data":data})


def update_fun(request,id):
    s1 = StudentData.objects.get(id=id)
    if request.method=="POST":
        s1.name=request.POST["name"]
        s1.age=request.POST["age"]
        s1.mobile=request.POST["mobile"]
        s1.email=request.POST["email"]
        s1.gender=request.POST["gender"]
        if "skills" in request.POST:
            skills = request.POST.getlist("skills")
            s1.skills=",".join(skills)
        else:
            s1.skills=""

        s1.place=request.POST["place"]
        s1.education=request.POST["education"]
        s1.save()
        return  redirect('display')
    return render(request,'trainerupdate.html',{"data":s1})


def delete_fun(request,id):
    s1=StudentData.objects.get(id=id)
    s1.delete()
    return redirect('display')


def logout_fun(request):
    return render(request,'trainerhome.html')