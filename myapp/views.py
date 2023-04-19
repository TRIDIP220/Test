from django.shortcuts import render
from django.http import HttpResponse
from .models import User

def First(request):
    return render(request ,"index.html")

def fetch(request):
    u = User()
    u.Fname = request.GET['Fname']
    u.Lname = request.GET['Sname']
    u.save()
    return render(request,'Index.html')

def show(request):
    u = User.objects.all()
    return render(request,'show.html',{'x':u})
