from django.shortcuts import redirect, render
import urllib.request
from django.contrib.messages import constants as messages
#from Managers.models import workers
import MySQLdb
from django.contrib import messages
from Passengers.models import passengers
from django.http import HttpResponse
from Managers.models import schedule,managerreport,passengerfiless,news

from django.contrib.auth import authenticate, login, logout

from Passengers.models import ratings

from django.contrib.auth.forms import UserCreationForm
from Workers.models import report

global user





def logoutpage(request):
    logout(request)
    return render('login.html')    
        



def showre(request):  
     reported = report.objects.all()  
     return render(request,"showre.html",{'reported':reported})  




def switchmanager(request):
    return render(request,"passengers.html")


def schedulework(request):
    form=UserCreationForm
    if request.method=='POST':
        workername1=request.POST['workername']
        date1=request.POST['date']
        date11=request.POST['date1']


        schedule.objects.create(workername=workername1,date=date1,date1=date11)
        #schedule.save()
        return render(request,"managerschedule.html",{'form':form})
    else:
        return render(request,"managerschedule.html")



def showratings(request):
	rate=ratings.objects.all() 
	return render(request,'passengerrating.html',{'rate':rate})


def managerreports(request):
    form=UserCreationForm
    if request.method == 'POST':
        count1=request.POST['count']
        name1 = request.POST['workername']
        text1 = request.POST['text']

        managerreport.objects.create(count=count1,workername=name1,text=text1)
        #managerreport.save()
    return render(request,"managerreport.html",{'form':form})


def managerfiles(request):
    form=UserCreationForm
    if request.method == 'POST':
        count1=request.POST['count']
        file1 = request.POST['files']
        name1 = request.POST['passenger_name']
        id1 = request.POST['passenger_id']


        passengerfiless.objects.create(count=count1,files=file1,passenger_name=name1,passenger_id=id1)
        #passengerfiless.save()
    return render(request,"managerfiles.html",{'form':form})



def managernews(request):
    form=UserCreationForm
    if request.method=='POST':
        news1=request.POST['news']
        date1=request.POST['date']

        news.objects.create(news=news1,date=date1)
        #schedule.save()
        return render(request,"managernews.html",{'form':form})
    else:
        return render(request,"managernews.html")
