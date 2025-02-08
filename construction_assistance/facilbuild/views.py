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
            elif user.usertype=='user':
                return redirect('/user_home')
            elif user.usertype=='worker':
                return redirect('/worker_home')
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
        certi=request.FILES['certi']
        wrk_hrs=request.POST['wrk_hrs']
        if login_tbl.objects.filter(username=email).exists():
            messages.error(request,'User already exists')
        else:
            log=login_tbl.objects.create_user(username=email,password=password,usertype='contractor')
            log.save()
            contractor=Contractor.objects.create(name=name,email=email,phone=phone,cmp_name=cmp_name,
            srv_cat=srv_cat,expc=expc,certi=certi,wrk_hrs=wrk_hrs,user=log)
            contractor.save()
            messages.success(request,'Registration Successfull')
            return redirect("/login")

    return render(request,"contra_reg.html") 
def contra_home(request):
    return render(request,"contra_home.html") 
def user_reg(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['tele']
        password=request.POST['password']
        city=request.POST['city']
        address=request.POST['address']
        if login_tbl.objects.filter(username=email).exists():
            messages.error(request,'User already exists')
        else:
            log=login_tbl.objects.create_user(username=email,password=password,usertype='user')
            log.save()
            user=User.objects.create(name=name,email=email,phone=phone,address=address,city=city,user=log)
            user.save()
            messages.success(request,'Registration Successfull')
            return redirect("/login")
    return render(request,"user_reg.html") 
def worker_reg(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['tele']
        password=request.POST['password']
        skills=request.POST['skills']
        expc=request.POST['expc']
        if login_tbl.objects.filter(username=email).exists():
            messages.error(request,'User already exists')
        else:
            log=login_tbl.objects.create_user(username=email,password=password,usertype='worker')
            log.save()
            worker=Worker.objects.create(name=name,email=email,phone=phone,skills=skills,expc=expc,user=log)
            worker.save()
            messages.success(request,'Registration Successfull')
            return redirect("/contra_home")
    return render(request,"worker_reg.html") 
def admin_home(request):
    return render(request,"admin_home.html")
def worker_home(request):
    return render(request,"worker_home.html")
def user_home(request):
    return render(request,"user_home.html")
def adcont_view(request):
    contractor=Contractor.objects.all()
    return render(request,"adcont_view.html",{"contractor":contractor}) 
def adwr_view(request):
    worker=Worker.objects.all()
    return render(request,"adwr_view.html",{"worker":worker}) 
def adusr_view(request):
    user=User.objects.all()
    return render(request,"adusr_view.html",{"user":user}) 
def admin_approval_contractor(request):
    uid=request.GET.get("id")
    contractor=login_tbl.objects.get(id=uid)
    contractor.is_active=1
    contractor.save()
    messages.success(request,"Approved successfully")
    return redirect("/adcont_view")
def admin_approval_user(request):
    uid=request.GET.get("id")
    user=login_tbl.objects.get(id=uid)
    user.is_active=1
    user.save()
    messages.success(request,"Approved successfully")
    return redirect("/adusr_view")
def admin_reject_contractor(request):
    uid=request.GET.get("id")
    contractor=login_tbl.objects.get(id=uid)
    contractor.is_active=0
    contractor.save()
    messages.success(request,"Rejected successfully")
    return redirect("/adcont_view")
def admin_reject_user(request):
    uid=request.GET.get("id")
    user=login_tbl.objects.get(id=uid)
    user.is_active=0
    user.save()
    messages.success(request,"Rejected successfully")
    return redirect("/adusr_view")