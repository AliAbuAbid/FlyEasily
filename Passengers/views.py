from msilib.schema import Error
from django.http import HttpResponse
from django.shortcuts import redirect, render
import urllib.request
from django.contrib.messages import constants as messages
from Passengers.models import passengers,Passengerorders,ratings
import MySQLdb
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, login, logout
from Managers.models import passengerfiless,news

import requests
import json

global user
user = ()
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = MySQLdb.connect(db_file)
    except:
        print("error")

    return conn



    
    
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('fn')
        password = request.POST.get('password2')
        JOb = request.POST.get('job')


        passenger = passengers.objects.get(fn=username)
    
        if passenger.password2 == password and passenger.job=="Passenger":
            return render(request,"passenger.html")
        elif(passenger.password2==password and passenger.job=="Worker"):
            return render(request,"worker.html")
        elif(passenger.password2==password and passenger.job=="Manager"):
            return render(request,"manager.html")
        else:            
            messages.info(request, 'Username or password is incorrect')
            return render(request,"login.html")
    template_name = 'login.html'
    return render(request, template_name)

#@login_required(login_url='loginpage')
def logoutpage(request):
    logout(request)
    return render('login.html')

#########################################################
    
def signup(request):
    form=UserCreationForm
    if request.method == 'POST':
        passport = request.POST['id']
        fullname = request.POST['fn']
        JOb1 = request.POST['job']
        email1 = request.POST['email']
        phone = request.POST['phone']
        gender = request.POST['gender']
        age = request.POST['age']
        password11=request.POST['password1']
        password22=request.POST['password2']
        country1 = request.POST['country']
        if(password11==password22):
            passengers.objects.create(id=passport,fn=fullname,job=JOb1,email=email1,phone=phone,gender=gender,age=age,password1=password11,password2=password22,country=country1)


        return render(request,'signup.html',{'form':form})

        
    return render(request, 'signup.html')

def Orders(request):
    form=UserCreationForm
    if request.method == 'POST':
        cold1 = request.POST['cold']
        hot1 = request.POST['hot']
        chair1 = request.POST['chair']
        food1 = request.POST['food']
        other1 = request.POST['other']
        
        Passengerorders.objects.create(cold=cold1,hot=hot1,chair=chair1,food=food1,other=other1)
        #Passengerorders.save()
        
        
    return render(request, 'orders.html',{'form':form})


def Home(request):
    content = {}
    lst = passengers.objects.all()
    content = {'RegisterationForm': lst}
    return render(request, 'home.html', content)



def Index(request):
    return render(request, 'index.html')

def rating(request):
    if request.method == 'POST':
        name1 = request.POST['name']
        worker1 = request.POST['id']
        rating1 = request.POST['rating']
        
        ratings.objects.create(name=name1,id=worker1,rating=rating1)
        #ratings.save()
        
        
    return render(request, 'rating.html')







def forgot(request):
    # password1 = passengers.objects.get(password1=password1)
    # password2 = passengers.objects.get(password2=password2)  
    if request.method == 'POST':
        username = request.POST.get('id')
        password = request.POST.get('password2')
        passenger = passengers.objects.get(id=username)
        if(username==id.passenger):
            name1 = request.POST['password1']
            worker1 = request.POST['password2']
            if(passengers.password1==passengers.password2):
                passengers.objects.create(password1=name1,password2=worker1)
        

    return render(request,'forgot.html')


    




def show(request):  
    ordered = Passengerorders.objects.all()  
    return render(request,"show.html",{'ordered':ordered})  

def pay(request):
    return render(request,"paypal.html")


import urllib

def airplane(request):
    data=requests.get('https://data.gov.il/api/3/action/datastore_search?resource_id=e83f763b-b7d7-479e-b172-ae981ddc6de5&limit=10').json()
    x=data["result"]["records"]
    
    return render(request, 'airlines.html',{"data":x})


def download(request):
        File = passengerfiless.objects.all()  
        return render(request,"download.html",{'File':File})  


def about(request):
    return render(request,"About.html")



def show_newss(request):
    newss = news.objects.all()
    return render(request,"news.html",{'newss':newss})