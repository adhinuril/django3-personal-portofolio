from django.shortcuts import render
from .models import Project

def home(request) :
    projects = Project.objects.all()
    return render(request,'portofolio/home.html',{'projects':projects})
