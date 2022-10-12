from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import Feedback,Flight,Profile

def home(request):
    if request.method == 'POST':
        frommm=request.POST.get('fromm')
        too=request.POST.get('too')
        datee=request.POST.get('datee')
        flights=Flight.objects.all().order_by('datee')
        print(datee)
        filters=Flight.objects.filter(fromm__icontains=frommm,to__icontains=too)
        return render(request,'homePage.html',{'filters':filters,'flights':flights})
    return render(request,'homePage.html')

def about(request):
    return render(request,'aboutUS.html')

def feedback(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        username=request.POST.get('username')
        address=request.POST.get('address')
        gender=request.POST.get('gender')
        message=request.POST.get('message')
        entry=Feedback(email=email,username=username,address=address,
        gender=gender,message=message)
        entry.save()
        if entry:
            messages.success(request,'Thank you for your feedback!! ')
        return render(request,'feedback.html')
    return render(request,'feedback.html')

@login_required
def profile(request):
    queryset=Profile.objects.order_by()
    return render(request,'profile.html',{'qset1':queryset})

def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return render(request,'register.html')
            elif len(password) <8:
                messages.info(request,'ATLEAST 8 CHARACTER PASSWORD NEEDED')
                return render(request,'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return render(request,'register.html')
            else:
                entry=User.objects.create_user(username=username,email=email,password=password)
                entry.save()
                return HttpResponseRedirect('/')
        else:
            messages.info(request,'Password and confirm password didn"t match')
    return render(request,'register.html')

def logout(request):
    auth_logout(request)
    messages.success(request,'Logout Successful')
    return HttpResponseRedirect('/login')

def pay(request,flight_from,flight_to):
    qset=Flight.objects.filter(fromm=flight_from,to=flight_to)
    qset1=Flight.objects.get(fromm=flight_from,to=flight_to)
    return render(request,'pay.html',{'qset':qset,'qset1':qset1})

