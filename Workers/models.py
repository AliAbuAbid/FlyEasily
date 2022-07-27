from django.db import models

# Create your models here.


# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from contextlib import nullcontext
from operator import mod


from django.db import models


# Create your models here.





class Workersorders(models.Model):
    cold =models.CharField(max_length=100, null=True,default="Cold drink")
    hot =models.CharField(max_length=100, null=True,default="Hot drink")
    worker=models.CharField(max_length=100,null=False,primary_key=True)
    food =models.CharField(max_length=100, null=True,default="Food")
    other =models.CharField(max_length=1000,null=True,default="nothing")
    class Meta:  
        db_table = "Workersorders"  


class report(models.Model): 
    count=models.IntegerField(null=False,primary_key=True)
    name=models.CharField(max_length=100,null=False,default="Full Name")
    id=models.CharField(max_length=10,null=False)
    text=models.CharField(max_length=1000,null=False,default="text")
    class Meta:
        db_table="report"