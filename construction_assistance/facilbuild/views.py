from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from .models import *

# Create your views here.
def index(request):
    return render(request,"index.html")
def login(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(username=email,password=password)
        if user is None:
            messages.error(request,'Invalid Username or Password')
        else:
            if user.is_superuser:
                return redirect('/admin_home')
            elif user.usertype=='contractor':
                 return redirect('/contra_home')
            elif user.usertype=='manager':
                return redirect('/managerhome')
            else:
                messages.error(request,'Invalid Username or Password')
    return render(request,"login.html")
def contra_reg(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['tele']
        password=request.POST['password']
        cmp_name=request.POST['cmp_name']
        srv_cat=request.POST['srv_cat']
        expc=request.POST['expc']
        certi=request.Files['certi']
        wrk_hrs=request.POST['wrk_hrs']
        if login_tbl.objects.filter(username=email).exists():
            messages.error(request,'User already exists')
        else:
            log=login_tbl.objects.create_user(username=email,password=password,usertype='contractor')
            log.save()
            contractor=Contractor.objects.create(name=name,email=email,phone=phone,cmp_name=cmp_name,srv_cat=srv_cat,expc=expc,certi=certi,wrk_hrs=wrk_hrs,user=log)
            contractor.save()
            messages.success(request,'Registration Successfull')
            return redirect("/login")

    return render(request,"contra_reg.html") 
def contra_home(request):
    return render(request,"contra_home.html") 
def user_reg(request):
    return render(request,"user_reg.html") 
def worker_reg(request):
    return render(request,"worker_reg.html") 
def admin_home(request):
    return render(request,"admin_home.html")
def adcont_view(request):
    contractor=Contractor.objects.all()
    return render(request,"adcont_view.html",{"contractor":contractor}) 