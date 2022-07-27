from django.db import models

# Create your models here.


# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from contextlib import nullcontext
from operator import mod


from django.db import models


# Create your models here.



class schedule(models.Model):
    workername=models.CharField(max_length=40,null=False)
    date=models.DateTimeField(null=False,primary_key=True)
    date1=models.DateTimeField(null=False)


    class Meta:
        db_table="schedule"



class managerreport(models.Model): 
    count=models.IntegerField(null=False,primary_key=True)
    workername=models.CharField(max_length=100,null=False,default="Full Name")
    text=models.CharField(max_length=1000,null=False,default="text")
    class Meta:
        db_table="managerreport"



class passengerfiless(models.Model):
    count=models.IntegerField(null=False,primary_key=True)
    files=models.FileField(null=False)
    passenger_name=models.CharField(null=False,max_length=40)
    passenger_id=models.CharField(null=False,max_length=9)

    class Meta:
        db_table="passengerfiless"


class news(models.Model):
    news=models.CharField(max_length=4000,null=False)
    date=models.DateTimeField(null=False,primary_key=True)

    class Meta:
        db_table="news"