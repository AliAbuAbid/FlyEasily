"""FlyEasily URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from Passengers.views import signup,forgot,Orders,show,rating,loginpage,logout,pay,airplane,download,about,show_newss
from Workers.views import workerorders,reports,switchepassenger,managershowre,show_schedule,show_news
from Managers.views import switchmanager,schedulework,showratings,showre,managerreports,managerfiles,managernews



urlpatterns = [
    #passenger
    path('admin/', admin.site.urls),
    path('register/',signup,name="signup"),
    path('', loginpage,name="login"),
    path('signup/',signup,"signup"),
    path('register/',signup,name="signup"),
    path('forgot/',forgot,name="forgot"),
    path('orders/',Orders,name="orders"),
    path('show/',show,name="show"),
    path('raing/',rating,name="rating"),
    path('',logout,'login.html'),
    path('passengerrating/',showratings,name="passengerrating"),
    path('paypal/',pay,name="paypal"),
    path('airlines/',airplane,name='airplane'),
    path('passenger/files/',download,name='download'),
    path('files/',download,name='download'),
    path('About/',about,name='About'),
    path('news/',show_newss,name='news'),
    path('forgot/',forgot,name="forgot"),

######
    path('passenger/orders/',Orders,name="orders"),
    path('passenger/show/',show,name="show"),
    path('passenger/raing/',rating,name="rating"),
    path('',logout,'login.html'),
    path('passenger/passengerrating/',showratings,name="passengerrating"),
    path('passenger/paypal/',pay,name="paypal"),
    path('passenger/airlines/',airplane,name='airplane'),
    path('passenger/files/',download,name='download'),
    path('files/',download,name='download'),
    path('About/',about,name='About'),
    path('news/',show_newss,name='news'),






    #manager
    path('',logout,name='login.html'),
    path('passeger/',switchmanager,name="passengers"),
    #path('reports/',reports,name="reports")
    path('showre/',showre,name='showre'),
    path('workerorder/',workerorders,name="orders"),
    path('managerschedule/',schedulework,name="managerschedule"),
    path('passenger/raing/',rating,name="rating"),
    path('managerreport/',managerreports,name="managerreport"),
    path('managerfiles/',managerfiles,name="managerfiles"),
    path('managernews/',managernews,name="managernews"),








    #worker
    
    path('reports/',reports,name="reports"),
    path('passenger/',switchepassenger,name="passengers"),
    path('managershowre/',managershowre,name="managershowre"),   
    path('managershowre/',managershowre,name=""),   
    path('schedule/',show_schedule,name="schedule"),   
    path('news/',show_news,name='news'),


    


]