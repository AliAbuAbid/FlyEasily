from django.shortcuts import render
from Passengers.models import passengers
from Workers.models import report

# Create your views here.
import re
import urllib

from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.models import Group
#from Workers.models import Workerorders
#from Workers.models import Workers
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.shortcuts import render, redirect
#from travil import forms
from django.http import HttpResponseRedirect
from Passengers.models import Passengerorders,passengers
from Workers.models import Workersorders
from Managers.models import schedule,managerreport,news
from django.contrib.auth.forms import UserCreationForm










def show(request):
    ordered = Passengerorders.objects.all()
    return render(request,"passengerorders.html",{ordered:Passengerorders})




def managershowre(request):
        reported = managerreport.objects.all()
       # reported=managerreport.objects.values_list('workername')
        return render(request,"managershowre.html",{'reported':reported})



def show_schedule(request):
    your = schedule.objects.all()
    return render(request,"schedule.html",{'your':your})


def workerorders(request):
    form=UserCreationForm
    if request.method == 'POST':
        cold1 = request.POST['cold']
        hot1 = request.POST['hot']
        name1 = request.POST['worker']
        food1 = request.POST['food']
        other1 = request.POST['other']
        
        Workersorders.objects.create(cold=cold1,hot=hot1,worker=name1,food=food1,other=other1)
        #Workersorders.save()
    return render(request,"workerorder.html",{'form':form})

def reports(request):
    form=UserCreationForm
    if request.method == 'POST':
        count1=request.POST['count']
        name1 = request.POST['name']
        id1 = request.POST['id']
        text1 = request.POST['text']

        report.objects.create(count=count1,name=name1,id=id1,text=text1)
        #report.save()
    return render(request,"reports.html",{'form':form})



def switchepassenger(request):
    return render(request,"passenger.html")


def show_news(request):
    newss = news.objects.all()
    return render(request,"news.html",{'newss':newss})